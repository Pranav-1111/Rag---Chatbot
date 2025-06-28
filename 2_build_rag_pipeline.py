from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

#Load FAISS vector store
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("index", embedding, allow_dangerous_deserialization=True)

#Load LLM
pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", max_new_tokens=256)
llm = HuggingFacePipeline(pipeline=pipe)

#Create RAG pipeline
retriever = vectorstore.as_retriever(search_type="similarity", k=2)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

#Test
query = "What is this document about?"
response = qa_chain.run(query)
print("💬", response)