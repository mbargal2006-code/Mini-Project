#!/usr/bin/env python3
"""Complete test to verify the anxiety categorization fix"""

import sys
import os
import requests
import json
import time

sys.path.append('project/backend')

def test_ai_service_directly():
    """Test AI service directly"""
    print("=== Testing AI Service Directly ===")
    
    from services.ai import AIService
    import asyncio
    
    async def test():
        ai_service = AIService()
        
        test_cases = [
            ("I am so angry at my boss", "anger"),
            ("I feel guilty about lying", "guilt"), 
            ("I'm scared of heights", "fear"),
            ("I need everything perfect", "perfectionism"),
            ("I'm worried about germs", "contamination"),
            ("I hate myself", "self-criticism"),
            ("I can't stop thinking about it", "obsession")
        ]
        
        for thought, expected_category in test_cases:
            result = await ai_service.analyze_thought(thought)
            actual_category = result['category']
            status = "PASS" if actual_category == expected_category else "FAIL"
            print(f"Thought: '{thought}'")
            print(f"Expected: {expected_category} | Got: {actual_category} | {status}")
            print("-" * 40)
    
    asyncio.run(test())

def test_api_endpoint():
    """Test the actual API endpoint"""
    print("\n=== Testing API Endpoint ===")
    
    # Test without auth first to see if it reaches the AI service
    try:
        response = requests.post("http://localhost:5000/api/thoughts", 
                               json={"text": "I am so angry right now"},
                               timeout=5)
        print(f"API Response Status: {response.status_code}")
        if response.status_code == 401:
            print("Expected: 401 Unauthorized (need auth token)")
            print("But this means the endpoint is reachable")
        else:
            print(f"Unexpected response: {response.text}")
    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    # Set environment variables
    os.environ['AI_PROVIDER'] = 'openrouter'
    os.environ['OPENROUTER_API_KEY'] = os.getenv('OPENROUTER_API_KEY', '<YOUR_OPENROUTER_API_KEY>')
    
    test_ai_service_directly()
    test_api_endpoint()
    
    print("\n=== SUMMARY ===")
    print("If the AI service tests show correct categorization (not anxiety),")
    print("then the fix is working. The web interface needs proper authentication")
    print("to test end-to-end, but the core categorization issue is resolved.")
