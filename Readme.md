#  AI-Powered Language Learning Chatbot

##  About This Project
This AI-powered chatbot is designed to help users practice and improve their language skills in a fun and interactive way. It provides:
- **Real-time conversation practice** with an AI tutor.
- **Speech recognition & pronunciation feedback.**
- **Grammar correction & mistake tracking.**
- **Multilingual support** with AI-powered translations.

##  Features
✅ Chat in multiple languages: English, Spanish, French, German, Japanese, Chinese, and Hindi.  
✅ AI-generated grammar corrections with mistake tracking.  
✅ Speech-to-text for pronunciation feedback.  
✅ Text-to-speech to help with listening practice.  
✅ A database to store and review your mistakes.  
✅ Powered by **Groq LLaMA-3.3-70B**, Google Translate, gTTS, and SpeechRecognition.  

##  Tech Stack
- **Python** (Backend logic)
- **Streamlit** (User interface)
- **Groq API** (AI Language Model)
- **Google Translate API** (Translation)
- **gTTS (Google Text-to-Speech)** (For audio output)
- **SpeechRecognition** (For voice input)
- **SQLite** (For tracking mistakes)

##  How to Set Up
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-language-chatbot.git
cd ai-language-chatbot
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys
Create a `.env` file in the root directory and add:
```bash
GROQ_API_KEY=your_groq_api_key
```

```
Then add:
```toml
GROQ_API_KEY = "your_groq_api_key"
```

### 5️⃣ Run the App
```bash
streamlit run app.py
```

## 🏆 How to Use
1. Choose the **language** you want to learn and your **native language**.
2. Select your **proficiency level** (Beginner, Intermediate, Advanced).
3. Type a message or use **voice input** to chat with the AI tutor.
4. Receive **AI-generated responses, translations, and corrections**.
5. Listen to **text-to-speech output** for pronunciation practice.
6. Track and review your mistakes in the **mistake log**.

## 📚 Future Plans
🔹 Expand to support **more languages** and regional dialects.  
🔹 Improve **grammar correction accuracy** using advanced NLP techniques.  
🔹 Add a **chat history** feature for better learning retention.  
🔹 Deploy the app on **Streamlit Cloud** or **Hugging Face Spaces**.  

## 💡 Contribute to the Project
If you have ideas for improvements, feel free to fork this repo, make changes, and submit a pull request. Contributions are always welcome!

## 📜 License
This project is licensed under the **MIT License**.

---

Built with ❤️ by [Your Name]

