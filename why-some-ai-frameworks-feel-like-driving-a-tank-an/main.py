#!/usr/bin/env python3
"""
Why Some AI Frameworks Feel Like Driving a Tank
================================================
This demo compares THREE approaches to the same task:
1. Raw OpenAI API (bicycle - simple, direct)
2. LangChain (SUV - moderate abstraction)
3. Simulated "Enterprise Framework" (tank - maximum ceremony)

All three do the SAME thing: summarize text. Watch the complexity grow!
"""

import os
import time
from typing import Optional

# We'll simulate the enterprise framework to avoid heavy dependencies
# But use real OpenAI for the first two approaches

def approach_1_bicycle(text: str, api_key: str) -> dict:
    """The Bicycle: Raw OpenAI API - just ride and go!"""
    from openai import OpenAI
    
    client = OpenAI(api_key=api_key)
    start = time.time()
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize in one sentence: {text}"}],
        max_tokens=100
    )
    
    return {
        "result": response.choices[0].message.content,
        "time": time.time() - start,
        "lines_of_code": 6,
        "concepts_to_learn": ["API client", "messages format"]
    }

def approach_2_suv(text: str, api_key: str) -> dict:
    """The SUV: LangChain - comfortable, more features, more setup"""
    from langchain_openai import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    from langchain.schema.output_parser import StrOutputParser
    
    start = time.time()
    
    # Build the chain (LangChain way)
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, max_tokens=100)
    prompt = ChatPromptTemplate.from_template("Summarize in one sentence: {text}")
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"text": text})
    
    return {
        "result": result,
        "time": time.time() - start,
        "lines_of_code": 8,
        "concepts_to_learn": ["ChatPromptTemplate", "Chain composition", "OutputParser", "LCEL syntax"]
    }

def approach_3_tank(text: str, api_key: str) -> dict:
    """The Tank: Simulated Enterprise Framework - maximum ceremony!"""
    start = time.time()
    
    # Simulating what heavy frameworks often require...
    print("    [Tank] Initializing AgentOrchestrationManager...")
    print("    [Tank] Loading PromptTemplateRegistry...")
    print("    [Tank] Configuring MemoryBufferStrategyFactory...")
    print("    [Tank] Establishing CallbackHandlerChain...")
    print("    [Tank] Validating AgentRoleDefinitionSchema...")
    time.sleep(0.5)  # Simulated initialization overhead
    
    # Under the hood, tanks still just call the API!
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize in one sentence: {text}"}],
        max_tokens=100
    )
    
    return {
        "result": response.choices[0].message.content,
        "time": time.time() - start,
        "lines_of_code": "50+ (config files not included)",
        "concepts_to_learn": ["Agents", "Crews", "Tasks", "Roles", "Memory", "Callbacks", 
                              "Tools", "Orchestration", "YAML configs", "Delegation patterns"]
    }

def main():
    """Run all three approaches and compare results."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Please set OPENAI_API_KEY environment variable")
        print("   export OPENAI_API_KEY='your-key-here'")
        return
    
    sample_text = """
    The Python programming language was created by Guido van Rossum and first 
    released in 1991. It emphasizes code readability with significant whitespace 
    and supports multiple programming paradigms including procedural, object-oriented, 
    and functional programming. Python has become one of the most popular languages 
    for AI and machine learning applications.
    """
    
    print("="*60)
    print("🚲 vs 🚙 vs 🚛  FRAMEWORK COMPLEXITY SHOWDOWN")
    print("="*60)
    print(f"\nTask: Summarize a paragraph about Python\n")
    
    approaches = [
        ("🚲 BICYCLE (Raw API)", approach_1_bicycle),
        ("🚙 SUV (LangChain)", approach_2_suv),
        ("🚛 TANK (Enterprise)", approach_3_tank),
    ]
    
    results = []
    for name, func in approaches:
        print(f"\n{'-'*50}")
        print(f"{name}")
        print(f"{'-'*50}")
        result = func(sample_text, api_key)
        results.append((name, result))
        print(f"  Result: {result['result']}")
        print(f"  Time: {result['time']:.2f}s")
        print(f"  Lines of code: {result['lines_of_code']}")
        print(f"  Concepts to learn: {len(result['concepts_to_learn'])}")
    
    print(f"\n{'='*60}")
    print("📊 THE VERDICT")
    print("="*60)
    print("""
    Use the BICYCLE (raw API) when:
    ✓ Simple, one-off tasks
    ✓ Learning how things work
    ✓ Maximum control needed
    
    Use the SUV (LangChain) when:
    ✓ Building chains of operations  
    ✓ Need prompt templating
    ✓ Want ecosystem integrations
    
    Use the TANK (heavy frameworks) when:
    ✓ Multi-agent orchestration
    ✓ Complex workflow management
    ✓ Enterprise requirements
    ✓ You ACTUALLY need the firepower!
    
    Remember: A tank is overkill for grocery shopping! 🛒
    """)

if __name__ == "__main__":
    main()