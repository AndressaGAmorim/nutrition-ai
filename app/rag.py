from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class RAGEngine:

    def __init__(self, vectorstore: FAISS, llm: ChatOllama):

        self.vectorstore = vectorstore
        self.llm = llm
        self.cache = {}

    # ========================================================
    # CHECK DE DOMÍNIO (CORRETO AGORA)
    # ========================================================
    def is_in_domain(self, question: str):

        docs = self.vectorstore.similarity_search_with_score(
            question,
            k=1
        )

        if not docs:
            return False

        _, score = docs[0]

        logger.info(f"TOP1 SCORE: {score}")

        # REGRA PRÁTICA (FUNCIONA MELHOR QUE THRESHOLD FIXO)
        # FAISS: menor = melhor (distância)
        return score < 1.0

    # ========================================================
    # RETRIEVAL
    # ========================================================
    def retrieve(self, question: str, k: int = 5):

        docs_with_score = self.vectorstore.similarity_search_with_score(
            question,
            k=k
        )

        contexts = []

        logger.info("=== RETRIEVAL START ===")

        for doc, score in docs_with_score:
            logger.info(f"SCORE: {score}")
            contexts.append(doc.page_content)

        logger.info(f"TOTAL CONTEXTS: {len(contexts)}")
        logger.info("=== RETRIEVAL END ===")

        return contexts

    # ========================================================
    # PROMPT
    # ========================================================
    def build_prompt(self, question: str, contexts: list[str]):

        context_text = "\n\n".join(contexts)

        return f"""
Você é um assistente especialista em nutrição.

Responda de forma clara e educativa.

REGRAS:
- Use SOMENTE o contexto
- Se não houver informação suficiente, diga que não encontrou
- Não invente nada

Contexto:
{context_text}

Pergunta:
{question}

Resposta:
"""

    # ========================================================
    # GENERATE
    # ========================================================
    def generate(self, prompt: str):

        response = self.llm.invoke(prompt)
        return response.content

    # ========================================================
    # PIPELINE FINAL
    # ========================================================
    def query(self, question: str):

        # 🔴 BLOQUEIO INTELIGENTE
        if not self.is_in_domain(question):
            return "Essa pergunta está fora da base de conhecimento de nutrição."

        contexts = self.retrieve(question)

        if not contexts:
            return "Não encontrei informações relevantes na base."

        prompt = self.build_prompt(question, contexts)

        return self.generate(prompt)