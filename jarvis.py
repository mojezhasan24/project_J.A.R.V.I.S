import datetime
import subprocess
import speech_recognition as sr
import time
import wikipedia
import webbrowser
import os
import random  # Make sure this import is at the top if you're using random selection
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


def speak(audio):
    subprocess.call(["spd-say", audio])

def wishMe():
    hour = datetime.datetime.now().hour  # Get the current hour
    print(f"Current hour: {hour}")  # Debugging: Print the current hour

    if hour >= 0 and hour < 12:
        print("Executing morning greeting...")  # Debugging
        speak("Good morning sir!")
        time.sleep(1)
        speak("I am Jarvis, your personal A.I. assistant. How can I help you today?")
    elif hour >= 12 and hour < 18:
        print("Executing afternoon greeting...")  # Debugging
        speak("Good afternoon sir!")
        time.sleep(1)
        speak("I am Jarvis, your personal A.I. assistant. How can I help you today?")
    else:
        print("Executing evening greeting...")  # Debugging
        speak("Good evening sir!")
        time.sleep(1)
        speak("I am Jarvis, your personal A. I. assistant. How can I help you today?")

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
    time.sleep(1)
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
    time.sleep(2)
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query or 'wiki' in query:
            # speak("Searching Wikipedia for...")
            sub_query = query.replace("wikipedia", "").replace("wiki", "").strip()
            results = wikipedia.summary(sub_query, sentences=2)

            speak(f"serching wikipedia for {sub_query}")
            # results = wikipedia.summary(query, sentences=2)
            # speak("according to wikipedia")
            print(results)
            speak(results)
            time.sleep(20)
            speak("sir, do you want me to search it on youtube too")
            query2=takeCommand().lower()
            if "yes" in query2:
                speak("opening youtube")
                webbrowser.open("youtube.com")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "exit" in query or "quit" in query:
            speak("Goodbye sir! Have a great day!")
            break
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif "open stack overflow" in query:
            speak("opening stack overflow")
            webbrowser.open("stackoverflow.com")
        elif "open github" in query:
            speak("opening github")
            webbrowser.open("github.com")   
        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")
        elif "open instagram" in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")
        elif "open twitter" in query:
            speak("opening twitter")
            webbrowser.open("twitter.com")  
        elif "open linkedin" in query:
            speak("opening linkedin")
            webbrowser.open("linkedin.com")
        elif "open whatsapp" in query:
            speak("opening whatsapp")
            webbrowser.open("web.whatsapp.com")
        elif "open amazon" in query:
            speak("opening amazon")
            webbrowser.open("amazon.com")
        elif "open flipkart" in query:
            speak("opening flipkart")
            webbrowser.open("flipkart.com")
        elif "open gmail" in query:
            speak("opening gmail")
            webbrowser.open("gmail.com")
        elif "open outlook" in query:
            speak("opening outlook")
            webbrowser.open("outlook.com")
        elif "open news" in query:
            speak("opening news")
            webbrowser.open("news.google.com")
        elif "open weather" in query:
            speak("opening weather")
            webbrowser.open("weather.com")
        elif "open calendar" in query:
            speak("opening calendar")
            webbrowser.open("calendar.google.com")
        elif "open drive" in query:
            speak("opening drive")
            webbrowser.open("drive.google.com")
        elif "open docs" in query:
            speak("opening docs")
            webbrowser.open("docs.google.com")
        elif "open sheets" in query:
            speak("opening sheets")
            webbrowser.open("sheets.google.com")
        elif "open slides" in query:
            speak("opening slides")
            webbrowser.open("slides.google.com")
        
        elif "play music" in query or "play songs" in query:
                music_dir = "/home/mojez-hasan/Music/"
                try:
                    # Get music files
                    songs = [os.path.join(music_dir, f) for f in os.listdir(music_dir) 
                            if f.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a'))]
                    
                    if not songs:
                        speak("No music files found in your Music folder")
                        continue
                        
                    selected_song = songs[0]  # Or use random.choice(songs) for random playback
                    
                    # Try different playback methods
                    players = [
                        ["xdg-open", selected_song],  # System default player
                        ["mpv", "--no-video", selected_song],  # Lightweight player
                        ["vlc", "--play-and-exit", selected_song],  # VLC with auto-close
                        ["pw-play", selected_song],  # PipeWire native player
                        ["ffplay", "-nodisp", "-autoexit", selected_song]  # FFmpeg player
                    ]
                    
                    for player in players:
                        try:
                            subprocess.Popen(player,
                                            stdout=subprocess.DEVNULL,
                                            stderr=subprocess.DEVNULL)
                            speak(f"Now playing {os.path.basename(selected_song)}")
                            break
                        except FileNotFoundError:
                            continue
                    else:
                        speak("Could not find any compatible music player")
                        
                except Exception as e:
                    print(f"Music playback error: {e}")
                    speak("Sorry, I couldn't play the music")


    
    

            
        
