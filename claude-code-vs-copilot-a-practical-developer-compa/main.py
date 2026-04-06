#!/usr/bin/env python3
"""
Claude Code vs. Copilot: A Practical Developer Comparison

This tool simulates typical coding tasks and compares how each AI assistant
would handle them, helping developers understand the key differences.
"""

from dataclasses import dataclass
from typing import List
import json

@dataclass
class CodingTask:
    """Represents a typical developer task for comparison"""
    name: str
    description: str
    claude_code_approach: str
    copilot_approach: str
    winner: str
    reasoning: str

# Define real-world coding scenarios for comparison
TASKS: List[CodingTask] = [
    CodingTask(
        name="Multi-file Refactoring",
        description="Rename a function across 15 files and update all imports",
        claude_code_approach="Terminal agent scans codebase, identifies all usages, executes changes autonomously",
        copilot_approach="Requires manual file-by-file editing with inline suggestions",
        winner="Claude Code",
        reasoning="Agentic workflow handles multi-file operations natively"
    ),
    CodingTask(
        name="Inline Code Completion",
        description="Auto-complete a function while typing in VS Code",
        claude_code_approach="Requires switching to terminal, describing what you want",
        copilot_approach="Real-time ghost text appears as you type, Tab to accept",
        winner="Copilot",
        reasoning="Deep IDE integration provides seamless inline experience"
    ),
    CodingTask(
        name="Debug Failing Tests",
        description="Identify why 3 unit tests are failing and fix them",
        claude_code_approach="Runs tests, reads output, analyzes code, applies fixes, re-runs to verify",
        copilot_approach="Chat explains errors; developer manually applies suggested fixes",
        winner="Claude Code",
        reasoning="Autonomous test-fix-verify loop saves significant time"
    ),
    CodingTask(
        name="Quick Documentation",
        description="Add docstrings to a single function",
        claude_code_approach="Works well but requires context switch to terminal",
        copilot_approach="Type triple-quote, get instant docstring suggestion",
        winner="Copilot",
        reasoning="Zero-friction for small, inline documentation tasks"
    ),
    CodingTask(
        name="New Feature Implementation",
        description="Build a REST API endpoint with tests and documentation",
        claude_code_approach="Plans approach, creates files, writes tests, runs them, iterates",
        copilot_approach="Assists with each file individually via chat/completions",
        winner="Claude Code",
        reasoning="End-to-end feature development benefits from agentic planning"
    ),
]

def display_comparison(tasks: List[CodingTask]) -> dict:
    """Display the comparison results and return summary statistics"""
    print("=" * 70)
    print("  CLAUDE CODE vs. COPILOT: Practical Developer Comparison")
    print("=" * 70)
    
    scores = {"Claude Code": 0, "Copilot": 0}
    
    for i, task in enumerate(tasks, 1):
        print(f"\n[Task {i}] {task.name}")
        print(f"  Scenario: {task.description}")
        print(f"  ├─ Claude Code: {task.claude_code_approach}")
        print(f"  ├─ Copilot: {task.copilot_approach}")
        print(f"  └─ Winner: {task.winner} — {task.reasoning}")
        scores[task.winner] += 1
    
    print("\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    print(f"  Claude Code wins: {scores['Claude Code']}/{len(tasks)} tasks")
    print(f"  Copilot wins: {scores['Copilot']}/{len(tasks)} tasks")
    print("\n  KEY INSIGHT: Use Claude Code for complex, multi-step autonomous tasks.")
    print("               Use Copilot for fast, inline completions while coding.")
    print("               Many developers use BOTH tools together!\n")
    
    return scores

if __name__ == "__main__":
    results = display_comparison(TASKS)
    # Export results for further analysis
    with open("comparison_results.json", "w") as f:
        json.dump({"tasks": [t.__dict__ for t in TASKS], "scores": results}, f, indent=2)
    print("Results saved to comparison_results.json")
