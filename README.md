# 🥗 NutritionAI

O **NutritionAI** é um sistema de perguntas e respostas baseado em Inteligência Artificial que utiliza a arquitetura **RAG (Retrieval-Augmented Generation)** para responder dúvidas sobre nutrição a partir de documentos técnicos e científicos.

Diferente de um chatbot tradicional, o sistema não responde apenas com o conhecimento do modelo de linguagem. Antes de gerar uma resposta, ele pesquisa uma base de documentos, recupera os trechos mais relevantes e utiliza essas informações como contexto, tornando as respostas mais confiáveis e fundamentadas.

O NutritionAI foi desenvolvido para demonstrar a aplicação prática de técnicas modernas de Inteligência Artificial Generativa na construção de um sistema de perguntas e respostas baseado em documentos. O projeto reúne conceitos de **RAG**, **busca semântica**, **bancos vetoriais** e **orquestração com LangGraph**, evidenciando uma arquitetura modular e escalável.

---

# 📸 Demonstração

### ✅ Pergunta dentro do domínio da nutrição

A aplicação recupera automaticamente os documentos mais relevantes da base de conhecimento e gera uma resposta fundamentada utilizando **RAG**, **FAISS**, **LangGraph** e **Llama 3 (Ollama)**.

<p align="center">
  <img src="Pergunta valida.png" alt="Pergunta válida" width="100%">
</p>

---

### 🚫 Pergunta fora do domínio

Quando a pergunta não pertence ao domínio da nutrição, o sistema identifica que não há contexto relevante e evita gerar respostas utilizando conhecimento externo.

<p align="center">
  <img src="Pergunta negada.png" alt="Pergunta negada" width="70%">

# 🚀 Tecnologias utilizadas

- Python 3.12
- LangChain
- LangGraph
- FAISS
- Ollama
- Embeddings locais
- Retrieval-Augmented Generation (RAG)

---

# ✨ Principais funcionalidades

- Consulta em linguagem natural
- Busca semântica utilizando embeddings
- Recuperação automática dos trechos mais relevantes
- Geração de respostas fundamentadas em documentos científicos
- Criação automática do banco vetorial (FAISS)
- Restrição de respostas para perguntas fora do domínio da nutrição
- Arquitetura modular para facilitar manutenção e evolução do projeto

---

# 🧠 Como o projeto funciona

O NutritionAI segue o fluxo abaixo:

```text
Documentos PDF
        │
        ▼
Leitura dos documentos
        │
        ▼
Divisão em chunks
        │
        ▼
Geração de Embeddings
        │
        ▼
FAISS (Banco Vetorial)
        │
        ▼
Busca Semântica
        │
        ▼
LangGraph
        │
        ▼
LLM Local (Ollama)
        │
        ▼
Resposta ao usuário
```

Sempre que uma pergunta é feita, o sistema pesquisa os documentos da base de conhecimento, recupera os trechos mais relevantes e utiliza essas informações como contexto para que o modelo de linguagem gere uma resposta fundamentada.

---

# 📂 Estrutura do projeto

```text
nutrition-ai/
│
├── app/
│   ├── api/
│   ├── chains/
│   ├── config/
│   ├── embeddings/
│   ├── graph/
│   ├── ingestion/
│   ├── prompts/
│   ├── services/
│   ├── utils/
│   ├── vectordb/
│   ├── graph.py
│   ├── pdf_loader.py
│   └── rag.py
│
├── data/
├── tests/
├── logs/
├── main.py
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/AndressaGAmorim/nutrition-ai.git
```

## 2. Acesse a pasta do projeto

```bash
cd nutrition-ai
```

## 3. Crie um ambiente virtual

```bash
python -m venv venv
```

## 4. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

## 6. Certifique-se de que o Ollama esteja em execução

O projeto utiliza um modelo local por meio do Ollama. Antes de executar a aplicação, inicie o serviço e verifique se o modelo configurado no projeto está disponível.

## 7. Execute a aplicação

```bash
python main.py
```

Na primeira execução, caso o banco vetorial (`faiss_db`) não exista, ele será criado automaticamente a partir dos documentos presentes na pasta `data`.

---

# 📚 Base de conhecimento

A base de conhecimento é composta por documentos técnicos e científicos da área de nutrição armazenados na pasta `data`.

Durante a inicialização da aplicação, esses documentos são:

- carregados;
- divididos em pequenos trechos (*chunks*);
- convertidos em embeddings;
- indexados automaticamente utilizando FAISS.

---

# 🎯 Objetivo do projeto

Este projeto foi desenvolvido para consolidar conhecimentos em Inteligência Artificial Generativa e demonstrar a aplicação prática de tecnologias modernas na construção de sistemas baseados em recuperação de informação.

Os principais conceitos explorados foram:

- Retrieval-Augmented Generation (RAG)
- LangChain
- LangGraph
- Bancos Vetoriais (FAISS)
- Embeddings
- Engenharia de Prompts
- Modelos de Linguagem executados localmente com Ollama

---

# 🔮 Melhorias futuras

- Interface Web
- API REST
- Upload de novos documentos pela interface
- Histórico de conversas
- Avaliação automática das respostas
- Deploy em nuvem
- Cache de consultas

---

# 👩‍💻 Desenvolvido por

**Andressa Grazioli Amorim**

Projeto desenvolvido como parte do meu portfólio para demonstrar conhecimentos em **Inteligência Artificial Generativa**, **Processamento de Linguagem Natural**, **Recuperação de Informação** e desenvolvimento de aplicações utilizando **Python**.

🔗 GitHub: https://github.com/AndressaGAmorim