import os
import time
import pyautogui
import pyttsx3
import speech_recognition as sr
import requests


def speak(text):
    print(f"Text to speech: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    print("Starting to listen...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        try:
            print("Waiting for command...")
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio, language="en-US")
            print(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("I didn't understand what you said.")
            print("Error: Could not understand what was said.")
            return None
        except sr.RequestError:
            speak("Error with the speech recognition service.")
            print("Error: Speech recognition service unavailable.")
            return None

def generate_command(prompt):
    print(f"Generating command with the prompt: {prompt}")
    
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "model": "command_executer",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()

        result = response.json()
        if 'response' in result:
            return result['response']
        else:
            print("Error: The response does not contain the 'response' field.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error sending the prompt: {e}")
        return None
    except ValueError as e:
        print(f"Error processing the JSON response: {e}")
        return None

def execute_in_cmd(command):
    print(f"Opening CMD and executing: {command}")
    os.system("start cmd")
    time.sleep(1)
    pyautogui.typewrite(command)
    pyautogui.press("enter")
    print("Command executed.")

if __name__ == "__main__":
    speak("Welcome to the voice assistant with Ollama.")
    print("Starting voice assistant with Ollama...")
    
    while True:
        user_input = listen()
        if user_input:
            if "exit" in user_input:
                speak("Goodbye.")
                print("Exiting...")
                break
            else:
                speak("Analyzing the command...")
                print(f"Command received: {user_input}")
                prompt = (
                    "You are a Windows assistant. You receive natural text and respond "
                    "with the corresponding CMD command. Text: " + user_input
                )
                command = generate_command(prompt)
                if command:
                    speak(f"Executing: {command}")
                    execute_in_cmd(command)
