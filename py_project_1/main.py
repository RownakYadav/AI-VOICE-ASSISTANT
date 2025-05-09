import speech_recognition as sr
import webbrowser
import pyttsx3
from AppOpener import open, close
from openai import OpenAI
from gtts import gTTS
import pygame
import os

engine = pyttsx3.init()

def speak(str):
    tts = gTTS(str, lang="en", tld='co.in')
    tts.save('output.mp3')


    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load your MP3 file
    pygame.mixer.music.load("output.mp3")

    # Play the MP3
    pygame.mixer.music.play()

    # Keep the program running while audio is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)

    pygame.mixer.music.unload()
    os.remove("output.mp3")

def ai(command):

    client = OpenAI(
        api_key="AIzaSyA1YNC3rB7p_bVoL5ShB64QDLlBrQQhxsM",
        base_url="Your_api_key"
    )

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
        {"role": "system", "content": "You are a helpful assistant named jarvis like chatgpt and gemini and keep the response 4 lines."},
        {"role": "user","content": command}
        ]
    )

    return response.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open_new("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open_new("https://www.youtube.com")
    elif "open github" in c.lower():
        webbrowser.open_new("https://www.github.com")
    elif "open pinterest" in c.lower():
        webbrowser.open_new("https://www.pinterest.com")
    elif "open instagram" in c.lower():
        webbrowser.open_new("https://www.instagram.com")
    elif "open bts" in c.lower():
        webbrowser.open_new("https://www.weverse.io")
    elif "open whatsapp" in c.lower():
        open("whatsapp")
    elif "close whatsapp" in c.lower():
        close("whatsapp")
    elif "open word" in c.lower():
        open("word")
    elif "close word" in c.lower():
        close("word")
    elif "open paint" in c.lower():
        open("paint")
    elif "close paint" in c.lower():
        close("paint")
    else:
        output = ai(c)
        speak(output)
    
if __name__ == "__main__":

    speak("Intializing Jarvis...")

    while True:
        r = sr.Recognizer()

        print("Recognizing...")
        # obtain audio from the microphone using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")
                # process command
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
                    ai(command)

        except Exception as e:
            print("Error; {0}".format(e))

    
