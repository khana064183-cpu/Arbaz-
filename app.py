import streamlit as str
import google.generativeai as genai
import os

# Google Colab की Secrets (UserData) से आपकी API Key "Arbazkhankey" को लोड करना
# नोट: सुनिश्चित करें कि आपने Colab के Left Sidebar में '🔑 (Key icon)' पर जाकर 
# Name में "Arbazkhankey" और Value में अपनी असली Key डाली हुई है।
try:
    from google.colab import userdata
    api_key = userdata.get('Arbazkhankey')
except Exception:
    api_key = None

# अगर Colab Secrets में नहीं मिली, तो डायरेक्ट की सेट करना
if not api_key:
    api_key = "AIza..." # यहाँ अपनी AIza से शुरू होने वाली असली Key डाल सकते हैं

genai.configure(api_key=api_key)

# ऐप का इंटरफेस और आपका नाम "Alsasy" सेट कर दिया है
str.title("AI Assistant")
str.write("Hello Alsasy! Main aapka AI Assistant hoon.")

user_input = str.text_input("Mujhse kuch bhi puchiye:")
if user_input:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        str.write(response.text)
    except Exception as e:
        str.error(f"Error: {e}. Kripya check karein ki aapki API Key sahi hai ya nahi.")
