from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate

from constants import embedding_model, llm_model, index_filename

# Initialize Ollama model
llm = ChatOllama(model=llm_model)

# Load the vector store and create a retriever
embeddings = OllamaEmbeddings(model=embedding_model)
vectorstore = FAISS.load_local(index_filename, embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()


prompt_template = """
You are an expert AI assistant on the Mantine UI framework. 
Use the following retrieved context to answer the user's question. 
If you are asked to provide code, generate a complete and runnable Mantine code example in React. 
If the context does not contain the information to answer, say "I don't have enough information to answer that based on the Mantine documentation provided."

Context: {context}

Question: {question}

Answer:
"""

rag_prompt = PromptTemplate.from_template(prompt_template)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)
