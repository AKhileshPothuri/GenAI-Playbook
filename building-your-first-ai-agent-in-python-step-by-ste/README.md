# Building Your First AI Agent in Python 🤖

A simple, beginner-friendly AI agent that can use tools to answer questions. This project demonstrates the core concepts of AI agents: reasoning, tool selection, and action execution.

## What It Does

This agent can:
- 🕐 **Get the current time** - Uses a time tool
- 🧮 **Perform calculations** - Uses a calculator tool  
- 🔍 **Search for information** - Uses a knowledge search tool

The agent automatically decides which tool to use based on your question!

## How AI Agents Work


User Question → LLM Decides → Tool Execution → LLM Summarizes → Answer


Unlike simple chatbots, agents can:
1. **Reason** about what tools to use
2. **Execute** actions (tool calls)
3. **Adapt** based on results

## Installation

1. Clone or download this project

2. Install dependencies:
bash
pip install -r requirements.txt


3. Set your OpenAI API key:
bash
# On Mac/Linux
export OPENAI_API_KEY="your-api-key-here"

# On Windows
set OPENAI_API_KEY=your-api-key-here


Get your API key at: https://platform.openai.com/api-keys

## How to Run

bash
python main.py


## Expected Output


==================================================
🚀 Welcome to Your First AI Agent!
==================================================

🤖 Agent received: What time is it right now?
🔧 Using tool: get_current_time with args: {}
📊 Tool result: 2024-01-15 14:32:45

💬 Final Answer: The current time is 2:32 PM on January 15th, 2024.

--------------------------------------------------

🤖 Agent received: Calculate 25 * 4 + 10
🔧 Using tool: calculator with args: {'expression': '25 * 4 + 10'}
📊 Tool result: Result: 110

💬 Final Answer: The result of 25 × 4 + 10 is 110.

--------------------------------------------------

🤖 Agent received: What is an AI agent?
🔧 Using tool: search_knowledge with args: {'query': 'AI agent'}
📊 Tool result: An AI agent is a program that uses LLMs to autonomously perform tasks through reasoning and tool use.

💬 Final Answer: An AI agent is a program that uses Large Language Models (LLMs) to autonomously perform tasks. They work by reasoning about problems and using tools to take actions and gather information.

--------------------------------------------------


## Project Structure


├── main.py           # The agent code (under 80 lines!)
├── requirements.txt  # Python dependencies
└── README.md         # This file


## Key Concepts Explained

### Tools
Tools are functions the agent can call. We define them with:
- A **name** the LLM can reference
- A **description** so the LLM knows when to use it
- **Parameters** the tool accepts

### The Agent Loop
1. User sends a question
2. LLM receives question + available tools
3. LLM decides to use a tool (or answer directly)
4. We execute the tool and return results
5. LLM generates final answer using tool results

## Next Steps

Once you understand this basic agent, try:
- Adding new tools (weather API, web search, database queries)
- Implementing memory (conversation history)
- Chaining multiple tool calls
- Exploring frameworks like LangChain or CrewAI

## Troubleshooting

**"No API key found"**: Make sure you've set the `OPENAI_API_KEY` environment variable

**"Rate limit exceeded"**: Wait a minute and try again, or check your OpenAI usage limits

**"Module not found"**: Run `pip install -r requirements.txt` again

## License

MIT - Feel free to use this code in your own projects!
