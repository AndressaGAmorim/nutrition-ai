from typing import TypedDict, List
from langgraph.graph import StateGraph, END


class GraphState(TypedDict):
    question: str
    contexts: List[str]
    answer: str


class RAGGraph:

    def __init__(self, rag_engine):
        self.rag = rag_engine
        self.graph = self.build_graph()

    # ========================================================
    # NODE 1 — RETRIEVE
    # ========================================================
    def retrieve_node(self, state: GraphState):

        question = state["question"]

        contexts = self.rag.retrieve(question)

        return {"contexts": contexts}

    # ========================================================
    # NODE 2 — GENERATE
    # ========================================================
    def generate_node(self, state: GraphState):

        question = state["question"]
        contexts = state["contexts"]

        if not contexts:
            return {
                "answer": "Não encontrei informações relevantes na base de conhecimento."
            }

        prompt = self.rag.build_prompt(question, contexts)
        answer = self.rag.generate(prompt)

        return {"answer": answer}

    # ========================================================
    # GRAPH
    # ========================================================
    def build_graph(self):

        graph = StateGraph(GraphState)

        graph.add_node("retrieve", self.retrieve_node)
        graph.add_node("generate", self.generate_node)

        graph.set_entry_point("retrieve")

        graph.add_edge("retrieve", "generate")
        graph.add_edge("generate", END)

        return graph.compile()

    # ========================================================
    # RUN (CORRIGIDO)
    # ========================================================
    def run(self, question: str):

        # 🔴 usa o nome correto do RAG
        if not self.rag.is_in_domain(question):
            return "Essa pergunta está fora da base de conhecimento de nutrição."

        result = self.graph.invoke({
            "question": question,
            "contexts": [],
            "answer": ""
        })

        return result["answer"]