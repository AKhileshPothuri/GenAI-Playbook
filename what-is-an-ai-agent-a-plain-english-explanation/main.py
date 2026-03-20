#!/usr/bin/env python3
"""
AI Agent Demo: A Simple Goal-Oriented Agent
This demonstrates core AI agent concepts through a practical example.
"""

import random
import time
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Environment:
    """Simulates a simple task environment with obstacles and goals"""
    obstacles: List[str]
    available_tools: List[str]
    goal_status: Dict[str, bool]
    
class SimpleAIAgent:
    """A basic AI agent that perceives, decides, and acts autonomously"""
    
    def __init__(self, name: str, goal: str):
        self.name = name
        self.goal = goal
        self.memory = []  # Agent's experience memory
        self.actions_taken = []
        
    def perceive(self, environment: Environment) -> Dict[str, Any]:
        """PERCEPTION: Agent observes its environment"""
        perception = {
            'obstacles_detected': environment.obstacles,
            'tools_available': environment.available_tools,
            'goal_progress': environment.goal_status
        }
        self.memory.append(f"Perceived: {perception}")
        return perception
    
    def decide(self, perception: Dict[str, Any]) -> str:
        """DECISION-MAKING: Agent chooses best action based on observations"""
        # Simple decision logic (in real agents, this would be much more sophisticated)
        if perception['obstacles_detected']:
            action = f"analyze_obstacle_{random.choice(perception['obstacles_detected'])}"
        elif perception['tools_available']:
            action = f"use_tool_{random.choice(perception['tools_available'])}"
        else:
            action = "explore_environment"
            
        print(f"🧠 {self.name} decides: {action}")
        return action
    
    def act(self, action: str, environment: Environment) -> bool:
        """ACTION: Agent executes chosen action and modifies environment"""
        print(f"🤖 {self.name} executes: {action}")
        self.actions_taken.append(action)
        
        # Simulate action effects
        if "analyze_obstacle" in action:
            obstacle = action.split("_")[-1]
            if obstacle in environment.obstacles:
                environment.obstacles.remove(obstacle)
                environment.available_tools.append(f"solution_for_{obstacle}")
                print(f"✅ Obstacle '{obstacle}' analyzed and solution found!")
                
        elif "use_tool" in action:
            tool = action.split("_")[-1]
            if tool in environment.available_tools:
                environment.goal_status[self.goal] = True
                print(f"🎯 Goal '{self.goal}' achieved using {tool}!")
                return True
                
        return False
    
    def is_goal_achieved(self, environment: Environment) -> bool:
        """Check if agent has achieved its goal"""
        return environment.goal_status.get(self.goal, False)

def demonstrate_agent_behavior():
    """Main demonstration of AI agent concepts"""
    print("🚀 AI Agent Demo: Understanding Autonomous Behavior\n")
    
    # Create environment with challenges
    env = Environment(
        obstacles=["data_inconsistency", "network_timeout", "authentication_error"],
        available_tools=["debugger", "retry_mechanism"],
        goal_status={}
    )
    
    # Create an AI agent with a specific goal
    agent = SimpleAIAgent("DataProcessorAgent", "process_customer_data")
    
    print(f"🎯 Agent Goal: {agent.goal}")
    print(f"🌍 Environment: {len(env.obstacles)} obstacles, {len(env.available_tools)} tools\n")
    
    # Agent operates autonomously until goal is achieved
    step = 1
    max_steps = 10
    
    while not agent.is_goal_achieved(env) and step <= max_steps:
        print(f"--- Step {step} ---")
        
        # 1. PERCEIVE: Agent observes environment
        perception = agent.perceive(env)
        
        # 2. DECIDE: Agent chooses action based on observations
        action = agent.decide(perception)
        
        # 3. ACT: Agent executes action and potentially achieves goal
        goal_achieved = agent.act(action, env)
        
        if goal_achieved:
            break
            
        step += 1
        time.sleep(1)  # Pause for readability
        print()
    
    # Summary
    print("\n" + "="*50)
    if agent.is_goal_achieved(env):
        print(f"✅ SUCCESS: {agent.name} achieved its goal in {step} steps!")
    else:
        print(f"❌ Agent reached maximum steps without achieving goal")
        
    print(f"\n📊 Agent took {len(agent.actions_taken)} actions:")
    for i, action in enumerate(agent.actions_taken, 1):
        print(f"   {i}. {action}")

if __name__ == "__main__":
    demonstrate_agent_behavior()