#!/usr/bin/env python3
"""
AI Agent Demo: A Simple Task-Planning Agent

This demonstrates the core concepts of an AI agent:
- Perception: Reading user goals and environment
- Reasoning: Breaking down tasks into steps
- Action: Executing and tracking progress
"""

import json
import time
from datetime import datetime
from typing import List, Dict

class SimpleAIAgent:
    """A basic AI agent that demonstrates perception, reasoning, and action"""
    
    def __init__(self, name: str):
        self.name = name
        self.memory = []  # Agent's memory of actions taken
        self.task_knowledge = {
            "write_email": ["draft content", "review tone", "check recipients", "send"],
            "plan_meeting": ["check calendars", "find time slot", "book room", "send invites"],
            "research_topic": ["identify sources", "gather information", "analyze data", "summarize findings"],
            "create_report": ["outline structure", "collect data", "write content", "format document"]
        }
    
    def perceive(self, user_input: str) -> Dict:
        """PERCEPTION: Understanding the environment and user request"""
        print(f"🔍 {self.name} is perceiving the request...")
        
        # Simple keyword matching to understand the task
        task_type = None
        for task in self.task_knowledge.keys():
            if any(word in user_input.lower() for word in task.split('_')):
                task_type = task
                break
        
        environment = {
            "user_request": user_input,
            "task_type": task_type,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "complexity": len(user_input.split())  # Simple complexity measure
        }
        
        print(f"   Detected task type: {task_type or 'general'}")
        return environment
    
    def reason(self, environment: Dict) -> List[str]:
        """REASONING: Planning the steps to achieve the goal"""
        print(f"🧠 {self.name} is reasoning and planning...")
        
        task_type = environment['task_type']
        
        if task_type and task_type in self.task_knowledge:
            steps = self.task_knowledge[task_type]
        else:
            # Generic problem-solving approach
            steps = ["understand requirements", "research options", "create solution", "review results"]
        
        print(f"   Planned {len(steps)} steps to complete the task")
        return steps
    
    def act(self, steps: List[str], environment: Dict) -> Dict:
        """ACTION: Executing the planned steps"""
        print(f"🚀 {self.name} is taking action...")
        
        results = {
            "task": environment['user_request'],
            "steps_completed": [],
            "status": "in_progress",
            "start_time": environment['timestamp']
        }
        
        for i, step in enumerate(steps, 1):
            print(f"   Step {i}/{len(steps)}: {step.title()}...")
            time.sleep(0.5)  # Simulate work being done
            
            results['steps_completed'].append({
                "step": step,
                "status": "completed",
                "time": datetime.now().strftime("%H:%M:%S")
            })
            
            # Store in memory
            self.memory.append(f"Completed: {step}")
        
        results['status'] = "completed"
        results['end_time'] = datetime.now().strftime("%H:%M:%S")
        
        print(f"✅ Task completed successfully!")
        return results
    
    def process_request(self, user_input: str) -> Dict:
        """Main agent loop: Perceive -> Reason -> Act"""
        print(f"\n{'='*50}")
        print(f"AI Agent '{self.name}' Processing Request")
        print(f"{'='*50}")
        
        # Agent's core loop
        environment = self.perceive(user_input)
        planned_steps = self.reason(environment)
        results = self.act(planned_steps, environment)
        
        return results

def demonstrate_multi_agent_system():
    """Shows multiple agents working together"""
    print("\n" + "="*60)
    print("MULTI-AGENT SYSTEM DEMO")
    print("="*60)
    
    # Create specialized agents
    research_agent = SimpleAIAgent("ResearchBot")
    writing_agent = SimpleAIAgent("WriterBot")
    
    # Simulate collaboration
    task1_result = research_agent.process_request("research market trends for AI agents")
    task2_result = writing_agent.process_request("write email summary of research findings")
    
    print(f"\n📊 Collaboration Summary:")
    print(f"   - {research_agent.name}: {task1_result['status']}")
    print(f"   - {writing_agent.name}: {task2_result['status']}")

def main():
    print("🤖 AI Agent Demonstration")
    print("This demo shows how AI agents work: Perceive → Reason → Act")
    
    # Create an AI agent
    agent = SimpleAIAgent("TaskBot")
    
    # Demo different types of requests
    sample_requests = [
        "Please help me write an email to the team",
        "I need to plan a meeting for next week",
        "Create a report on our quarterly performance"
    ]
    
    for request in sample_requests:
        result = agent.process_request(request)
    
    # Show agent's memory
    print(f"\n🧠 Agent Memory ({len(agent.memory)} items):")
    for memory in agent.memory[-3:]:  # Show last 3 memories
        print(f"   - {memory}")
    
    # Demonstrate multi-agent collaboration
    demonstrate_multi_agent_system()
    
    print(f"\n" + "="*60)
    print("Demo complete! This shows the basic concepts of AI agents:")
    print("✓ Perception: Understanding requests and environment")
    print("✓ Reasoning: Planning steps to achieve goals")
    print("✓ Action: Executing plans and tracking progress")
    print("✓ Memory: Storing experiences for future use")
    print("✓ Collaboration: Multiple agents working together")

if __name__ == "__main__":
    main()