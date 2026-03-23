#!/usr/bin/env python3
"""
Personal AI Agent: Your Digital Life Assistant

A starter implementation showing how AI agents can autonomously
handle tasks like scheduling, web research, and task management.
"""

import os
from datetime import datetime
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Agent's available tools/capabilities
TOOLS = {
    "check_calendar": lambda date: f"Calendar for {date}: Meeting at 2pm, Gym at 6pm",
    "add_reminder": lambda task: f"✓ Reminder set: '{task}'",
    "search_web": lambda query: f"Top result for '{query}': Latest AI news from TechCrunch",
    "send_message": lambda msg: f"✓ Message queued: '{msg[:30]}...'",
    "get_weather": lambda loc: f"Weather in {loc}: 72°F, Sunny",
}

def agent_decide(user_request: str, context: list) -> dict:
    """Agent analyzes request and decides which tool to use."""
    system_prompt = """You are a Personal AI Agent. Analyze the user's request and respond with:
1. TOOL: one of [check_calendar, add_reminder, search_web, send_message, get_weather, none]
2. PARAM: the parameter to pass to the tool
3. RESPONSE: a friendly response to the user

Format your response exactly as:
TOOL: <tool_name>
PARAM: <parameter>
RESPONSE: <your friendly response>"""
    
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(context)
    messages.append({"role": "user", "content": user_request})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=200
    )
    
    # Parse agent's decision
    text = response.choices[0].message.content
    result = {"tool": "none", "param": "", "response": text}
    
    for line in text.split("\n"):
        if line.startswith("TOOL:"):
            result["tool"] = line.replace("TOOL:", "").strip().lower()
        elif line.startswith("PARAM:"):
            result["param"] = line.replace("PARAM:", "").strip()
        elif line.startswith("RESPONSE:"):
            result["response"] = line.replace("RESPONSE:", "").strip()
    
    return result

def run_agent():
    """Main agent loop - maintains context and handles user requests."""
    print("\n🤖 Personal AI Agent Initialized")
    print(f"   Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("   Type 'quit' to exit\n")
    
    context = []  # Agent maintains conversation history
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            print("\n👋 Agent shutting down. Goodbye!")
            break
        
        # Agent decides what to do
        decision = agent_decide(user_input, context)
        
        # Execute tool if needed
        tool_result = ""
        if decision["tool"] in TOOLS:
            tool_result = TOOLS[decision["tool"]](decision["param"])
            print(f"   [Agent Action: {tool_result}]")
        
        print(f"Agent: {decision['response']}\n")
        
        # Update context for persistent memory
        context.append({"role": "user", "content": user_input})
        context.append({"role": "assistant", "content": decision["response"]})
        context = context[-10:]  # Keep last 10 messages

if __name__ == "__main__":
    run_agent()
