from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path


# ============================================================
# CARREGAMENTO ROBUSTO DE PDFs
# ============================================================

def load_documents():

    # caminho absoluto baseado no arquivo atual
    BASE_DIR = Path(__file__).resolve().parent
    DATA_PATH = BASE_DIR.parent / "data"   # ajusta para raiz do projeto

    print(f"\n📂 Procurando PDFs em: {DATA_PATH}")

    loader = PyPDFDirectoryLoader(str(DATA_PATH))
    documents = loader.load()

    print(f"📄 Documentos carregados: {len(documents)}")

    if len(documents) == 0:
        print("❌ Nenhum PDF encontrado. Verifique a pasta data/")
        return []

    # ========================================================
    # CHUNKING
    # ========================================================
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " "]
    )

    chunks = text_splitter.split_documents(documents)

    print(f"🧩 Chunks gerados: {len(chunks)}")

    cleaned_chunks = [
        chunk for chunk in chunks
        if len(chunk.page_content.strip()) > 50
    ]

    print(f"✨ Chunks após limpeza: {len(cleaned_chunks)}")

    return cleaned_chunks