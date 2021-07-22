import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia    
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
            speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Please tell me how are you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 800
        audio = r.listen(source)

    try:
        print("recognizing...")
        query= r.recognize_google(audio, language="en-in")
        print("User said:", query)
    
    except Exception as e:
        #print(e)

        print("Say that again please...")
        return"None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nainamajumdar1459@gmail.com','Naina@1459')
    server.sendmail('nainamajumdar1459@gmail.com',to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open email' in query:
            webbrowser.open("gmail.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open code' in query:
            codepath = "C:\\Users\\NAINA MAJUMDAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send a mail' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "satyajitmajumdar20@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! I am not able to send this mail")