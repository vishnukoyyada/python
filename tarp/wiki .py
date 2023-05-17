import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")

    elif hour>=12 and hour<18:
        speak("good afternoon sir")

    else:
        speak("good evening")
    
    speak("i am jarvis sir how may i help you sir")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    
    except Exception as e:
       # print(e)

        print("say that again please...")
        return "none"
    return query


if _name_ == "_main_":
    wishme()
    while True:
        query = takecommand().lower()
        #executing wikipedia and stuff code
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open youtube' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("stackoverflow.com")