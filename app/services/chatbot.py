# app/services/chatbot.py
import json
import os
from pathlib import Path
from app.services.language_detection import detect_language

# Load datasets
DATA_DIR = Path(__file__).parent.parent / "data"

def load_json_data(filename: str) -> dict:
    """Load JSON data from the data directory"""
    filepath = DATA_DIR / filename
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load datasets at module level
PHRASES = load_json_data("kenyan_phrases.json")
RESPONSES = load_json_data("responses.json")

def get_language_name(lang_code: str) -> str:
    """Convert language code to full name"""
    lang_map = {
        'sw': 'swahili',
        'en': 'english',
        'ki': 'kikuyu',
        'luo': 'luo',
        'lu': 'luhya',
        'kam': 'kamba'
    }
    return lang_map.get(lang_code, 'english')

def find_matching_phrase(message: str, lang: str) -> str | None:
    """Find a matching phrase in the dataset"""
    message_lower = message.lower().strip()
    
    # Check greetings
    if lang in PHRASES['greetings']:
        for item in PHRASES['greetings'][lang]:
            if message_lower in item['phrase'].lower() or item['phrase'].lower() in message_lower:
                return item['response']
    
    # Check farewells
    if lang in PHRASES['farewells']:
        for item in PHRASES['farewells'][lang]:
            if message_lower in item['phrase'].lower() or item['phrase'].lower() in message_lower:
                return item['response']
    
    return None

def get_response_by_topic(message: str, lang: str) -> str | None:
    """Get response based on message topic"""
    message_lower = message.lower()
    
    # Check for capability questions
    if any(word in message_lower for word in ['what can you', 'unaweza', 'capabilities', 'unafanya nini']):
        return RESPONSES['capabilities'].get(lang, RESPONSES['capabilities']['english'])
    
    # Check for Kenya info
    if any(word in message_lower for word in ['kenya', 'about kenya', 'kuhusu kenya']):
        return RESPONSES['kenya_info'].get(lang, RESPONSES['kenya_info']['english'])
    
    # Check for help
    if any(word in message_lower for word in ['help', 'msaada', 'nisaidie']):
        return RESPONSES['help'].get(lang, RESPONSES['help']['english'])
    
    # Check for language learning
    if any(word in message_lower for word in ['learn', 'jifunza', 'teach', 'fundisha']):
        return RESPONSES['language_learning'].get(lang, RESPONSES['language_learning']['english'])
    
    return None

def generate_response(message: str) -> tuple[str, str]:
    """
    Generate a response to the user's message.
    Returns: (response, detected_language)
    """
    # Detect language
    detected_lang_code = detect_language(message)
    lang = get_language_name(detected_lang_code)
    
    # Try to find exact phrase match
    response = find_matching_phrase(message, lang)
    if response:
        return response, detected_lang_code
    
    # Try to find topic-based response
    response = get_response_by_topic(message, lang)
    if response:
        return response, detected_lang_code
    
    # Default response
    default_response = RESPONSES['default'].get(lang, RESPONSES['default']['english'])
    return default_response, detected_lang_code