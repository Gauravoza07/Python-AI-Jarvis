import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<1:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
        
    speak("I am jarvis Please tell me how may I help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")
        return "None" 
    return query

if __name__=="__main__" :
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "How are you" in query:
            speak("I'm fine thanks for asking")

            