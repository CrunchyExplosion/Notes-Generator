import google.generativeai as genai
import os
import textwrap
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '*')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Retrieve API key from environment variable
GOOGLE_API_KEY = 'AIzaSyAhd6hBehgK4QRMrnGgukT1VZKSoDqNETk'

genai.configure(api_key=GOOGLE_API_KEY)

# List available models for user selection
print("Available models:")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# Get user's model choice
while True:
  model_name = input("Enter the name of the model you'd like to use: ")
  try:
    model = genai.GenerativeModel(model_name)
    break  # Exit loop if the model is found
  except ValueError:
    print("Model not found. Please choose from the available models.")


#user_speech="""
#Machine learning plays a fundamental role in the realm of artificial intelligence (AI) by enabling systems to learn from data and improve 
#their performance without being explicitly programmed. At its core, machine learning algorithms analyze large amounts of data, identify patterns, 
#and make predictions or decisions based on those patterns. This process mimics the way humans learn, albeit at a much faster and scalable pace. By 
#leveraging techniques such as supervised learning, unsupervised learning, and reinforcement learning, machine learning algorithms can handle a wide 
#range of tasks, from image and speech recognition to natural language processing and autonomous decision-making. In the context of AI, machine learning 
#acts as the engine that drives intelligent behavior by allowing systems to adapt and improve over time through experience. This adaptive capability is 
#particularly crucial in complex and dynamic environments where traditional rule-based systems may fall short. Moreover, the integration of machine 
#learning with other AI techniques such as knowledge representation, reasoning, and planning enhances the overall intelligence of AI systems, enabling 
#them to solve more intricate problems and make more informed decisions. As technology advances and more sophisticated algorithms are developed, 
#the role of machine learning in AI continues to expand, driving innovation and unlocking new possibilities across various industries and domains.
#"""

#user_speech="""
#India, officially the Republic of India,is a country in South Asia. It is the 
#seventh-largest country by area; the most populous country as of June 2023;and 
#from the time of its independence in 1947, the world's most populous democracy.
#Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, 
#and the Bay of Bengal on the southeast, it shares land borders with Pakistan to 
#the west; China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar 
#to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the 
#Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, 
#Myanmar, and Indonesia.
#"""







#----------------------------- For Speech Detection ------------------------------------------------
import speech_recognition as sr

def listen():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise levels
        recognizer.adjust_for_ambient_noise(source)

        # Listen to the user's speech
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Use Google Speech Recognition to convert audio to text
        # text = recognizer.recognize_google(audio, language='hi-IN') for hindi
        text = recognizer.recognize_google(audio)

        # Print the recognized text
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None

    except sr.RequestError as e:
        print("Sorry, an error occurred. Please try again later.")
        return None
    
user_speech=listen()




# Get user's prompt
user_prompt = "I am giving you content please make directly provide me notes of it."

# Generate and display response
try:
  response = model.generate_content(user_prompt+user_speech)
  print(response.text)
  #display(to_markdown(response.text))
except Exception as e:
  print(f"An error occurred: {e}")


#def func1():
#      question=input("Here You Go -> ")
#      try:
#        response = model.generate_content(f"""please answer this question in short and to point ({question}) use the data given 
#                                          further as a conntext you can add more information from your side"""+user_speech)
#        print(response.text)
#        #display(to_markdown(response.text))
#      except Exception as e:
#        print(f"An error occurred: {e}")


# Gives option to write or speak text
def func1():
      choice=input("How you would like to ask a question?\n1. Voice \n2. Type \n( v / t) ? --> ")
      if(choice=="v"):
        press_enter=input("Hit enter and speak...")
        question=listen()
      else:
        question=input("Here You Go . Please ask -> ")
    
      
      try:
        response = model.generate_content(f"""please answer this question in short and to point ({question}) use the data given 
                                          further as a context you can add more information from your side"""+user_speech)
        print(response.text)
        #display(to_markdown(response.text))
      except Exception as e:
        print(f"An error occurred: {e}")


while(True):
  ask=input("Do you want to ask any question related to it? (y/n) ")
  if(ask=="y"):
    func1()
  else:
    break
  
print("""Thanks for using the program ; ) 
      Developed By : Apoorv , Chinmay and Harsh.
      Special Thanks Gemini Google 
      """)
