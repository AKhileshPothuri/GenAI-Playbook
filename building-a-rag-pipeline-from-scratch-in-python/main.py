#!/usr/bin/env python3
"""
Building a RAG Pipeline from Scratch in Python

This minimal implementation demonstrates the three core components of RAG:
1. Document Processing - Chunk and prepare text for embedding
2. Vector Store - Store and retrieve documents by semantic similarity
3. Generation - Use retrieved context to answer questions with an LLM
"""

import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Step 1: Load and process documents
print("📄 Step 1: Loading and processing documents...")
loader = TextLoader("knowledge_base.txt")
documents = loader.load()

# Split documents into chunks for better retrieval
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Each chunk ~500 characters
    chunk_overlap=50     # Overlap to maintain context between chunks
)
chunks = text_splitter.split_documents(documents)
print(f"   Created {len(chunks)} chunks from the knowledge base")

# Step 2: Create embeddings and vector store
print("🔢 Step 2: Creating embeddings and vector store...")
# Using free, local embeddings (no API key needed!)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store chunks in ChromaDB (runs locally, no setup needed)
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  # Retrieve top 3 chunks
print("   Vector store ready!")

# Step 3: Set up the LLM and RAG chain
print("🤖 Step 3: Setting up the RAG chain...")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# The RAG prompt template - instructs the LLM to use retrieved context
RAG_PROMPT = ChatPromptTemplate.from_template("""
Answer the question based only on the following context. If you cannot
answer from the context, say "I don't have enough information."

Context:
{context}

Question: {question}

Answer:
""")

# Helper to format retrieved documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Build the RAG chain: retrieve -> format -> prompt -> generate -> parse
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | RAG_PROMPT
    | llm
    | StrOutputParser()
)
print("   RAG pipeline ready!\n")

# Step 4: Ask questions!
print("=" * 50)
print("🎯 RAG Pipeline Demo")
print("=" * 50)

questions = [
    "What is Python used for?",
    "Who created Python and when?",
    "What is the capital of France?"  # Not in our knowledge base!
]

for question in questions:
    print(f"\n❓ Question: {question}")
    answer = rag_chain.invoke(question)
    print(f"💡 Answer: {answer}")

print("\n" + "=" * 50)
print("✅ RAG pipeline demonstration complete!")
