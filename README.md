# Mantine Expert

Mantine Expert is an AI-powered chatbot that answers questions about the [Mantine UI framework](https://mantine.dev/) using Retrieval-Augmented Generation (RAG). It leverages LangChain, Ollama, and FAISS to ingest Mantine documentation and provide context-aware responses.

## Features

- RAG-powered chatbot for Mantine UI
- Runs locally using Ollama
- Ingests official Mantine documentation and guides
- Provides complete, runnable Mantine React code examples when possible
- Built with Streamlit for an interactive chat interface

### **Technical Requirements**

* **Reasonably powerful computer:** ideally something with >= 16GB RAM.
* **Ollama:** Must be installed and running on your system.
* **Python:** Version 3.10 or higher.
* **A Modern Browser:** For the Streamlit web interface.

### **Technologies Used**

* **LangChain:** The core framework for orchestrating the RAG pipeline.
* **Ollama:** Used to run the local LLM and embedding models.
* **codellama:7b:** An LLM fine-tuned for code generation. It excels at both conversational responses and producing high-quality code. Pull locally by running (`ollama pull codellama:7b`)
* **nomic-embed-text:latest:** A powerful, open-source embedding model that is specifically used to convert text into numerical vectors (embeddings). Pull locally by running `ollama pull nomic-embed-text:latest`
* **FAISS:** An efficient library for similarity search, used here as the vector store for the Mantine documentation.
* **Streamlit:** A Python-based framework for creating the simple, yet powerful, web user interface.

## Setup

1. **Set up virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Ingest Mantine documentation:**

   ```sh
   python ingestion.py
   ```

   This will download and index Mantine documentation into FAISS for retrieval.

4. **Run the chatbot app:**

   ```sh
   streamlit run app.py
   ```

   Open the provided local URL in your browser to interact with the chatbot.

## Project Structure

- `app.py` – Streamlit chat UI for Mantine Expert
- `core.py` – RAG chain setup and retrieval logic
- `ingestion.py` – Script to ingest Mantine documentation into FAISS
- `mantine_urls.py` – List of Mantine documentation URLs
- `constants.py` – Model and index configuration
- `faiss/` – Directory for FAISS vector index files

## Requirements

See [`requirements.txt`](requirements.txt) for all dependencies.

## How it works

Mantine Expert uses LangChain to retrieve relevant documentation chunks from Mantine's official site, then generates answers using an Ollama-powered LLM. If code is requested, it attempts to provide complete, runnable Mantine React examples.

## License

MIT