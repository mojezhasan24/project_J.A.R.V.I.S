import datetime
import subprocess
import speech_recognition as sr
import time


def speak(audio):
    subprocess.call(["spd-say", audio])

def wishMe():
    hour = datetime.datetime.now().hour  # Get the current hour
    print(f"Current hour: {hour}")  # Debugging: Print the current hour

    if hour >= 0 and hour < 12:
        print("Executing morning greeting...")  # Debugging
        speak("Good morning sir!")
        time.sleep(1)
        speak("I am Jarvis, your personal assistant. How can I help you today?")
    elif hour >= 12 and hour < 18:
        print("Executing afternoon greeting...")  # Debugging
        speak("Good afternoon sir!")
        time.sleep(1)
        speak("I am Jarvis, your personal assistant. How can I help you today?")
    else:
        print("Executing evening greeting...")  # Debugging
        speak("Good evening sir!")
        time.sleep(1)
        speak("I am Jarvis, your personal A.I. assistant. How can I help you today()")

def takeCommand():
    # This function will take microphone input and return the string output
    # You can implement this function using speech recognition libraries

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        r.energy_threshold = 2000
        r.phrase_threshold = 1 # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry, I did not get that. Please say that again.")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()
    
    