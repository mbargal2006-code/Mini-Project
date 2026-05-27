#!/usr/bin/env python3
"""Test script to verify AI categorization is working with OpenRouter"""

import sys
import os
sys.path.append('project/backend')

from services.ai import AIService

async def test_ai_categorization():
    ai_service = AIService()
    
    test_thoughts = [
        "I am so angry at my boss for treating me unfairly",
        "I feel guilty about what I said to my friend",
        "I'm scared that I might fail the exam tomorrow",
        "I need everything to be perfect or I can't function",
        "I keep thinking about germs and contamination everywhere"
    ]
    
    print("Testing AI categorization with OpenRouter...")
    print("=" * 50)
    
    for thought in test_thoughts:
        result = await ai_service.analyze_thought(thought)
        print(f"Thought: {thought}")
        print(f"Category: {result['category']}")
        print(f"Distortion: {result['distortion_type']}")
        print("-" * 30)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_ai_categorization())
