from constants import embedding_model, index_filename
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

from mantine_urls import mantine_urls

# Add the parent directory to sys.path

# List of Mantine documentation URLs to ingest
urls = mantine_urls

# Load and split documents
loader = WebBaseLoader(urls)
print("DOCUMENT LOAD STARTING")
docs = loader.load()
print("DOCUMENT LOAD FINISHED")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print("DOCUMENT SPLIT FINISHED")

# Create and save the vector store
embeddings = OllamaEmbeddings(model=embedding_model)
print("CREATING VECTOR STORE")
vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
print("Saving VECTOR STORE")
vectorstore.save_local(index_filename)
