from flask import Flask, render_template, request
import speech_recognition as sr
import google.generativeai as genai
import os
import textwrap
from IPython.display import Markdown

app = Flask(__name__)

# Configure Google AI API
#GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  # Make sure to set your API key in your environment
genai.configure(api_key='AIzaSyAhd6hBehgK4QRMrnGgukT1VZKSoDqNETk')

# Initialize speech recognizer
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError as e:
        print("Sorry, an error occurred. Please try again later.")
        return None

# Load AI model
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    user_prompt = "I am giving you content please make directly provide me notes of it."
    user_speech = listen()
    model_name = request.form['model_name']  # Adjust this based on your HTML form
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(user_prompt + user_speech)
        return render_template('result.html', response=response.text)
    except Exception as e:
        error_message = f"An error occurred: {e}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
