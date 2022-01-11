import pyttsx3 as p
import speech_recognition as sr
from wikipedia import *
from youtube import *
from weather import *
import pyjokes
import datetime
import os
import webbrowser
import time
import requests

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def get_audio():
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            print("Listening...")

            # recording the audio using speech recognition
            audio = rObject.listen(source, phrase_time_limit=5)
        print("Okay.")  # limit 5 secs

        try:

            text = rObject.recognize_google(audio, language='en-US')
            print("You : ", text2)
            return text2

        except:
            speak("Could not understand your audio, PLease try again !")
            return 0

def tellDay():
      
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():

    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes") 

def speak(text: object) -> object:
    engine.say(text)
    engine.runAndWait()


speak("Hello Riya, I am your voice assistant Micky, How are you?")

r = sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

    if "what" and "about" and "you" in text:
        speak("i am also having a good day Riya")
        print("i am also having a good day Riya")
    speak("What can i do for you??")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)


    if "information" in text2:
        speak("sure mam, you need information related to which topic?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening...")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
        speak("searching {} in wikipedia".format(infor))
        print("searching {} in wikipedia".format(infor))

        assist = infow()
        assist.get_info(infor)
        

    elif "open geeksforgeeks" in text2:
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")
            
    elif "which day it is" in text2:
            tellDay()
    
    elif "tell me the time" in text2:
            tellTime()

    elif "play" and "song" in text2:
        speak("you want me to play which video??")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
        print("Playing {} on youtube".format(vid))
        speak("Playing {} on youtube".format(vid))
        assist = music()
        assist.play(vid)

    elif 'is love' in text2:
            speak("It is 7th sense that destroy all other senses")
        

    elif 'exit' in text2:
            speak("sure mam,")
            speak("Thanks for giving me your time")
            print("Thanks for giving me your time")
            exit()
 
    elif "joke" in text2:
            speak("sure mam,")
            speak(pyjokes.get_joke())
    

    elif "temperature" in text2:
            speak("Sure mam,")
            speak("Temperature in azamgarh is" + str(temp()) +
          " degree celsius" + "and with" + str(des()))

    elif "who made you" in text2 or "who created you" in text2:
        speak("I have been created by Riya Jaiswal")
        print("I have been created by Riya Jaiswal")

    elif 'open google' in text2:
        speak("sure mam,")
        speak("Here you go to Google\n")
        print("Here you go to Google")
        webbrowser.open("google.com")



    

