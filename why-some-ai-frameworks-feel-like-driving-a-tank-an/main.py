#!/usr/bin/env python3
"""
Why Some AI Frameworks Feel Like Driving a Tank
================================================
This demo compares building the SAME simple task using:
1. "Tank Mode" - Heavy framework simulation (verbose, over-engineered)
2. "Sports Car Mode" - Lightweight, direct approach

The task: Summarize a piece of text and extract key points.
Spoiler: You don't always need a tank.
"""

import os
import time
from openai import OpenAI

# Initialize client (works with OpenAI or compatible APIs)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))

SAMPLE_TEXT = """
Artificial intelligence frameworks have exploded in popularity. MetaGPT offers
multi-agent software development. AutoGen enables conversational AI patterns.
CrewAI provides role-based agent teams. Meanwhile, OpenAI's agents-python keeps
things minimal. The question isn't which is 'best' - it's which fits YOUR task.
"""

# ============ TANK MODE: Over-engineered approach ============
class AgentConfig:
    """Configuration class (because tanks need manuals)"""
    def __init__(self, name, role, goal, backstory):
        self.name, self.role, self.goal, self.backstory = name, role, goal, backstory

class TaskPipeline:
    """Pipeline orchestrator (tanks have complex systems)"""
    def __init__(self, agents, tasks, verbose=True):
        self.agents, self.tasks, self.verbose = agents, tasks, verbose
        self.results = []
    
    def execute(self, text):
        for i, (agent, task) in enumerate(zip(self.agents, self.tasks)):
            if self.verbose:
                print(f"  [Pipeline] Stage {i+1}: {agent.name} executing '{task}'...")
            # All this ceremony... for one API call
            self.results.append(f"Result from {agent.name}")
        return self.results

def tank_mode(text):
    """The heavy framework experience - lots of setup, same result"""
    print("\n🚜 TANK MODE: Heavy Framework Simulation")
    print("="*50)
    start = time.time()
    
    # Step 1: Define agents with backstories (really?)
    summarizer = AgentConfig("SummarizerAgent", "Senior Analyst", 
        "Create summaries", "20 years of summarizing experience...")
    extractor = AgentConfig("ExtractorAgent", "Key Point Specialist",
        "Extract insights", "PhD in extraction sciences...")
    
    # Step 2: Create pipeline
    pipeline = TaskPipeline([summarizer, extractor], ["summarize", "extract"])
    pipeline.execute(text)
    
    # Step 3: Finally, make the actual API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize and extract 3 key points:\n{text}"}]
    )
    
    elapsed = time.time() - start
    print(f"  [Setup overhead: All that config for one API call]")
    print(f"  Time: {elapsed:.2f}s | Lines of setup: ~25")
    return response.choices[0].message.content

# ============ SPORTS CAR MODE: Just drive ============
def sports_car_mode(text):
    """The lightweight approach - direct and effective"""
    print("\n🏎️  SPORTS CAR MODE: Lightweight Approach")
    print("="*50)
    start = time.time()
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize and extract 3 key points:\n{text}"}]
    )
    
    elapsed = time.time() - start
    print(f"  [No ceremony, just results]")
    print(f"  Time: {elapsed:.2f}s | Lines of code: ~8")
    return response.choices[0].message.content

# ============ DECISION HELPER ============
def print_decision_guide():
    print("\n" + "="*50)
    print("🎯 WHEN TO CHOOSE WHAT")
    print("="*50)
    print("""
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
    """)

if __name__ == "__main__":
    print("\n" + "🤖 AI FRAMEWORK WEIGHT CLASS COMPARISON".center(50))
    
    # Run both approaches
    result1 = tank_mode(SAMPLE_TEXT)
    print(f"\n  Result: {result1[:100]}...")
    
    result2 = sports_car_mode(SAMPLE_TEXT)
    print(f"\n  Result: {result2[:100]}...")
    
    print_decision_guide()
    print("\n💡 Both produce the SAME result. Choose complexity wisely!\n")
