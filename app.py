import streamlit as st
from deep_translator import GoogleTranslator
import pyttsx3
import speech_recognition as sr
import sqlite3
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from gtts import gTTS  # Import gTTS
import os  # For file handling

# Set up Groq LLaMA API (Replace with your API Key)
GROQ_API_KEY = "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"

# Initialize TTS Engine
tts_engine = pyttsx3.init()

# Set up SQLite Database
conn = sqlite3.connect("mistakes.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS mistakes (id INTEGER PRIMARY KEY, user_input TEXT, correction TEXT)")
conn.commit()

# Load the model locally
llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=GROQ_API_KEY)

def generate_response(user_input, target_language, user_level):
    """Generates a response using the AI tutor."""
    prompt_template = ChatPromptTemplate.from_template(
        "You are a language tutor. The user is learning {target_language} at {user_level} level. "
        "Set a scene based on their selection and chat with them in {target_language}. "
        "Correct their mistakes and keep track of them. "
        "User: {user_input}"
    )
    prompt = prompt_template.format(target_language=target_language, user_level=user_level, user_input=user_input)
    response = llm.invoke(prompt)
    return response.content.strip()

def translate_text(text, src_lang, dest_lang):
    """Translates text to the desired language."""
    translation = GoogleTranslator(source=src_lang[:2], target=dest_lang[:2]).translate(text)
    return translation

def text_to_speech(translation, src_lang):
    """Convert text to speech and play in Streamlit."""
    audio_file = "output.mp3"  
    tts = gTTS(text=translation, lang=src_lang[:2])
    tts.save(audio_file)  # Save audio file dynamically
    st.audio(audio_file)  # Play audio

def speech_to_text():
    """Convert speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status = st.empty()
        status.write("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the speech."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

def log_mistake(user_input, correction):
    """Logs user mistakes into the SQLite database."""
    cursor.execute("INSERT INTO mistakes (user_input, correction) VALUES (?, ?)", (user_input, correction))
    conn.commit()

def get_mistake_summary():
    """Retrieves and summarizes user mistakes."""
    cursor.execute("SELECT * FROM mistakes")
    return cursor.fetchall()

# Streamlit UI
st.title("🌍 Advanced Language Learning Chatbot")

learning_language = st.selectbox("Select the language you are learning:", ["English", "Spanish", "French", "German", "Japanese", "Chinese", "Hindi"])
known_language = st.selectbox("Select the language you know:", ["English", "Spanish", "French", "German", "Japanese", "Chinese", "Hindi"])
user_level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"])

user_input = st.text_input("Type a message or phrase:")

if st.button("Chat") and user_input:
    response = generate_response(user_input, learning_language, user_level)
    translated_text = translate_text(response, src_lang=learning_language.lower(), dest_lang=known_language.lower())

    st.write("### AI Tutor Response:")
    st.write(response)
    st.write("### Translation:")
    st.write(translated_text)
    
    text_to_speech(translated_text, learning_language.lower())

    # Log user mistakes
    correction = generate_response(user_input, learning_language, "Advanced")
    log_mistake(user_input, correction)

if st.button("Speak & Check Pronunciation"):
    spoken_text = speech_to_text()
    st.write("You said:", spoken_text)
    st.write("### AI Feedback:")
    st.write(generate_response(spoken_text, learning_language, user_level))
    response1=generate_response(spoken_text, learning_language, user_level)
    translated_text = translate_text(response1, src_lang=learning_language.lower(), dest_lang=known_language.lower())
    st.write("### Translation:")
    st.write(translated_text)
    text_to_speech(translated_text, learning_language.lower())