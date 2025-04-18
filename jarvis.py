import pyttsx3
engine = pyttsx3.init('espeak', debug=True)
voices = engine.getProperty('voices')
print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
if __name__ == "__main__":
    speak("Hello, I am Jarvis, your personal assistant.")