# 📄 AI-Powered PDF Q&A App

This project is an AI-powered Question-Answering (Q&A) application that lets users upload a PDF document and interact with its content using natural language queries. Built with Streamlit and powered by an Agentic RAG (Retrieval-Augmented Generation) architecture, the app extracts, embeds, and retrieves document knowledge in real-time.

## 🚀 Features

- ✅ Upload PDF documents and ask natural language questions
- 🧠 Uses OpenAI's GPT-4o for contextual responses
- 🗃️ Builds a vector database from your PDF using Qdrant (in-memory)
- 📚 Knowledge base powered by Agno's PDFReader
- 🧠 Agent memory stored in SQLite
- 🔄 Persistent document memory with intelligent search and retrieval

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **LLM:** OpenAI GPT-4o
- **RAG Framework:** [Agno](https://pydantic-ai.github.io/agno/)
- **Vector DB:** Qdrant (in-memory)
- **Memory DB:** SQLite
- **Containerization:** Docker

## 📂 Project Structure

.
├── app.py # Streamlit app interface
├── pdf_rag.py # RAGPDF class to manage vector DB, memory, and agent
├── Dockerfile # Dockerfile to run the app
└── temp.pdf # Temporary uploaded file (generated at runtime)


## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-rag-app.git
cd pdf-rag-app
```

### 2. Create a `.env` file in your folder

Add the needed API Keys: OpenAI


#### 3. Run Locally (Without Docker)

Install dependencies:

```python
pip install -r requirements.txt
```

Run the Streamlit app:

```python
streamlit run app.py
```

#### 4. Run with Docker

Build the Docker image:

```bash
docker-compose up
```

Access the app in your browser at http://localhost:8501.

## 🧪 Example Usage

Upload any PDF file (e.g., a research paper or report).

Enter a question like:
`"What is the main topic in this document?"`

The app will return a contextualized answer, retrieving relevant parts of the document.

📌 Notes
By default, the app uses an in-memory Qdrant instance, which is not persistent.

Memory is stored in a temporary SQLite file under `tmp/memory.db` for the local run.

## 📄 License

This project is licensed under the MIT License.

## About

Made with ❤️ using Agno and Streamlit

Author: [Gustavo R. Santos](https://gustavorsantos.me)