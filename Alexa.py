import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)
def speak (audio):
    engine.say(audio)
    engine.runAndWait()
def Wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello, I am Alexa. How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
          print("Recoganising....")
          query=r.recognize_google(audio,language='en-in')
          print("User Said : {}".format(query))
  
    except Exception as e:
         print(e)
         print("Sorry, Say that again please...")
         return "None"
    return query
if __name__ == "__main__":
    Wishme()
    while True :
        query= takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query=query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'gmail' in query:
            webbrowser.open("gmail.com")
        elif 'Google chrome' in query:
            webbrowser.open("Google chrome.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("My Highness the time is {}".format(strTime))

   
   