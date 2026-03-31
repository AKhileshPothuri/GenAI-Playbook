"""Building Your First AI Agent in Python - Step by Step

This agent can perform simple tasks by using tools to:
1. Get the current time
2. Perform calculations
3. Search for information (simulated)

The agent decides which tool to use based on your question.
"""

import os
import json
from datetime import datetime
from openai import OpenAI

# Step 1: Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 2: Define the tools our agent can use
TOOLS = [
    {"type": "function", "function": {"name": "get_current_time", "description": "Get the current date and time", "parameters": {"type": "object", "properties": {}, "required": []}}},
    {"type": "function", "function": {"name": "calculator", "description": "Perform basic math calculations", "parameters": {"type": "object", "properties": {"expression": {"type": "string", "description": "Math expression to evaluate, e.g. '2 + 2'"}}, "required": ["expression"]}}},
    {"type": "function", "function": {"name": "search_knowledge", "description": "Search for information about a topic", "parameters": {"type": "object", "properties": {"query": {"type": "string", "description": "The search query"}}, "required": ["query"]}}}
]

# Step 3: Implement the actual tool functions
def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

def search_knowledge(query: str) -> str:
    # Simulated knowledge base - in production, connect to a real API
    knowledge = {"python": "Python is a high-level programming language created by Guido van Rossum in 1991.", "ai agent": "An AI agent is a program that uses LLMs to autonomously perform tasks through reasoning and tool use."}
    for key, value in knowledge.items():
        if key in query.lower():
            return value
    return f"No specific information found for '{query}'. Try asking about Python or AI agents."

# Step 4: Map tool names to functions
TOOL_FUNCTIONS = {"get_current_time": get_current_time, "calculator": calculator, "search_knowledge": search_knowledge}

# Step 5: The main agent loop
def run_agent(user_input: str) -> str:
    print(f"\n🤖 Agent received: {user_input}")
    messages = [{"role": "system", "content": "You are a helpful AI agent. Use the available tools to answer questions. Always explain what you're doing."}, {"role": "user", "content": user_input}]
    
    # First call: Let the LLM decide what to do
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, tools=TOOLS, tool_choice="auto")
    assistant_message = response.choices[0].message
    
    # Check if the agent wants to use a tool
    if assistant_message.tool_calls:
        messages.append(assistant_message)
        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments) if tool_call.function.arguments else {}
            print(f"🔧 Using tool: {tool_name} with args: {tool_args}")
            result = TOOL_FUNCTIONS[tool_name](**tool_args)
            print(f"📊 Tool result: {result}")
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": result})
        
        # Second call: Generate final response with tool results
        final_response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        return final_response.choices[0].message.content
    return assistant_message.content

# Step 6: Run the agent with example queries
if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Welcome to Your First AI Agent!")
    print("=" * 50)
    
    test_queries = ["What time is it right now?", "Calculate 25 * 4 + 10", "What is an AI agent?"]
    for query in test_queries:
        result = run_agent(query)
        print(f"\n💬 Final Answer: {result}\n")
        print("-" * 50)
