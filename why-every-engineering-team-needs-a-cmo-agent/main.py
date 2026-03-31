"""CMO Agent: AI-powered marketing strategy for engineering teams.

This demo shows how engineering teams can use an AI agent to generate
market positioning, messaging, and go-to-market insights for their products.
"""

import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# CMO Agent system prompt - defines the agent's expertise and behavior
CMO_SYSTEM_PROMPT = """You are a CMO (Chief Marketing Officer) Agent for engineering teams.
Your expertise includes: market positioning, competitive analysis, messaging strategy,
and go-to-market planning. You translate technical features into customer value.

Be concise, actionable, and speak in terms engineers understand.
Format your responses with clear sections and bullet points."""

def cmo_agent(product_description: str, task: str) -> str:
    """Run the CMO agent on a specific marketing task."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": CMO_SYSTEM_PROMPT},
            {"role": "user", "content": f"Product: {product_description}\n\nTask: {task}"}
        ],
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message.content

def run_cmo_analysis(product: str) -> dict:
    """Run a complete CMO analysis on a product."""
    # Define the key CMO tasks
    tasks = {
        "positioning": "Create a one-sentence positioning statement and identify the target audience.",
        "messaging": "Write 3 key marketing messages that translate technical features to customer benefits.",
        "competitive": "Identify 2-3 potential competitors and our key differentiator.",
        "gtm_advice": "Suggest 3 actionable go-to-market tactics for an engineering team with no marketing budget."
    }
    
    results = {}
    print("\n🎯 CMO Agent analyzing your product...\n")
    print("=" * 50)
    
    for task_name, task_prompt in tasks.items():
        print(f"\n📊 Analyzing: {task_name.replace('_', ' ').title()}...")
        results[task_name] = cmo_agent(product, task_prompt)
        print(f"\n{results[task_name]}")
        print("-" * 50)
    
    return results

def main():
    """Main entry point - demo with a sample engineering product."""
    # Sample product an engineering team might build
    sample_product = """
    FastCache: An open-source, Redis-compatible in-memory cache written in Rust.
    Features: 2x faster than Redis for small payloads, single binary deployment,
    built-in clustering, and automatic memory management. MIT licensed.
    """
    
    print("\n" + "=" * 50)
    print("🤖 CMO AGENT - Marketing Intelligence for Engineers")
    print("=" * 50)
    print(f"\nProduct being analyzed:{sample_product}")
    
    # Run the CMO analysis
    run_cmo_analysis(sample_product)
    
    print("\n✅ CMO Analysis Complete!")
    print("\n💡 Tip: Replace 'sample_product' with your own product description.")

if __name__ == "__main__":
    main()
