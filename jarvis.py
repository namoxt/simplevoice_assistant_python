import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir! jarvis here. How may I help you?")
    elif hour>=12 and hour<18:

        speak("good Afternoon sir! jarvis here. How may I help you? ")
    else: 
        speak("good evening sir! jarvis here. How may I help you?")


   # speak("Hello sir! Jarvis here. How may I help you?")     


def takeCommand():
    #it takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)

        print('say it again please....')
        return "None"


    return query


if __name__=="__main__":
    wishMe() 
    while True:
        query=takeCommand().lower()  #change the command to lower case
    
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1) #number of sentences to read from wikipedia
            speak('according to wikipedia')
           # print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'play music' in query:
            music_dir="C:\\Users\\pnamo\\Music\\Karan Aujla"#change the path to the folder where you keep music
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\pnamo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #modify the path if your vs code is in other folder
            os.startfile(codepath)
        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('gmail.com')
        elif 'the date' in query:
            today_date=datetime.date.today().strftime("%B %d %Y")
            #print(today_date)
            speak(f"sir the date is {today_date}")
        
          





 