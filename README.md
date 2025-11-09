 HEAD
# 🇰🇪 Umoja AI - Kenyan Language AI Platform

A FastAPI-based backend for processing and working with Kenyan local languages.

## 📁 Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Application configuration
│   ├── database.py          # Database setup and session management
│   │
│   ├── models/              # SQLAlchemy database models
│   │   ├── __init__.py
│   │   └── sample.py
│   │
│   ├── crud/                # Database CRUD operations
│   │   ├── __init__.py
│   │   └── sample.py
│   │
│   ├── routers/             # API route handlers
│   │   ├── __init__.py
│   │   └── sample.py
│   │
│   ├── schemas/             # Pydantic models for request/response
│   │   ├── __init__.py
│   │   └── sample.py
│   │
│   └── services/            # Business logic for AI features
│       ├── __init__.py
│       ├── language_detection.py
│       ├── text_to_speech.py
│       └── translation.py
│
├── static/                  # Static files (HTML, CSS, JS)
│   └── index.html
│
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Getting Started

### 1. Install Dependencies

```bash
# Activate virtual environment (if not already activated)
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

### 2. Run the Application

```bash
# From the backend directory
uvicorn app.main:app --reload
```

The application will be available at:
- **💬 Chat Interface**: http://localhost:8000/static/chat.html ⭐ **START HERE**
- **🏠 Landing Page**: http://localhost:8000/static/index.html
- **📚 API Docs**: http://localhost:8000/docs
- **🔌 API Base**: http://localhost:8000

### 3. Test the Chatbot

**Option 1: Web Interface (Recommended)**
- Open http://localhost:8000/static/chat.html
- Start chatting in any supported language!

**Option 2: Test Script**
```bash
python test_chatbot.py
```

**Option 3: API Direct**
```bash
curl -X POST "http://localhost:8000/api/chat/" \
  -H "Content-Type: application/json" \
  -d '{"message": "Habari", "session_id": "test123"}'
```

## 🌍 Supported Languages

- **Swahili** (sw)
- **English** (en)
- **Kikuyu** (ki)
- **Luhya** (lu)
- **Luo** (luo)
- **Kamba** (kam)

## 📚 API Endpoints

### Chat Endpoints (MVP)
- `POST /api/chat/` - Send a message to the chatbot
- `GET /api/chat/history/{session_id}` - Get conversation history

### Sample Endpoints
- `POST /api/sample/` - Create a new sample item
- `GET /api/sample/` - List all sample items
- `GET /api/sample/{item_id}` - Get a specific item

## 🛠️ Services

### Language Detection
Located in `app/services/language_detection.py`
- Detects the language of input text
- Validates against supported Kenyan languages

### Text-to-Speech
Located in `app/services/text_to_speech.py`
- Converts text to speech audio
- Supports multiple languages including Swahili

### Translation (Placeholder)
Located in `app/services/translation.py`
- Ready for integration with translation models
- Supports translation between Kenyan languages

## 🔧 Configuration

Edit `app/config.py` to modify:
- Database URL
- Supported languages
- Application settings

## 📊 Sample Datasets

**Location**: `app/data/`

- **`kenyan_phrases.json`**: Common phrases in Kenyan languages (greetings, questions, farewells)
- **`responses.json`**: AI response templates organized by topic

**To add more data**: Edit these JSON files and the chatbot will automatically use them!

See `app/data/README.md` for detailed instructions.

## 📝 Next Steps

### MVP Improvements
1. **Add More Language Data**: Expand `kenyan_phrases.json` with more phrases
2. **Improve Responses**: Add more topics to `responses.json`
3. **Voice Features**: Integrate text-to-speech in chat UI
4. **Context Awareness**: Make bot remember conversation context

### Advanced Features
1. **Integrate ML Models**: Add Hugging Face models for better language processing
2. **Translation API**: Implement real-time translation between languages
3. **Add Authentication**: Implement user authentication and API keys
4. **Database Migrations**: Set up Alembic for database migrations
5. **Testing**: Add unit and integration tests
6. **Docker**: Containerize the application

## 🤝 Contributing

This is a local Kenyan AI project. Contributions are welcome!

## 📄 License


# Umoja_AI
 59900c9e231ff882059816886f26a57cd3892368
