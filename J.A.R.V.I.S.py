import datetime
import os
import webbrowser
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import smtplib
import pyjokes

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Friday. Please tell me how may i help you? ")


# it takes audio of an user as an input and return string as output
def TakeCommand():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.pause_threshold = 1
        audio = recog.listen(source)

    try:
        print("Recognizing...")
        query = recog.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e) this will print the exception
        print("Say that again Please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP ("smtp.gmail.com",465)
    server.ehlo()
    server.starttls()
    server.login("Senders Email", "Password")
    server.sendmail("Senders Email",to, content)
    server.close()

if __name__ == "__main__":
    while True:
        Query = TakeCommand().lower()
        if "wikipedia" in Query:
            speak("Searching Wikipedia...")
            Query = Query.replace("wikipedia", "")
            result = wikipedia.summary(Query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in Query:
            webbrowser.open("https://www.youtube.com")

        elif "stop jarvis" in Query:
            speak("Quiting... Bye Sir have a Good Day!")
            break

        elif "hello" in Query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Good morning Sir")

            elif hour >= 12 and hour < 18:
                speak("Good Afternoon Sir")

            else:
                speak("Good Evening Sir")

            speak("Please tell me how may i help you? ")
        elif "introduction" in Query:
            speak("I am Friday 2.0, i was created by Sir Unkoosh")

        elif "search" in Query:
            Query = Query.replace("search", "")
            speak("This is what I Found on The Web!")
            pywhatkit.search(Query)

            try:
                result = wikipedia.summary(Query,2)
                print(result)
                speak(result)

            except:
                print("No speakable data is available!")
                speak("No speakable data is available!")


        elif "open google" in Query:
            webbrowser.open("https://www.google.com")

        elif "play" in Query:
            song = Query.replace("play", "")
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif "do you have heart" in Query:
            speak("No, I don't have heart, if you have extra Please give me one Sir! ")

        elif "open blogger" in Query:
            webbrowser.open("https://www.blogger.com")

        elif "tell me a joke" in Query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)


        elif "open WhatsApp" in Query:
            webbrowser.open("https://web.whatsapp.com")

        elif "my music" in Query:
            music = "D:\\My music"
            song = os.listdir(music)
            print(song)
            os.startfile(os.path.join(music, song[0]))

        elif "time" in Query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Sir the time is {strTime}")
            speak(f"Sir the time is {strTime}")

        elif "send email" in Query:
            try:
                speak("What would I say?")
                content = TakeCommand()
                to = "Reciever Email"
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry Sir! I am not able to send this email")
                speak("Sorry Sir! I am not able to send this email")



