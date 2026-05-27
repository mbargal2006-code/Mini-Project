#!/usr/bin/env python3
"""Test the updated chatbot responses to ensure they're humanistic and realistic"""

import sys
import os
import asyncio

sys.path.append('project/backend')

from services.ai import AIService

async def test_chatbot_responses():
    """Test chatbot with various user messages to check for humanistic responses"""
    
    # Set environment for OpenRouter
    os.environ['AI_PROVIDER'] = 'openrouter'
    os.environ['OPENROUTER_API_KEY'] = os.getenv('OPENROUTER_API_KEY', '<YOUR_OPENROUTER_API_KEY>')
    
    ai_service = AIService()
    
    test_messages = [
        [{"role": "user", "content": "I'm having really bad thoughts today"}],
        [{"role": "user", "content": "I feel like I'm going crazy"}],
        [{"role": "user", "content": "These intrusive thoughts won't stop"}],
        [{"role": "user", "content": "I'm scared of what I might do"}],
        [{"role": "user", "content": "Why is this happening to me?"}]
    ]
    
    print("=== Testing Updated Chatbot Responses ===")
    print("Looking for humanistic, realistic responses (not clinical/therapeutic)\n")
    
    for i, messages in enumerate(test_messages, 1):
        try:
            response = await ai_service.chat_conversation(messages)
            print(f"Test {i}:")
            print(f"User: {messages[0]['content']}")
            print(f"Bot: {response}")
            print("-" * 50)
        except Exception as e:
            print(f"Test {i} failed: {e}")
            print("-" * 50)

if __name__ == "__main__":
    asyncio.run(test_chatbot_responses())
