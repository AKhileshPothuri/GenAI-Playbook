# What is a Large Language Model? - Interactive Beginner's Guide

A hands-on Python demonstration that explains the core concepts behind Large Language Models (LLMs) like ChatGPT and Claude. Perfect companion code for a Medium article introducing LLMs to beginners.

## What This Project Does

This interactive script teaches three fundamental LLM concepts:

1. **Tokenization** - How LLMs break text into tokens (not words!)
2. **Next-Token Prediction** - The core task that powers all LLM magic
3. **Context Windows** - How much text an LLM can "see" at once

No API keys required! Uses OpenAI's `tiktoken` library for real tokenization.

## Installation

bash
# Clone or download this project
# Then install dependencies:
pip install -r requirements.txt


## How to Run

bash
python main.py


## Expected Output


************************************************************
  🤖 WHAT IS A LARGE LANGUAGE MODEL?
     An Interactive Beginner's Guide
************************************************************

============================================================
🔤 CONCEPT 1: TOKENIZATION
============================================================

Original text: 'Hello, LLMs are amazing! 🚀'

Number of tokens: 9
Token IDs: [9906, 11, 445, 11237, 82, 527, 8056, 0, 11410]

Token breakdown:
  Token 1: ID=  9906 -> 'Hello'
  Token 2: ID=    11 -> ','
  Token 3: ID=   445 -> ' L'
  Token 4: ID= 11237 -> 'LM'
  Token 5: ID=    82 -> 's'
  Token 6: ID=   527 -> ' are'
  Token 7: ID=  8056 -> ' amazing'
  Token 8: ID=     0 -> '!'
  Token 9: ID= 11410 -> ' 🚀'

💡 KEY INSIGHT: LLMs don't see words - they see tokens!
   'tokenization' becomes multiple pieces, emojis are single tokens.

============================================================
🎯 CONCEPT 2: NEXT-TOKEN PREDICTION
============================================================

LLMs predict probability of the NEXT token:

  Prompt: 'The cat sat on the ___'
  Likely next tokens: mat (35%), floor (25%), bed (15%), chair (10%)

  Prompt: 'Python is a programming ___'
  Likely next tokens: language (85%), tool (8%), framework (4%)

  Prompt: 'The capital of France is ___'
  Likely next tokens: Paris (95%), Lyon (2%), a (1%)

💡 KEY INSIGHT: LLMs are 'just' predicting the next word,
   but doing this REALLY well enables amazing capabilities!

============================================================
📚 CONCEPT 3: CONTEXT WINDOW
============================================================

Popular LLM context window sizes:
  GPT-3.5           4,096 tokens (~8 pages)
  GPT-4             8,192 tokens (~16 pages)
  GPT-4 Turbo     128,000 tokens (~256 pages)
  Claude 3        200,000 tokens (~400 pages)

  Example: 'Large Language Models are trained on billions of words.'
  Token count: 10 tokens

💡 KEY INSIGHT: More context = better understanding,
   but also more computation and cost!

============================================================
🎓 SUMMARY: THE 3 PILLARS OF LLMs
============================================================

1. TOKENS: LLMs process text as tokens, not words
2. PREDICTION: Core task is predicting the next token
3. CONTEXT: LLMs use surrounding text to make predictions

✨ These simple concepts, scaled massively, create AI magic!
============================================================


## Key Learning Points

- **Tokens ≠ Words**: "LLMs" becomes 3 tokens (L, LM, s), while emojis are often 1 token
- **Scale is the secret**: The same prediction task, done with billions of parameters on trillions of tokens, creates emergent intelligence
- **Context matters**: Larger context windows allow LLMs to understand more, but cost more to run

## Extending This Project

Try modifying the code to:
- Tokenize your own text and see how it breaks down
- Compare token counts between different texts
- Calculate the cost of an API call based on token count

## Resources

- [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer)
- [tiktoken Documentation](https://github.com/openai/tiktoken)
