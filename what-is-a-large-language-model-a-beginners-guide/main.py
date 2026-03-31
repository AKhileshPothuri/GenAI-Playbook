#!/usr/bin/env python3
"""
What is a Large Language Model? - Interactive Beginner's Guide

This script demonstrates the core concepts of LLMs through hands-on examples:
1. Tokenization - How LLMs break text into pieces
2. Next-word prediction - The fundamental task LLMs perform
3. Context and prompting - How LLMs use context to generate responses
"""

import tiktoken  # OpenAI's tokenizer library


def demonstrate_tokenization(text: str) -> None:
    """Show how LLMs break text into tokens (not just words!)."""
    print("\n" + "="*60)
    print("🔤 CONCEPT 1: TOKENIZATION")
    print("="*60)
    print(f"\nOriginal text: '{text}'")
    
    # Use GPT-4's tokenizer (cl100k_base encoding)
    encoder = tiktoken.get_encoding("cl100k_base")
    tokens = encoder.encode(text)
    
    print(f"\nNumber of tokens: {len(tokens)}")
    print(f"Token IDs: {tokens}")
    
    # Show each token decoded
    print("\nToken breakdown:")
    for i, token_id in enumerate(tokens):
        token_text = encoder.decode([token_id])
        print(f"  Token {i+1}: ID={token_id:6d} -> '{token_text}'")
    
    print("\n💡 KEY INSIGHT: LLMs don't see words - they see tokens!")
    print("   'tokenization' becomes multiple pieces, emojis are single tokens.")


def demonstrate_prediction() -> None:
    """Show the core task: predicting the next token."""
    print("\n" + "="*60)
    print("🎯 CONCEPT 2: NEXT-TOKEN PREDICTION")
    print("="*60)
    
    # Simple probability demonstration
    examples = [
        ("The cat sat on the", ["mat (35%)", "floor (25%)", "bed (15%)", "chair (10%)"]),
        ("Python is a programming", ["language (85%)", "tool (8%)", "framework (4%)"]),
        ("The capital of France is", ["Paris (95%)", "Lyon (2%)", "a (1%)"])
    ]
    
    print("\nLLMs predict probability of the NEXT token:")
    for prompt, predictions in examples:
        print(f"\n  Prompt: '{prompt} ___'")
        print(f"  Likely next tokens: {', '.join(predictions)}")
    
    print("\n💡 KEY INSIGHT: LLMs are 'just' predicting the next word,")
    print("   but doing this REALLY well enables amazing capabilities!")


def demonstrate_context_window() -> None:
    """Explain how context affects LLM responses."""
    print("\n" + "="*60)
    print("📚 CONCEPT 3: CONTEXT WINDOW")
    print("="*60)
    
    encoder = tiktoken.get_encoding("cl100k_base")
    
    # Show context window sizes
    print("\nPopular LLM context window sizes:")
    models = [
        ("GPT-3.5", 4096),
        ("GPT-4", 8192),
        ("GPT-4 Turbo", 128000),
        ("Claude 3", 200000)
    ]
    for model, tokens in models:
        pages = tokens // 500  # Rough estimate: ~500 tokens per page
        print(f"  {model:15} {tokens:>7,} tokens (~{pages} pages)")
    
    # Demonstrate with a sample text
    sample = "Large Language Models are trained on billions of words."
    tokens = encoder.encode(sample)
    print(f"\n  Example: '{sample}'")
    print(f"  Token count: {len(tokens)} tokens")
    
    print("\n💡 KEY INSIGHT: More context = better understanding,")
    print("   but also more computation and cost!")


def main():
    """Run all demonstrations."""
    print("\n" + "*"*60)
    print("  🤖 WHAT IS A LARGE LANGUAGE MODEL?")
    print("     An Interactive Beginner's Guide")
    print("*"*60)
    
    # Demo 1: Tokenization
    demonstrate_tokenization("Hello, LLMs are amazing! 🚀")
    
    # Demo 2: Next-token prediction
    demonstrate_prediction()
    
    # Demo 3: Context windows
    demonstrate_context_window()
    
    print("\n" + "="*60)
    print("🎓 SUMMARY: THE 3 PILLARS OF LLMs")
    print("="*60)
    print("\n1. TOKENS: LLMs process text as tokens, not words")
    print("2. PREDICTION: Core task is predicting the next token")
    print("3. CONTEXT: LLMs use surrounding text to make predictions")
    print("\n✨ These simple concepts, scaled massively, create AI magic!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
