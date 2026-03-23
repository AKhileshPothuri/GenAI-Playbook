# Personal AI Agent: Your Digital Life Assistant

A starter implementation demonstrating how Personal AI Agents can serve as the next interface for your digital life. This agent can autonomously decide which tools to use based on natural language requests.

## What It Does

This project showcases a **Personal AI Agent** that:
- 🧠 **Understands context** - Maintains conversation history for coherent interactions
- 🛠️ **Uses tools autonomously** - Decides which capability to invoke based on your request
- 📅 **Manages your digital life** - Calendar, reminders, web search, messaging, weather

## Features

| Tool | Description |
|------|-------------|
| `check_calendar` | View your schedule for any date |
| `add_reminder` | Set reminders for tasks |
| `search_web` | Search for information online |
| `send_message` | Queue messages to send |
| `get_weather` | Check weather for any location |

## Installation

bash
# 1. Clone or download this project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# Windows:
set OPENAI_API_KEY=your-api-key-here


## How to Run

bash
python main.py


## Expected Output


🤖 Personal AI Agent Initialized
   Date: 2024-01-15 10:30
   Type 'quit' to exit

You: What's on my calendar today?
   [Agent Action: Calendar for today: Meeting at 2pm, Gym at 6pm]
Agent: You have two things scheduled today - a meeting at 2pm and gym at 6pm!

You: Remind me to call mom this evening
   [Agent Action: ✓ Reminder set: 'call mom this evening']
Agent: I've set a reminder for you to call mom this evening. Family time is important!

You: What's the weather in San Francisco?
   [Agent Action: Weather in San Francisco: 72°F, Sunny]
Agent: It's a beautiful day in San Francisco - 72°F and sunny. Perfect weather!

You: Search for the latest AI news
   [Agent Action: Top result for 'latest AI news': Latest AI news from TechCrunch]
Agent: I found some recent AI news from TechCrunch for you. Want me to summarize it?

You: quit

👋 Agent shutting down. Goodbye!


## Key Concepts Demonstrated

1. **Agent Architecture**: The agent follows a Perceive → Decide → Act loop
2. **Tool Selection**: LLM autonomously chooses which tool fits the user's intent
3. **Persistent Context**: Conversation history enables coherent multi-turn interactions
4. **Extensibility**: Easy to add new tools by extending the `TOOLS` dictionary

## Extending the Agent

Add new capabilities by extending the `TOOLS` dictionary:

python
TOOLS["control_lights"] = lambda room: f"Lights in {room} toggled"
TOOLS["play_music"] = lambda song: f"Now playing: {song}"


## Learn More

This starter code accompanies the Medium article: **"Personal AI Agents: The Next Interface for Your Digital Life"**

---

*Built with OpenAI GPT-3.5 • Ready to expand into a full personal assistant*
