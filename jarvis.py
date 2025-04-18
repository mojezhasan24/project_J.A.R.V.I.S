import datetime
import subprocess

def speak(audio):
    subprocess.call(["spd-say", audio])

def wishMe():
    hour = datetime.datetime.now().hour  # Fixed: removed incorrect 'hours' parameter
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis, your personal assistant. How can I help you today?")

if __name__ == "__main__":
    speak("Hello, I am Jarvis, your personal assistant.")