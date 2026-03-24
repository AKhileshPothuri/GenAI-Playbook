#!/usr/bin/env python3
"""
Personal AI Agent: A starter example demonstrating autonomous task execution.
This agent can manage your digital life by planning and executing multi-step tasks.
"""

import os
from datetime import datetime
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the tools/capabilities our personal agent has access to
AGENT_TOOLS = {
    "check_calendar": lambda: f"📅 Today's events: Team standup at 10am, Lunch with Sarah at 12pm",
    "check_weather": lambda: f"🌤️ Weather: 72°F, partly cloudy, 10% chance of rain",
    "check_emails": lambda: f"📧 3 unread emails: 1 urgent from boss, 2 newsletters",
    "check_tasks": lambda: f"✅ Pending tasks: Review PR #42, Submit expense report, Call mom",
    "get_time": lambda: f"🕐 Current time: {datetime.now().strftime('%I:%M %p')}",
}

def execute_tool(tool_name: str) -> str:
    """Execute a tool and return its result."""
    if tool_name in AGENT_TOOLS:
        return AGENT_TOOLS[tool_name]()
    return f"❌ Unknown tool: {tool_name}"

def run_personal_agent(user_request: str) -> str:
    """Run the personal AI agent to handle a user request."""
    
    # System prompt defining our agent's personality and capabilities
    system_prompt = f"""You are a helpful personal AI agent managing the user's digital life.
    
Available tools: {', '.join(AGENT_TOOLS.keys())}

When responding:
1. First, identify which tools you need (prefix with TOOL:)
2. Then provide a helpful summary based on the information gathered
3. Suggest proactive next actions

Format tool calls as: TOOL: tool_name"""

    # Get the agent's plan
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_request}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    agent_plan = response.choices[0].message.content
    print("\n🤖 Agent Planning...\n")
    
    # Execute any tools the agent requested
    tool_results = []
    for line in agent_plan.split('\n'):
        if line.strip().startswith('TOOL:'):
            tool_name = line.replace('TOOL:', '').strip()
            result = execute_tool(tool_name)
            tool_results.append(result)
            print(f"  Executing: {tool_name}")
    
    # If tools were executed, get a final summary
    if tool_results:
        context = "\n".join(tool_results)
        final_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize this information helpfully and suggest next actions:"},
                {"role": "user", "content": f"User asked: {user_request}\n\nGathered info:\n{context}"}
            ],
            temperature=0.7
        )
        return f"\n📊 Tool Results:\n{context}\n\n💬 Agent Summary:\n{final_response.choices[0].message.content}"
    
    return agent_plan

if __name__ == "__main__":
    print("="*60)
    print("🏠 Personal AI Agent - Your Digital Life Interface")
    print("="*60)
    
    # Example: Morning briefing request
    request = "Give me my morning briefing - what do I need to know today?"
    print(f"\n👤 You: {request}")
    
    result = run_personal_agent(request)
    print(result)
