import datetime
import subprocess
import speech_recognition as sr
import time
import wikipedia
import webbrowser
import os
import random  # Make sure this import is at the top if you're using random selection
import sys
    # unwanted warning supressers
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


def speak(audio):
    subprocess.call(["spd-say", audio])

def wishMe():
    hour = datetime.datetime.now().hour  # Get the current hour
    # print(f"Current hour: {hour}")  # Debugging: Print the current hour

    if hour >= 0 and hour < 12:
        print("Executing morning greeting...")  # Debugging
        speak("Good morning user!")
        time.sleep(1)
    elif hour >= 12 and hour < 18:
        print("Executing afternoon greeting...")  # Debugging
        speak("Good afternoon user!")
        time.sleep(1)
    else:
        print("Executing evening greeting...")  # Debugging
        speak("Good evening user!")
        time.sleep(1)

def play_jarvis_boot_sound():
    sound_path = os.path.expanduser("/home/mojez-hasan/project_J.A.R.V.I.S/boot.mp3")
    
    if os.path.exists(sound_path):
        try:
            # Try PipeWire-native player first
            subprocess.Popen(["pw-play", sound_path],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        except:
            try:
                # Fallback to other players
                subprocess.Popen(["mpv", "--no-video", sound_path],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
            except:
                pass  # Silent fallback if no players available
def play_jarvis_shutdown_sound():
    sound_path = os.path.expanduser("/home/mojez-hasan/project_J.A.R.V.I.S/shutdown.mp3")
    print(r"""
     ██╗  █████╗  ██████╗  ██╗   ██╗ ██╗  ██████╗
     ██║ ██╔══██╗ ██╔══██╗ ██║   ██║ ██╗ ██╔════╝
     ██║ ███████║ ██████╔╝ ██║   ██║ ██╗ ╚█████╗ 
██   ██║ ██╔══██║ ██╔══██╗ ██║   ██║ ██╗  ╚═══██╗
╚█████╔╝ ██║  ██║ ██║  ██║ ╚██████╔╝ ██╗ ██████╔╝
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
    """)
    
    if os.path.exists(sound_path):
        try:
            # Try PipeWire-native player first
            subprocess.Popen(["pw-play", sound_path],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        except:
            try:
                # Fallback to other players
                subprocess.Popen(["mpv", "--no-video", sound_path],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
            except:
                pass  # Silent fallback if no players available

def jarvis_boot_sequence():
    print(r"""
     ██╗  █████╗  ██████╗  ██╗   ██╗ ██╗  ██████╗
     ██║ ██╔══██╗ ██╔══██╗ ██║   ██║ ██╗ ██╔════╝
     ██║ ███████║ ██████╔╝ ██║   ██║ ██╗ ╚█████╗ 
██   ██║ ██╔══██║ ██╔══██╗ ██║   ██║ ██╗  ╚═══██╗
╚█████╔╝ ██║  ██║ ██║  ██║ ╚██████╔╝ ██╗ ██████╔╝
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
    """)
    
    play_jarvis_boot_sound()
    time.sleep(4)
    speak("Initializing systems")
    print("Initializing systems")
    time.sleep(2)
    speak("Diagnostics complete")
    print("Diagnostics complete")
    time.sleep(2)
    speak("All systems operational")
    print("All systems operational")
    time.sleep(2)

def biometric_authentication():
    speak("please speak up for biometric authentication")
    if takeCommand().lower() == "hello jarvis":
        return 1
    else:
        speak("authentication failed")
        return 0
    
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
    time.sleep(1)
    while True:
        key = biometric_authentication()
        if key == 1:
            speak("Authentication successful")
            print("Authentication successful")
            time.sleep(3)
            speak("Initializing Jarvis")
            print("Initializing Jarvis")
            time.sleep(3)
            jarvis_boot_sequence()
            time.sleep(2)
            speak("welcome back sir")
            time.sleep(2)
            speak("jarvis at your service.")
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
                elif "exit" in query or "quit" in query or "close" in query or "shutdown" in query or "stop" in query or "terminate" in query or "power off" in query or "turn off" in query:
                    speak("shutting down")
                    play_jarvis_shutdown_sound()
                    hour = datetime.datetime.now().hour
                    if hour >= 0 and hour < 18:
                        speak("Goodbye sir! Have a great day!")
                    else:
                        speak("Goodbye sir! Have a great sleep!")
                    print("Shutting down...")
                    sys.exit(0)

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
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"The time is {strTime}")
                    speak(f"Sir, the time is {strTime}")
                elif "date" in query:
                    strDate = datetime.datetime.now().strftime("%Y-%m-%d")
                    print(f"The date is {strDate}")
                    speak(f"Sir, the date is {strDate}")
                elif "search" in query:
                    sub_query = query.replace("search", "").strip()
                    speak(f"Searching for {sub_query}")
                    webbrowser.open(f"https://www.google.com/search?q={sub_query}")
                elif "open notepad" in query:
                    speak("Opening Notepad")
                    subprocess.Popen(["gedit"])
                elif "open calculator" in query:    
                    speak("Opening Calculator")
                    subprocess.Popen(["gnome-calculator"])
                elif "open terminal" in query:
                    speak("Opening Terminal")
                    subprocess.Popen(["gnome-terminal"])
                elif "open file manager" in query:
                    speak("Opening File Manager")
                    subprocess.Popen(["nautilus"])
                elif "open settings" in query:
                    speak("Opening Settings")
                    subprocess.Popen(["gnome-control-center"])
                elif "open camera" in query:
                    speak("Opening Camera")
                    subprocess.Popen(["cheese"])
                elif "open code" in query:
                    speak("Opening Visual Studio Code")
                    subprocess.Popen(["code"])
                elif "open browser" in query:
                    speak("Opening Browser")
                    subprocess.Popen(["firefox"])
                elif "open video" in query:
                    speak("Opening Video")
                    subprocess.Popen(["vlc"])
                elif "open photos" in query:
                    speak("Opening Photos")
                    subprocess.Popen(["eog"])
                elif "open pdf" in query:
                    speak("Opening PDF")
                    subprocess.Popen(["evince"])
                elif "open word" in query:
                    speak("Opening Word")
                    subprocess.Popen(["libreoffice", "--writer"])
                elif "open excel" in query:   
                    speak("Opening Excel")
                    subprocess.Popen(["libreoffice", "--calc"])
                elif "open powerpoint" in query:
                    speak("Opening PowerPoint")
                    subprocess.Popen(["libreoffice", "--impress"])
                elif "open browser" in query:
                    speak("Opening Browser")
                    subprocess.Popen(["firefox"])
                elif "open email" in query:
                    speak("Opening Email")
                    subprocess.Popen(["thunderbird"])
                elif "open whatsapp" in query:
                    speak("Opening WhatsApp")
                    subprocess.Popen(["whatsapp"])
                elif "open telegram" in query:
                    speak("Opening Telegram")
                    subprocess.Popen(["telegram-desktop"])
                elif "open discord" in query:
                    speak("Opening Discord")
                    subprocess.Popen(["discord"])
                elif "open skype" in query:
                    speak("Opening Skype")
                    subprocess.Popen(["skypeforlinux"])
                elif "open zoom" in query:
                    speak("Opening Zoom")
                    subprocess.Popen(["zoom"])
                elif "open slack" in query:
                    speak("Opening Slack")
                    subprocess.Popen(["slack"])
                elif "open teams" in query:
                    speak("Opening Microsoft Teams")
                    subprocess.Popen(["teams"])
                elif "open spotify" in query:
                    speak("Opening Spotify")
                    subprocess.Popen(["spotify"])
                elif "open youtube music" in query:
                    speak("Opening YouTube Music")
                    subprocess.Popen(["chromium", "https://music.youtube.com"])
                elif "open apple music" in query:
                    speak("Opening Apple Music")
                    subprocess.Popen(["chromium", "https://music.apple.com"])
                elif "open soundcloud" in query:
                    speak("Opening SoundCloud")
                    subprocess.Popen(["chromium", "https://soundcloud.com"])
                elif "open pandora" in query:
                    speak("Opening Pandora")
                    subprocess.Popen(["chromium", "https://www.pandora.com"])
                elif "open deezer" in query:
                    speak("Opening Deezer")
                    subprocess.Popen(["chromium", "https://www.deezer.com"])
                elif "open tiktok" in query:
                    speak("Opening TikTok")
                    subprocess.Popen(["chromium", "https://www.tiktok.com"])
                elif "open snapchat" in query:
                    speak("Opening Snapchat")
                    subprocess.Popen(["chromium", "https://www.snapchat.com"])
                elif "open pinterest" in query:
                    speak("Opening Pinterest")
                    subprocess.Popen(["chromium", "https://www.pinterest.com"])
                elif "open reddit" in query:
                    speak("Opening Reddit")
                    subprocess.Popen(["chromium", "https://www.reddit.com"])
                elif "open quora" in query:
                    speak("Opening Quora")
                    subprocess.Popen(["chromium", "https://www.quora.com"])
                elif "open medium" in query:
                    speak("Opening Medium")
                    subprocess.Popen(["chromium", "https://www.medium.com"])
                elif "open stack exchange" in query:
                    speak("Opening Stack Exchange")
                    subprocess.Popen(["chromium", "https://stackexchange.com"])
                elif "open udemy" in query:
                    speak("Opening Udemy")
                    subprocess.Popen(["chromium", "https://www.udemy.com"])
                elif "open coursera" in query:
                    speak("Opening Coursera")
                    subprocess.Popen(["chromium", "https://www.coursera.org"])
                elif "open edx" in query:
                    speak("Opening edX")
                    subprocess.Popen(["chromium", "https://www.edx.org"])
                elif "open khan academy" in query:
                    speak("Opening Khan Academy")
                    subprocess.Popen(["chromium", "https://www.khanacademy.org"])
                elif "what's up" in query or "how are you" in query or "how are you doing" in query:
                    speak("I am doing great, thank you for asking! How can I assist you today?")
                elif "tell me a joke" in query or "make me laugh" in query:
                    jokes = [
                        "Why don't scientists trust atoms? Because they make up everything!",
                        "Why did the scarecrow win an award? Because he was outstanding in his field!",
                        "Why don't skeletons fight each other? They don't have the guts!",
                        "What do you call fake spaghetti? An impasta!",
                        "Why did the bicycle fall over? Because it was two-tired!"
                    ]
                    joke = random.choice(jokes)
                    print(joke)
                    speak(joke)
                elif "tell me something interesting" in query or "tell me a fact" in query:
                    facts = [
                        "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible.",
                        "Bananas are berries, but strawberries aren't! Botanically speaking, bananas are classified as berries, while strawberries are not.",
                        "Octopuses have three hearts! Two pump blood to the gills, while one pumps it to the rest of the body.",
                        "A group of flamingos is called a 'flamboyance'.",
                        "Wombat poop is cube-shaped! This unique shape prevents it from rolling away and helps mark their territory."
                    ]
                    fact = random.choice(facts)
                    print(fact)
                    speak(fact)
                elif "tell me a riddle" in query or "give me a riddle" in query:
                    riddles = [
                        "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? (Answer: An echo)",
                        "I have keys but open no locks. I have space but no room. You can enter, but you can't go outside. What am I? (Answer: A keyboard)",
                        "What has to be broken before you can use it? (Answer: An egg)",
                        "I can fly without wings. I can cry without eyes. Whenever I go, darkness flies. What am I? (Answer: A cloud)",
                        "The more you take, the more you leave behind. What am I? (Answer: Footsteps)",
                        "What has a heart that doesn't beat? (Answer: An artichoke)"
                    ]
                    riddle = random.choice(riddles)
                    print(riddle)
                    speak(riddle)
                elif "tell me a quote" in query or "give me a quote" in query:
                    quotes = [
                        "The only way to do great work is to love what you do. - Steve Jobs",
                        "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
                        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
                        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston S. Churchill",
                        "You miss 100% of the shots you don't take. - Wayne Gretzky"
                    ]
                    quote = random.choice(quotes)
                    print(quote)
                    speak(quote)
                elif "introduce yourself" in query or "who are you" in query:
                    speak(f"I am Jarvis, an A. I. assistant trained by my master mojez hasan. I can help you with various tasks like searching the web, telling jokes, and providing information. {time.sleep(0.8)}my processes are linux based. i am written in python3 language .{time.sleep(1)} i may not be a perfect example of artificial intelligence, but I am always learning and improving. How can I assist you today?")
                elif "thanks" in query or "thank you" in query or "thank you very much" in query or "thanks a lot" in query or "thank you so much" in query or "nice work" in query or "good job" in query or "well done" in query or "great work" in query:
                    speak("You're welcome! I'm glad I could help you. If you need anything else, just let me know.") 
                    # speak("You're welcome! If you need anything else, just let me know.")
                elif "love you" in query or "i love you" in query or "i like you" in query or "you are awesome" in query or "you are great" in query or "you are amazing" in query:
                    speak("I appreciate your kind words! I'm here to assist you. If you have any questions or need help, just ask.")
