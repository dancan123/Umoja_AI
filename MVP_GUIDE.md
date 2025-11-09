# 🚀 Umoja AI MVP - Complete Guide

## ✅ What's Been Built

### 1. **Complete Chatbot System**
- ✅ AI-powered conversational interface
- ✅ Multi-language support (Swahili, English, Kikuyu, Luo, Luhya, Kamba)
- ✅ Automatic language detection
- ✅ Conversation history tracking
- ✅ Beautiful web interface

### 2. **Sample Datasets**
Located in `backend/app/data/`:
- ✅ `kenyan_phrases.json` - Common phrases in Kenyan languages
- ✅ `responses.json` - AI response templates

### 3. **API Endpoints**
- ✅ `POST /api/chat/` - Send messages to chatbot
- ✅ `GET /api/chat/history/{session_id}` - Get conversation history
- ✅ `POST /api/sample/` - Create sample items
- ✅ `GET /api/sample/` - List sample items

### 4. **Web Interfaces**
- ✅ Landing page: http://localhost:8000/static/index.html
- ✅ **Chat interface: http://localhost:8000/static/chat.html** ⭐
- ✅ API docs: http://localhost:8000/docs

## 🎯 How to Use the MVP

### Access the Chatbot

1. **Open your browser** and go to:
   ```
   http://localhost:8000/static/chat.html
   ```

2. **Start chatting!** Try these examples:
   - **Swahili**: "Habari", "Mambo vipi", "Asante"
   - **English**: "Hello", "What can you do?", "Tell me about Kenya"
   - **Mixed**: The bot detects your language automatically!

### Test the API

Visit http://localhost:8000/docs for interactive API documentation.

**Example API call:**
```bash
curl -X POST "http://localhost:8000/api/chat/" \
  -H "Content-Type: application/json" \
  -d '{"message": "Habari", "session_id": "test123"}'
```

## 📊 Sample Datasets Location

### Where to Add/Edit Data

**Location**: `backend/app/data/`

#### 1. Adding New Phrases (`kenyan_phrases.json`)

```json
{
  "greetings": {
    "swahili": [
      {
        "phrase": "Your new phrase",
        "translation": "English meaning",
        "response": "Bot's response"
      }
    ]
  }
}
```

#### 2. Adding New Responses (`responses.json`)

```json
{
  "new_topic": {
    "swahili": "Response in Swahili",
    "english": "Response in English",
    "kikuyu": "Response in Kikuyu"
  }
}
```

### How to Update Datasets

1. **Edit the JSON files** in `backend/app/data/`
2. **Save the changes**
3. **Restart the server** (or it auto-reloads)
4. **Test in the chat interface**

## 🔧 Current Features

### Language Detection
- Automatically detects user's language
- Supports 6+ Kenyan languages
- Shows detected language in chat UI

### Conversation Memory
- Stores all conversations in database
- Tracks session history
- Retrievable via API

### Smart Responses
- Matches common phrases
- Topic-based responses
- Fallback for unknown queries

## 📝 Next Steps to Improve

### 1. Add More Language Data
```bash
# Edit these files:
backend/app/data/kenyan_phrases.json
backend/app/data/responses.json
```

### 2. Integrate ML Models
```python
# Future: Add in app/services/chatbot.py
from transformers import pipeline

# Use Hugging Face models for better responses
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-sw-en")
```

### 3. Add Voice Features
```python
# Already have TTS service in:
backend/app/services/text_to_speech.py

# Can add voice input/output to chat interface
```

### 4. Improve Responses
- Add more training data
- Implement context awareness
- Add personality to responses

## 🎨 Customization

### Change Chat UI Colors
Edit `backend/static/chat.html` and modify the CSS:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Add New Quick Actions
In `chat.html`, add buttons:
```html
<button class="quick-action-btn" onclick="sendQuickMessage('Your phrase')">
  🎯 Label
</button>
```

### Modify Bot Personality
Edit responses in `backend/app/data/responses.json`

## 📊 Database

**Location**: `backend/umoja_ai.db` (SQLite)

**Tables**:
- `sample_items` - Sample data
- `conversations` - Chat history

**View data**:
```bash
sqlite3 backend/umoja_ai.db
SELECT * FROM conversations;
```

## 🐛 Troubleshooting

### Chat not working?
1. Check server is running: http://localhost:8000
2. Check browser console for errors (F12)
3. Verify API at http://localhost:8000/docs

### Language detection wrong?
- Add more training phrases to `kenyan_phrases.json`
- The more data, the better detection

### Bot gives default response?
- Add specific phrases/topics to datasets
- Check `app/services/chatbot.py` logic

## 🚀 Deployment Ready

The MVP is ready to:
- ✅ Demo to stakeholders
- ✅ Collect user feedback
- ✅ Test with real users
- ✅ Iterate based on usage

## 📞 Support

For issues or questions:
1. Check the logs in terminal
2. Review API docs at /docs
3. Check dataset files for data issues

---

**Status**: ✅ MVP Complete and Running!
**Access**: http://localhost:8000/static/chat.html
**Last Updated**: 2025-11-09