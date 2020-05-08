import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os


birthdays = {"shaad":"3rd December", "samad": "19 april", "mom":"20 april", "papa":"11 may"}



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takecommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":

    wish()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("Asking wikipedia")
            print("asking wikipedia...")
            results = wikipedia.summary(query, sentences=3)
            # query = query.replace ("wikipedia", "")
            speak("According to wikipedia")
            print (results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        # elif 'open my website' or "open diastink" in query:
        #     webbrowser.open("diastink.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open python website' in query:
            webbrowser.open("python.org")

        elif "play song" in query:
            musicdir = 'C:\\Users\\Shaad\\Music\\arijeet singh hits'
            songs = os.listdir(musicdir)
            os.startfile(os.path.join(musicdir,songs[0]))

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {time}")
            print(time)

        elif "open code" in query:
            path = 'C:\\Users\\Shaad\Desktop\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe'
            os.startfile(path)

        elif "hi" in query:
            speak("Hi Mister Shad Sir.")


        elif "how are you" in query:
            speak("Yes Its Going Great. What about You")

        elif "i am fine" in query:
            speak("Ok. I will be happy if you too. You are my love and it can't last without You")

        elif "i am not fine" in query:
            speak("Sir You can share Your Thoughts Freely")

        elif "what is your name" in query:
            speak("I am jarvis and Sir. Shad is my master")

        elif "quit" in query:
            speak("Okay shad! I am Leaving. Call me When You need")
            quit()

        elif "play english songs" in query:
            musicdir = 'C:\\Users\\Shaad\\Music\\Hinglish'
            songs = os.listdir (musicdir)
            os.startfile (os.path.join (musicdir, songs[0]))

        elif "open NMDC website" in query:
            webbrowser.open("nmdc.com")


        # elif "no" in query:
        #     speak("Okay")

        elif "ok" in query:
            speak("Hmmmmmm")

        elif "thanks" in query:
            speak("It's My Happiness to do Work For you")

        elif "thank you" in query:
            speak("Ahh! Finally i am Appriciated for what I am Doing")


        elif "my birthday" in query:
            speak(f"Your Birthday is On")
            speak(birthdays["shaad"])


        elif "brother birthday" in query:
            speak(f"His Birthday is On")
            speak(birthdays["samad"])


        elif "mum birthday" in query:
            speak(f"Shad Your Beautiful Mother's Birthday is Comming soon On")
            speak(birthdays["mom"])


        elif "papa birthday" in query:
            speak(f"His Birthday is On")
            speak(birthdays["papa"])
        elif "you repeat" in query:
            pass