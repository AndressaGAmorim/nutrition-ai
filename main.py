import langchain_ollama
import langchain_community.vectorstores
import langchain_community.embeddings

from app.pdf_loader import load_documents
from app.rag import RAGEngine
from app.graph import RAGGraph

import os


llm = langchain_ollama.ChatOllama(model="llama3")

documents = load_documents()

embedding_model = langchain_community.embeddings.HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

DB_FAISS_PATH = "faiss_db"

if os.path.exists(DB_FAISS_PATH):

    print("\nCarregando banco vetorial salvo...")

    vectorstore = langchain_community.vectorstores.FAISS.load_local(
        DB_FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

else:

    print("\nCriando novo banco vetorial...")

    vectorstore = langchain_community.vectorstores.FAISS.from_documents(documents, embedding_model)
    vectorstore.save_local(DB_FAISS_PATH)

    print("\nBanco vetorial salvo com sucesso!")


rag = RAGEngine(vectorstore, llm)
graph = RAGGraph(rag)


while True:

    question = input("\nPergunta: ")

    if question.lower().strip() == "sair":
        break

    answer = graph.run(question)

    print("\nResposta:")
    print(answer)