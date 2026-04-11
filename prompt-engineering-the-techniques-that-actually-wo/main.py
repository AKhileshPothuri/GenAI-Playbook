#!/usr/bin/env python3
"""
Prompt Engineering Techniques Demo
Demonstrates 5 proven techniques that actually improve LLM outputs.
"""

import os
from anthropic import Anthropic

# Initialize the Anthropic client
client = Anthropic()  # Uses ANTHROPIC_API_KEY env variable

def basic_prompt(question: str) -> str:
    """Technique 1: Basic prompt - no engineering (baseline)"""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text

def role_based_prompt(question: str) -> str:
    """Technique 2: Role/Persona prompting - assign expertise"""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        system="You are a senior software architect with 15 years of experience. Be concise and practical.",
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text

def few_shot_prompt(question: str) -> str:
    """Technique 3: Few-shot learning - provide examples"""
    examples = """Examples of good code review feedback:
- Input: "i=i+1" -> Output: "Use i += 1 for cleaner increment"
- Input: "if x == True:" -> Output: "Simplify to 'if x:' for boolean checks"
- Input: "except:" -> Output: "Avoid bare except; catch specific exceptions"

Now review this:"""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        messages=[{"role": "user", "content": f"{examples}\n{question}"}]
    )
    return response.content[0].text

def chain_of_thought_prompt(question: str) -> str:
    """Technique 4: Chain-of-thought - encourage step-by-step reasoning"""
    cot_instruction = f"{question}\n\nThink through this step-by-step before giving your final answer."
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        messages=[{"role": "user", "content": cot_instruction}]
    )
    return response.content[0].text

def structured_output_prompt(question: str) -> str:
    """Technique 5: Structured output - specify exact format"""
    structured = f"""{question}

Respond in this exact JSON format:
{{"summary": "one sentence", "pros": ["list"], "cons": ["list"], "recommendation": "one sentence"}}"""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=250,
        messages=[{"role": "user", "content": structured}]
    )
    return response.content[0].text

def main():
    """Run all 5 techniques on sample questions to compare outputs."""
    print("="*60)
    print("PROMPT ENGINEERING TECHNIQUES COMPARISON")
    print("="*60)
    
    # Test questions for each technique
    demos = [
        ("1. BASIC (Baseline)", basic_prompt, "What is Docker?"),
        ("2. ROLE-BASED", role_based_prompt, "What is Docker?"),
        ("3. FEW-SHOT", few_shot_prompt, "data = data"),
        ("4. CHAIN-OF-THOUGHT", chain_of_thought_prompt, "Should I use SQL or NoSQL for a chat app?"),
        ("5. STRUCTURED OUTPUT", structured_output_prompt, "Evaluate Python vs JavaScript for backend"),
    ]
    
    for name, technique, question in demos:
        print(f"\n{'─'*60}\n{name}\nQuestion: {question}\n{'─'*60}")
        print(technique(question))
    
    print("\n" + "="*60)
    print("KEY TAKEAWAY: Match the technique to your use case!")
    print("="*60)

if __name__ == "__main__":
    main()
