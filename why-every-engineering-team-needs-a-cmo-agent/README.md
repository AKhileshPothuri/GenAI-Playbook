# CMO Agent: AI Marketing Intelligence for Engineering Teams

A lightweight AI agent that acts as a Chief Marketing Officer for engineering teams. It analyzes your product and provides positioning, messaging, competitive analysis, and go-to-market advice.

## Why This Matters

Engineering teams often build technically excellent products but struggle with:
- **Positioning**: How do we describe what we built?
- **Messaging**: How do we translate features into benefits?
- **Go-to-market**: How do we reach users without a marketing budget?

This CMO Agent bridges that gap using AI.

## Installation

bash
# Clone or download this project
pip install -r requirements.txt


## Setup

Set your OpenAI API key as an environment variable:

bash
# Linux/Mac
export OPENAI_API_KEY="your-api-key-here"

# Windows
set OPENAI_API_KEY=your-api-key-here


## How to Run

bash
python main.py


## Expected Output


==================================================
🤖 CMO AGENT - Marketing Intelligence for Engineers
==================================================

Product being analyzed:
    FastCache: An open-source, Redis-compatible in-memory cache written in Rust...

🎯 CMO Agent analyzing your product...

==================================================

📊 Analyzing: Positioning...

**Positioning Statement:** FastCache is the blazing-fast, zero-config 
in-memory cache for teams who need Redis compatibility without the overhead.

**Target Audience:**
- Backend engineers at startups scaling their infrastructure
- DevOps teams seeking simpler deployment options
- Rust enthusiasts looking for production-ready tools
--------------------------------------------------

📊 Analyzing: Messaging...

**Key Messages:**
1. "Deploy in seconds, not hours" - Single binary means no dependency hell
2. "2x faster where it matters" - Optimized for the small payloads that make up 80% of cache operations
3. "Redis compatible, Rust reliable" - Use your existing code with memory-safe infrastructure
--------------------------------------------------

📊 Analyzing: Competitive...

**Competitors:**
- Redis (incumbent, feature-rich but complex)
- Dragonfly (also claims speed improvements)

**Key Differentiator:** Single-binary deployment with built-in clustering - no ops team required
--------------------------------------------------

📊 Analyzing: Gtm Advice...

**Go-to-Market Tactics:**
1. Write a "Redis to FastCache in 5 minutes" migration guide on dev.to
2. Post benchmarks on r/rust and Hacker News (engineers love data)
3. Create a GitHub Action for easy CI/CD integration - drive adoption through DX
--------------------------------------------------

✅ CMO Analysis Complete!

💡 Tip: Replace 'sample_product' with your own product description.


## Customization

Edit the `sample_product` variable in `main.py` to analyze your own product:

python
sample_product = """
Your product name and description here.
Include: key features, technical details, target use case.
"""


## How It Works

1. **System Prompt**: Defines the CMO agent's expertise and communication style
2. **Task Loop**: Runs 4 marketing analyses (positioning, messaging, competitive, GTM)
3. **Output**: Actionable marketing insights formatted for engineers

## License

MIT - Use this in your own projects!
