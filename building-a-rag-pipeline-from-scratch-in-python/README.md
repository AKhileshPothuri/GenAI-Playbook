# Building a RAG Pipeline from Scratch in Python

A minimal, beginner-friendly implementation of Retrieval Augmented Generation (RAG) that demonstrates the three core components: document processing, vector storage, and LLM generation.

## What This Does

This project builds a complete RAG pipeline that:
1. **Loads** a text file as a knowledge base
2. **Chunks** the text into smaller pieces for better retrieval
3. **Embeds** the chunks using a free, local model (no API key needed for embeddings!)
4. **Stores** embeddings in ChromaDB (runs locally)
5. **Retrieves** relevant chunks based on semantic similarity
6. **Generates** answers using GPT-3.5-turbo with the retrieved context

## Installation

bash
# Clone or download the project files

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# On Windows:
set OPENAI_API_KEY=your-api-key-here


## How to Run

bash
python main.py


## Expected Output


📄 Step 1: Loading and processing documents...
   Created 3 chunks from the knowledge base
🔢 Step 2: Creating embeddings and vector store...
   Vector store ready!
🤖 Step 3: Setting up the RAG chain...
   RAG pipeline ready!

==================================================
🎯 RAG Pipeline Demo
==================================================

❓ Question: What is Python used for?
💡 Answer: Python is widely used for web development, data science, artificial intelligence, machine learning, automation, and scientific computing.

❓ Question: Who created Python and when?
💡 Answer: Python was created by Guido van Rossum and was first released in 1991.

❓ Question: What is the capital of France?
💡 Answer: I don't have enough information.

==================================================
✅ RAG pipeline demonstration complete!


## Key Concepts Demonstrated

| Component | Tool Used | Purpose |
|-----------|-----------|--------|
| Document Loader | LangChain TextLoader | Load text files |
| Text Splitter | RecursiveCharacterTextSplitter | Chunk documents |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) | Convert text to vectors |
| Vector Store | ChromaDB | Store and search vectors |
| LLM | OpenAI GPT-3.5-turbo | Generate answers |

## Customization Ideas

- Replace `knowledge_base.txt` with your own documents
- Try different chunk sizes (smaller = more precise, larger = more context)
- Swap GPT-3.5 for GPT-4 or Claude for better answers
- Add PDF support with `PyPDFLoader`
- Persist the vector store to disk for faster restarts

## Requirements

- Python 3.8+
- OpenAI API key (get one at https://platform.openai.com)
- ~500MB disk space for the embedding model (downloaded automatically)
