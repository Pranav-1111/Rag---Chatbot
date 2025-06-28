import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

st.set_page_config(page_title="📚 GenAI RAG Chatbot")

st.title("📚 Ask Me Anything (RAG + LangChain)")

#Load FAISS & model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("index", embedding, allow_dangerous_deserialization=True)

pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", max_new_tokens=256)
llm = HuggingFacePipeline(pipeline=pipe)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

query = st.text_input("🔍 Ask a question from your document:")

if query:
    result = qa_chain.run(query)
st.markdown("### 📖 Answer:")
st.write(result)