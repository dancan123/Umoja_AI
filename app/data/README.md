# 📊 Sample Datasets for Umoja AI

This directory contains sample datasets for the Umoja AI chatbot.

## 📁 Files

### `kenyan_phrases.json`
Contains common phrases in Kenyan languages organized by category:
- **Greetings**: Common greetings and their responses
- **Common Questions**: Frequently asked questions
- **Farewells**: Goodbye phrases

**Supported Languages:**
- Swahili (sw)
- English (en)
- Kikuyu (ki)
- Luo (luo)
- Luhya (lu)
- Kamba (kam)

### `responses.json`
Contains AI response templates organized by topic:
- **Capabilities**: What Umoja AI can do
- **Kenya Info**: Information about Kenya
- **Language Learning**: Responses for learning requests
- **Help**: Help and guidance messages
- **Default**: Fallback responses

## 🔧 How to Add More Data

### Adding New Phrases

Edit `kenyan_phrases.json` and add entries in this format:

```json
{
  "greetings": {
    "swahili": [
      {
        "phrase": "Your phrase here",
        "translation": "English translation",
        "response": "Bot's response"
      }
    ]
  }
}
```

### Adding New Response Templates

Edit `responses.json` and add new topics:

```json
{
  "your_topic": {
    "swahili": "Response in Swahili",
    "english": "Response in English",
    "kikuyu": "Response in Kikuyu"
  }
}
```

## 📝 Best Practices

1. **Always include translations** for non-English phrases
2. **Provide responses in multiple languages** when possible
3. **Keep phrases natural** and conversational
4. **Test new phrases** in the chat interface
5. **Document sources** for cultural or traditional phrases

## 🌍 Contributing

To contribute more Kenyan language data:

1. Add phrases to the appropriate category
2. Ensure accuracy of translations
3. Include cultural context when relevant
4. Test in the chat interface
5. Document any special usage notes

## 📚 Resources for Kenyan Languages

- **Swahili**: Most widely spoken, official language
- **Kikuyu**: Spoken by the Kikuyu people
- **Luo**: Spoken by the Luo people
- **Luhya**: Spoken by the Luhya people
- **Kamba**: Spoken by the Kamba people

## 🎯 Future Enhancements

- [ ] Add more languages (Kalenjin, Maasai, etc.)
- [ ] Include audio pronunciations
- [ ] Add cultural context and usage notes
- [ ] Integrate with translation APIs
- [ ] Add domain-specific vocabularies (medical, legal, etc.)