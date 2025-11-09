#!/usr/bin/env python3
"""
Quick test script for Umoja AI chatbot
Run this to test the chatbot functionality
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_chat(message: str, session_id: str = "test_session"):
    """Test the chat endpoint"""
    url = f"{BASE_URL}/api/chat/"
    payload = {
        "message": message,
        "session_id": session_id
    }
    
    print(f"\n{'='*60}")
    print(f"YOU: {message}")
    print(f"{'='*60}")
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        print(f"BOT: {data['response']}")
        print(f"Language Detected: {data['detected_language']}")
        print(f"Session ID: {data['session_id']}")
        
        return data
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def main():
    """Run test conversations"""
    print("\n🇰🇪 Testing Umoja AI Chatbot")
    print("="*60)
    
    # Test different languages
    test_messages = [
        "Habari",  # Swahili greeting
        "What can you do?",  # English question
        "Tell me about Kenya",  # English info request
        "Asante",  # Swahili thank you
        "Nisaidie kujifunza",  # Swahili learning request
        "Kwaheri"  # Swahili goodbye
    ]
    
    session_id = "test_session_001"
    
    for message in test_messages:
        test_chat(message, session_id)
        input("\nPress Enter to continue...")
    
    print("\n" + "="*60)
    print("✅ Test completed!")
    print(f"View full conversation at: {BASE_URL}/static/chat.html")
    print(f"API docs at: {BASE_URL}/docs")

if __name__ == "__main__":
    main()