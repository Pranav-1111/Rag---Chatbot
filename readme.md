🧠 GenAI-Powered RAG Chatbot using LangChain 🚀
This project is a Retrieval-Augmented Generation (RAG) based Q&A chatbot that can answer questions from a custom PDF document using open-source LLMs. Built using LangChain, Hugging Face, and FAISS for vector search.

📌 Features
Load and parse PDF using LangChain loaders

Chunk and embed text using Hugging Face Transformers

Store embeddings in FAISS vector DB for fast retrieval

Query system using similarity search + LLM generation

Built-in web UI using Streamlit

🔧 Tech Stack
Tool	Purpose
Python	Programming language
LangChain	RAG pipeline & orchestration
HuggingFace	Embeddings & models
FAISS	Vector store for semantic search
Streamlit	Frontend UI for interacting with bot
PyMuPDF	PDF text extraction

🗂️ Folder Structure :
📁 Q&A Chatbot/
│
├── 1_ingest_data.py        # Load + chunk + embed + save to FAISS
├── 2_chat_with_bot.py      # Query and respond using LangChain
├── data/                   # Folder containing PDF files
├── faiss_index/            # Saved vectorstore DB
├── chatbot_ui.py           # Streamlit-based chatbot interface
├── requirements.txt
└── README.md
🧪 Demo
Ask questions like:

"What is Pranav Bhatt's internship experience?"

"Where did he study BSc IT?"

"What technical skills does he have?"

⏩ Response will come from the PDF content you loaded.

🚀 Getting Started
Clone the repository:
git clone https://github.com/Pranav-1111/rag-chatbot
cd rag-chatbot

Install dependencies:
pip install -r requirements.txt
Put your document (e.g., resume.pdf) inside the /data folder.

Ingest the data:
python 1_ingest_data.py
Run the chatbot:

streamlit run chatbot_ui.py
📄 PDF Used
You can replace the default PDF file (e.g., bhatt_pranav.pdf) in the /data folder with any document you want to use as a knowledge base.

🌟 Highlights
Built from scratch using open-source stack

Fully local deployment with no paid APIs

Ready-to-demo for interviews or clients

Fine-grained control over chunking, embedding, retrieval, and generation

🔗 Links
🔗 LangChain Docs

🔗 Hugging Face Transformers

🔗 FAISS Vector DB

Built with ❤️ by Pranav Bhatt

🔗 GitHub: https://github.com/Pranav-1111
🔗 LinkedIn: https://linkedin.com/in/pranavbhatt

🤝 Contributing
Pull requests are welcome! If you find a bug or want to improve something, open an issue first.

📜 License
MIT License © 2025 Pranav Bhatt