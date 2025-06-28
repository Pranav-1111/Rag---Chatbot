from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

#Load documents
loader = PyPDFLoader("data/bhatt pranav.pdf")
documents = loader.load()

#Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

#Embed using Sentence Transformers
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#Create FAISS vector store
vectorstore = FAISS.from_documents(chunks, embedding)

#Save to disk
vectorstore.save_local("index")
print("✅ FAISS index created and saved!")