import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
#import wolframalpha
import json
import requests
from os import environ, path
import subprocess
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import time

if (os.environ.get('environment')=="pi"):
    from helper.Server.Led import *
    led=Led()

#r = sr.Recognizer()
#source = sr.Microphone()

active = False

import time

keywords = [("cat", 1), ("hey cat", 1), ]


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       
        
        #try:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio=r.listen(source)        
        print("processand...")


        statement=r.recognize_sphinx(audio,language='en-US', keyword_entries=[("hey cat", 1), ("cat", 1), ])
        print(f"user said:{statement}\n")
        return statement
        #except:
        #    print("error ")
        #    return False

#speak("Meow")
#speak("Meow")
#wishMe()





def callback(recognizer, audio):  # this is called from the background thread
    print ("entrou no callback")
    if active==False:
        try:
            #speech_as_text=recognizer.recognize_google(audio)
            speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
            print(speech_as_text)

            # Look for your "Ok Google" keyword in speech_as_text
            if "cat" in speech_as_text :
                recognize_main()

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
    else:
        print ("Ops Active")



def speak(text):
    print("text")
    command='espeak "'+text+'"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    #time.sleep(0.5)
    #os.system('espeak "'+text+'"')

def recognize_main():
    
    # engine=pyttsx3.init("sapi5")
    # voices = engine.getProperty('voices')
    # voices=engine.getProperty('voices')
    # engine.setProperty('voice','com.apple.speech.synthesis.voice.Alex')
    # engine.setProperty("rate", 178)


    
    if (os.environ.get('environment')=="pi"):
        led.colorWipe(led.strip, Color(0, 255, 0))
    speak("Meow")
    global active
    if active == False:
        active=True
        with sr.Microphone() as source:
            print("listening")
            audio = sr.Recognizer().listen(source, timeout=5)
            print("processing")
            statement=r.recognize_google(audio)
            print(f"user said:{statement}\n")
            statement = statement.lower()

            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('I am your personal assistant,Good bye')
                print('your personal assistant G-one is shutting down,Good bye')
                return True



            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(5)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif "weather" in statement:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                    print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))

                else:
                    speak(" City Not Found ")



            elif 'time' in statement:
                print ("telling the time")
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                #speak("I was built by Mirthula")
                speak(f"the time is {strTime}")
                active = False
                print ("saindo...")
                return True

            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                    'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                    'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Mirthula")
                print("I was built by Mirthula")

            elif "open stackoverflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")

            elif 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

            # elif "camera" in statement or "take a photo" in statement:
            #     ec.capture(0,"robo camera","img.jpg")

            elif 'search'  in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)

            # elif 'ask' in statement:
            #     speak('I can answer to computational and geographical questions and what question do you want to ask now')
            #     question=takeCommand()
            #     app_id="R2K75H-7ELALHR35X"
            #     client = wolframalpha.Client('R2K75H-7ELALHR35X')
            #     res = client.query(question)
            #     answer = next(res.results).text
            #     speak(answer)
            #     print(answer)


            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
            else:
                print("Soory, I can not understand")
                speak("I can not understand, meow")
            # except:
            #     print("error processing")
            #     speak("I can not understand, meow")
            #     active = False
            #     return True
    active = False
    return False
            # interpret the user's words however you normally interpret the

def start_recognizer():
    
    #r = sr.Recognizer()
    #source = sr.Microphone()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
    print("listening")
    #r.energy_threshold = 200
    r.pause_threshold = 0.5
    r.listen_in_background(source, callback)
    time.sleep(1000000)


source = sr.Microphone()
r = sr.Recognizer()
if __name__ == '__main__':
    if (os.environ.get('environment')=="pi"):
        led.colorWipe(led.strip, Color(0, 255, 0))
    start_recognizer()


            

