# Prompt Engineering: Techniques That Actually Work

A hands-on demo comparing 5 proven prompt engineering techniques using Claude. See the real difference each technique makes on identical or similar questions.

## What It Does

This project demonstrates and compares:

1. **Basic Prompting** - No engineering (baseline)
2. **Role-Based Prompting** - Assign expertise/persona
3. **Few-Shot Learning** - Provide examples first
4. **Chain-of-Thought** - Encourage step-by-step reasoning
5. **Structured Output** - Specify exact response format

## Installation

bash
# Clone or download this project
pip install -r requirements.txt


## Setup

Set your Anthropic API key:

bash
# Linux/Mac
export ANTHROPIC_API_KEY="your-api-key-here"

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your-api-key-here"


Get your API key at: https://console.anthropic.com/

## How to Run

bash
python main.py


## Expected Output


============================================================
PROMPT ENGINEERING TECHNIQUES COMPARISON
============================================================

────────────────────────────────────────────────────────────
1. BASIC (Baseline)
Question: What is Docker?
────────────────────────────────────────────────────────────
Docker is a platform for developing, shipping, and running 
applications in containers. Containers are lightweight, 
standalone packages that include everything needed to run 
software...

────────────────────────────────────────────────────────────
2. ROLE-BASED
Question: What is Docker?
────────────────────────────────────────────────────────────
Docker is containerization technology that packages apps with 
their dependencies. In production, use it for consistent 
deployments, microservices isolation, and CI/CD pipelines. 
Start with Docker Compose for local dev, graduate to 
Kubernetes for orchestration.

────────────────────────────────────────────────────────────
3. FEW-SHOT
Question: data = data
────────────────────────────────────────────────────────────
Self-assignment is redundant; remove or use meaningful 
transformation like 'data = process(data)'

────────────────────────────────────────────────────────────
4. CHAIN-OF-THOUGHT
Question: Should I use SQL or NoSQL for a chat app?
────────────────────────────────────────────────────────────
Let me think through this step-by-step:

1. Chat apps need fast writes for messages
2. Data structure: messages are relatively simple documents
3. Scale: potentially millions of messages
4. Queries: mostly recent messages by conversation
5. Relationships: users to conversations (simple)

Final answer: NoSQL (like MongoDB) - better for high-write 
workloads with simple document structures.

────────────────────────────────────────────────────────────
5. STRUCTURED OUTPUT
Question: Evaluate Python vs JavaScript for backend
────────────────────────────────────────────────────────────
{"summary": "Both are excellent; Python excels in data/ML, 
JS in real-time apps", "pros": ["Python: cleaner syntax, 
ML libraries", "JS: async performance, full-stack unity"], 
"cons": ["Python: slower runtime", "JS: callback complexity"], 
"recommendation": "Choose Python for data-heavy apps, JS for 
real-time features"}

============================================================
KEY TAKEAWAY: Match the technique to your use case!
============================================================


## When to Use Each Technique

| Technique | Best For |
|-----------|----------|
| Basic | Simple factual queries |
| Role-Based | Domain-specific expertise |
| Few-Shot | Consistent formatting, style matching |
| Chain-of-Thought | Complex reasoning, decisions |
| Structured Output | API responses, data extraction |

## Learn More

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
