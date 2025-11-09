# app/services/text_to_speech.py
from gtts import gTTS
import io

def text_to_speech(text: str, lang: str = 'sw') -> bytes:
    """
    Convert text to speech audio.
    
    Args:
        text: The text to convert
        lang: Language code (default: 'sw' for Swahili)
    
    Returns:
        Audio bytes in MP3 format
    """
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer.read()
    except Exception as e:
        print(f"Text-to-speech error: {e}")
        raise