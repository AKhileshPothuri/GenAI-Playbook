# Why Some AI Frameworks Feel Like Driving a Tank 🚜

A hands-on demonstration comparing "heavy" vs "lightweight" approaches to the same AI task.

## What This Does

This project illustrates the overhead difference between:
- **Tank Mode**: Simulates heavy framework patterns (agents, configs, pipelines)
- **Sports Car Mode**: Direct API calls with minimal abstraction

Both accomplish the **exact same task**: summarizing text and extracting key points.

## Install Steps

bash
# 1. Clone or download this project
# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"


## How to Run

bash
python main.py


## Expected Output


        🤖 AI FRAMEWORK WEIGHT CLASS COMPARISON        

🚜 TANK MODE: Heavy Framework Simulation
==================================================
  [Pipeline] Stage 1: SummarizerAgent executing 'summarize'...
  [Pipeline] Stage 2: ExtractorAgent executing 'extract'...
  [Setup overhead: All that config for one API call]
  Time: 1.23s | Lines of setup: ~25

  Result: AI frameworks vary in complexity. The key is matching the tool to the task...

🏎️  SPORTS CAR MODE: Lightweight Approach
==================================================
  [No ceremony, just results]
  Time: 1.18s | Lines of code: ~8

  Result: AI frameworks vary in complexity. The key is matching the tool to the task...

==================================================
🎯 WHEN TO CHOOSE WHAT
==================================================

    USE A TANK (Heavy Framework) WHEN:
    ✓ Multiple agents need to collaborate
    ✓ Complex state management required
    ✓ You need built-in memory/tool systems
    ✓ Production system with many workflows
    
    USE A SPORTS CAR (Lightweight) WHEN:
    ✓ Single task or simple chain
    ✓ Prototyping or learning
    ✓ You value understanding your code
    ✓ Latency and simplicity matter

💡 Both produce the SAME result. Choose complexity wisely!


## Key Takeaway

The "tank" approach adds ~25 lines of boilerplate for the same result. Heavy frameworks shine when you **actually need** multi-agent coordination, persistent memory, or complex tool orchestration. For simple tasks, they're just overhead.

## Framework Reference

| Framework | Stars | Best For |
|-----------|-------|----------|
| MetaGPT | 65.8k | Multi-agent software dev |
| AutoGen | 56k | Conversational patterns |
| CrewAI | 46.8k | Role-based agent teams |
| OpenAI agents-python | 20.2k | Simple, direct workflows |

Choose your vehicle based on the journey, not the hype! 🎯
