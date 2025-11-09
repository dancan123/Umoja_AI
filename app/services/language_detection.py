# app/services/language_detection.py
from langdetect import detect, DetectorFactory
from app.config import settings

# Set seed for consistent results
DetectorFactory.seed = 0

def detect_language(text: str) -> str:
    """
    Detect the language of the given text.
    Returns language code (e.g., 'sw' for Swahili, 'en' for English)
    """
    try:
        lang_code = detect(text)
        return lang_code
    except Exception as e:
        print(f"Language detection error: {e}")
        return "unknown"

def is_supported_language(lang_code: str) -> bool:
    """Check if the detected language is supported"""
    return lang_code in settings.supported_languages