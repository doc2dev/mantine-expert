# app.py
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from core import rag_chain

st.set_page_config(page_title="Mantine AI Assistant", page_icon="💡")
st.title("💡 Mantine AI Expert")
st.caption("A RAG-powered chatbot for the Mantine UI framework.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

# Get user input and invoke the RAG chain
if prompt := st.chat_input("Ask a question about Mantine..."):
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        response = rag_chain.invoke(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(AIMessage(content=response))