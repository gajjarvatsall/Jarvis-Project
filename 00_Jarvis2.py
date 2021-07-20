
import pyttsx3
import wikipedia 
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import subprocess
import pyautogui


from wikipedia.wikipedia import page



engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=4 and hour<12:
        speak("Good Morning,Sir")
    elif hour>=12 and hour<17:
        speak("Good AfterNoon,Sir")
    else:
        speak("Good Evening,Sir")

    print('''HI I am Jarvis,The virtual artificial Intelligence and I am here to assist you with a variety of tasks as best I can,
    24hours a day,
    7 days a week,
    Importing all preferences form home interface''')
    
    speak('''HI I am Jarvis,The virtual artificial Intelligence and I am here to assist you with a variety of tasks as best I can
             24hours a day,
            7 days a week,
            Importing all preferences form home interface
            Systems are now fully operational''')
    print("*********** Systems are now fully operational ************")

def openFile(filename):
    if sys.platform == "win32" and "win64":
        os.startfile("filename")
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener,filename])

# def wik():
#     try:
#         page = wikipedia.page("Recommendation")
#     except wikipedia.exceptions.DisambiguationError as e:
#         print e.options



def takeCommand():
    # It take microphone input from the user and returns string output


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            reuslts = wikipedia.summary(query, sentences = 2 )
            speak("According to wikipedia")
            print(reuslts)
            speak(reuslts)
        
        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
        
        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
        
        elif 'open apple website' in query:
            webbrowser.open_new_tab("https://www.apple.com")
        
        elif 'open amazon' in query:
            webbrowser.open_new_tab("https://www.amazon.in")
        
        elif 'open filpkart' in query:
            webbrowser.open_new_tab("https://www.flipkart.com")
        
        elif 'open myntra' in query:
            webbrowser.open_new_tab("https://www.myntra.com")
        
        elif 'open meet' in query:
            webbrowser.open_new_tab("https://meet.google.com")
        
        elif 'play bhajan' in query:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=5-Xoh7jKVo8")
        
        # elif 'Whatsapp' in query:
        #     webbrowser.open_new_tab("https://web.whatsapp.com")
        
        elif 'code' in query:
            codepath = "/Users/vatsalgajjar/Downloads/Visual Studio Code.app"
            openFile(codepath)
        
        elif 'vlc' in query:
            codepath = "/Applications/VLC.app"
            openFile(codepath)
        
        elif 'notes' in query:
            codepath = "/System/Applications/Notes.app"
            openFile(codepath)
        
        elif 'calendar' in query:
            codepath = "/System/Applications/Calendar.app"
            openFile(codepath)
        
        elif 'whatsapp' in query:
            codepath = "/Applications/WhatsApp.app"
            openFile(codepath)
        
        elif 'zoom' in query:
            codepath = "/Applications/zoom.us.app"
            openFile(codepath)
        
        elif 'app store' in query:
            codepath = "/System/Applications/App Store.app"
            openFile(codepath)
        
        elif 'system preferences' in query:
            codepath = "/System/Applications/System Preferences.app"
            openFile(codepath)
        
        elif 'calculator' in query:
            codepath = "/System/Applications/Calculator.app"
            openFile(codepath)
        
        elif 'webex' in query:
            codepath = "/Applications/Cisco Webex Meetings.app"
            openFile(codepath)
        
        elif 'discord' in query:
            codepath = "/Applications/Discord.app"
            openFile(codepath)
        
        elif 'reminder' in query:
            codepath = "/System/Applications/Reminders.app"
            openFile(codepath)
        
        elif 'screenshot' in query:
            from subprocess import call
            call(["screencapture", "screenshot.jpg"])
            speak("Screenshot is taken")
        
        elif 'search' in query:
            speak("What do you want me to search for (please type) ?")
            search_term = input()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.open_new_tab(search_url)
            speak(f"Here are the results for the search term: {search_term}")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'play music' in query:
            from playsound import playsound
            playsound('/Users/vatsalgajjar/Desktop/play2.mp3')
        
        elif 'stop music' in query:
            os.close(playsound)
        #     music_dir = ''
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[1]))
        
        elif 'close' in query:
            speak("Signing off,Jarvis")
            exit()
