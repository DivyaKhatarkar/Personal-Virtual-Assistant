import pyttsx3    # for speeking
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import imdb
import translators as ts
from gtts import gTTS
import playsound
import requests
from bs4 import BeautifulSoup
import pywhatkit as kit 
import pywhatkit
from plyer import notification
from pygame import mixer
import speedtest
import random
import pyjokes
import randfacts
import cv2 
import sys 
import time 
from time import sleep
import operator
import wolframalpha
from datetime import timedelta


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak(" The day is " + day_of_the_week)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon !")   

    else:
        speak("Good Evening !")  

    speak("I am jerry Mam. Please tell me how may I help you")


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
 
    try:
 
        said = r.recognize_google(audio)
        print(said)

    except:
        speak("Didn't get that")
    return said.lower()

for i in range(3):
    speak("Enter Password to open Jerry")
    a = input("Enter Password to open Jerry :- ")
    pw = "Jerry53"
    if (a==pw):
        print("WELCOME MAM")
        speak("WELCOME MAM.")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
        speak("Try Again")

from INTRO import play_gif
play_gif

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")

def search_movie():

    moviesdb = imdb.IMDb()
    text = get_audio()
    movies = moviesdb.search_movie(text)

    speak("Searching for " + text)
    if len(movies) == 0:
        speak("No result found")
    else:

        speak("I found these:")

        for movie in movies:

            title = movie['title']
            year = movie['year']
            speak(f'{title}-{year}')

            info = movie.getID()
            movie = moviesdb.get_movie(info)

            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            cast = movie.get('cast')
            topActors = 5
            for actor in cast[:topActors]:
                print("{0} as {1}".format(actor['name'], actor.currentRole ))
            plot = movie['plot outline']

            if year < int(datetime.datetime.now().strftime("%Y")):
                print(f'{title}was released in {year} has IMDB rating of {rating}. The plot summary of movie is{plot}')
                speak(f'{title}was released in {year} has IMDB rating of {rating}.   The plot summary of movie is{plot}      The casts of the movie are  ')
                topActors = 5
                for actor in cast[:topActors]:
                   speak("{0} as {1}".format(actor['name'], actor.currentRole ))
                break

            else:
                speak(f'{title}will release in {year} has IMDB rating of {rating}.The plot summary of movie is{plot}')
                print(f'{title}will release in {year} has IMDB rating of {rating}.The plot summary of movie is{plot}')
                break

def WolfRamAlpha(query):
    apikey = "57GP3H-XXUGVJ3HER"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jerry","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")
        
def sendMessage():
    from datetime import datetime, timedelta
    import pywhatkit
    
    now = datetime.now()
    strTime = now.hour
    update = now.minute + 1  # Adding 1 minute to the current time

    if update >= 59:
        strTime = (strTime + 1) % 24  # Increment hour if minute overflows
        update = 0

    speak("Who do you want to message")
    a = int(input('''madhuri - 1: khushi - 2: '''))
    
    if a == 1:
        speak("What's the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+917758081798", message, time_hour=strTime, time_min=update)
    elif a == 2:
        speak("What's the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+918830599294", message, time_hour=strTime, time_min=update)

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing")    
        query = r.recognize_google(audio, language='en-in')

        print(f"User said: {query}\n")
        speak("you said")
        speak({query})

    except Exception as e:
        #print(e)    
        print("Say that again please...")
        speak("say that again please")  
        return "None"
    return query

if __name__=="__main__" :
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'task view' in query: 
            pyautogui.hotkey('super', 'tab')
 
        elif 'open file explorer' in query: 
            pyautogui.hotkey('super', 'e')

        elif 'open setting' in query: 
            pyautogui.hotkey('super', 'i')

        elif 'lock the system' in query: 
            pyautogui.hotkey('super', 'l')

        elif "write a note" in query:
            speak("What should i write, mam")
            note = takeCommand()
            file = open('note.txt', 'w')
            speak("mam, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r") 
            print(file.read())

        elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jerry","")
                    query = query.replace("translate","")
                    translategl(query)

        elif 'jerry' in query:
             speak('Yes. How may i help you mam.')
            
        elif 'open youtube' in query:
            speak("What should i search!")
            qry = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={qry}")
            speak("Done, mam")

        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'maximize this window' in query: 
            pyautogui.hotkey('alt', 'space') 
            time.sleep(1) 
            pyautogui.press('x') 

        elif 'minimise this window' in query: 
            pyautogui.hotkey('alt', 'space') 
            time.sleep(1) 
            pyautogui.press('n')

        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)

        elif 'open history' in query: 
            pyautogui.hotkey('ctrl', 'h') 

        elif 'open downloads' in query: 
            pyautogui.hotkey('ctrl', 'j') 

        elif 'previous tab' in query: 
            pyautogui.hotkey('ctrl', 'shift', 'tab') 

        elif 'next tab' in query: 
            pyautogui.hotkey('ctrl', 'tab') 

        elif 'close tab' in query: 
            pyautogui.hotkey('ctrl', 'w') 

        elif 'clear browsing history' in query: 
            pyautogui.hotkey('ctrl', 'shift', 'delete') 

        elif 'refresh window' in query: 
            pyautogui.hotkey('ctrl', 'r')
 
        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")   

        elif "schedule my day" in query:
            tasks = [] 
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = takeCommand().lower()
            if "yes" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                speak("Enter the no. of tasks :- ")
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()

        elif "switch between open app" in query:
            pyautogui.hotkey('alt', 'Tab') 

        elif "show my schedule" in query:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("notification.wav")
            mixer.music.play()
            notification.notify(
                title = "My schedule :-",
                message = content,
                timeout = 15
            )

        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done, mam")

        elif "calculate" in query:

            query = query.replace("calculate","")
            query = query.replace("jerry","")
            Calc(query)

        # elif 'play music' in query:
        #       music_dir = "C:\\Users\\HP\\Music\\Baby_192(PaglaSongs).mp3"
        #       import subprocess, sys

        #       opener = "open" if sys.platform == "darwin" else "xdg-open"
        #       subprocess.call([opener, music_dir])

        #      songs = os.listdir(music_dir)
        #      print(songs)    
        #      os.startfile(os.path.join(music_dir, songs[0]))                
        
        elif 'temperature' in query:
              search = 'temperature in nagpur'
              url = f"https://www.google.com/search?q={search}" 
              r = requests.get(url) 
              data = BeautifulSoup(r.text,"html.parser")  
              temp = data.find("div", class_= "BNeawe").text
              speak(f"current{search} is {temp}")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")

        elif 'open song' in query:
            codePath = "C:\\Users\\HP\\Music\\Baby_192(PaglaSongs).mp3"
            os.startfile(codePath)

        elif 'open vs code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'close vs code' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'open word' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(codePath)

        elif 'close word' in query:
            os.system("taskkill /f /im WINWORD.EXE")


        elif 'open powerpoint' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(codePath)


        elif 'close powerpoint' in query:
            os.system("taskkill /f /im POWERPNT.EXE")


        elif 'open excel' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(codePath)

        elif 'close excel' in query:
            os.system("taskkill /f /im EXCEL.EXE")


        elif 'open command prompt' in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(codePath)

        elif 'close command prompt' in query:
            os.system("taskkill /f /im cmd.exe")


        elif "day" in query:
            tellDay()


        elif "news" in query:
            from NewsRead import latestnews
            latestnews()

        elif "open" in query:  
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")   

        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("jerry","")
            speak("you told me to remember that"+rememberMessage)
            remember = open("remember.txt","w")
            remember.write(rememberMessage)
            remember.close()

        elif "what do you remember" in query:
             remember = open("remember.txt","r")
             speak("you told me"+remember.read())

        elif "refresh" in query:
                pyautogui.moveTo(1551,55, 2)
                pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
                pyautogui.moveTo(1620,667, 1)
                pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
        
        elif "scroll down" in query:
                pyautogui.scroll(100000)

        elif "scroll up" in query:
                pyautogui.scroll(-100000)
    
        elif "volume up" in query:
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
 
        elif "volume down" in query:
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
        
        elif "mute" in query:
                    pyautogui.press("volumemute")

        elif "what is my ip address" in query: 
            speak("Checking mam") 
            try: 
                ipAdd = requests.get('https://api.ipify.org').text 
                print(ipAdd) 
                speak("your ip adress is") 
                speak(ipAdd) 
            except Exception as e: 
                speak("network is weak, please try again some time later")

        elif "who are you" in query:
                    print('My Name Is jerry')
                    speak('My Name Is jerry')
                    print('I can Do Everything that my creator programmed me to do')
                    speak('I can Do Everything that my creator programmed me to do')
                    
        elif "who created you" in query:
                    print('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
                    speak('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')

        elif "movie detail" in query:
            speak("Say the movie name")
            search_movie()

        elif "what is your name" in query:
            speak("I am Jerry. Your Virtual Assistant")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "play a game" in query:
            speak("Lets Play STONE PAPER SCISSORS !!")
            print("LETS PLAYYYYYYYYYYYYYY")
            i = 0
            Me_score = 0
            Com_score = 0
            while(i<5):
                choose = ("stone","paper","scissors") 
                com_choose = random.choice(choose)
                query = takeCommand().lower()
                if (query == "stone"):
                    if (com_choose == "stone"):
                        speak("STONE")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    elif (com_choose == "paper"):
                        speak("paper")
                        speak("points go to computer")
                        Com_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    else:
                        speak("Scissors")
                        Me_score += 1
                        speak("points go to you")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                elif (query == "tone"):
                    if (com_choose == "stone"):
                        speak("STONE")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    elif (com_choose == "paper"):
                        speak("paper")
                        speak("points go to computer")
                        Com_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    else:
                        speak("Scissors")
                        Me_score += 1
                        speak("points go to you")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                elif (query == "paper" ):
                    if (com_choose == "stone"):
                        speak("STONE")
                        Me_score += 1
                        speak("points go to you")
                        print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

                    elif (com_choose == "paper"):
                        speak("paper")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    else:
                        speak("Scissors")
                        Com_score += 1
                        speak("points go to computer")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                elif (query == "scissors" or query == "scissor"):
                    if (com_choose == "stone"):
                        speak("STONE")
                        Com_score += 1
                        speak("points go to computer")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    elif (com_choose == "paper"):
                        speak("paper")
                        Me_score += 1
                        speak("points go to you")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    else:
                        speak("Scissors")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                i += 1
    
            print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")
            speak("Final Score  your score")
            speak(Me_score)
            speak("computer score")
            speak(Com_score)
            if(Com_score > Me_score):
                speak("computer wins the game")
            elif(Com_score < Me_score):
                speak("you wins the game")
            else:
                 speak("There is a tie ")

        elif "pause" in query:
             pyautogui.press("k")

        elif "play" in query:
             pyautogui.press("k")

        elif "mute the video" in query:
             pyautogui.press("m")

        elif "unmute the video" in query:
             pyautogui.press("m")

        elif "minimise the screen" in query:
             pyautogui.press("i")

        elif "maximise the screen" in query:
             pyautogui.press("i")

        elif "minimize the screen" in query:
             pyautogui.press("i")

        elif "maximize the screen" in query:
             pyautogui.press("i")

        elif "10 second backward" in query:
             pyautogui.press("j")

        elif "10 second forward" in query:
             pyautogui.press("l")

        elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE PLEASE")
                    pyautogui.press("enter")

        elif "camera" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE PLEASE")
                    pyautogui.press("enter")

        elif "screenshot" in query:
                     im = pyautogui.screenshot()
                     speak("Tell me the file name")
                     query = takeCommand().lower()
                     im.save(query + ".jpg")
                     speak("screenshot saved mam")

        elif "whatsapp" in query:
            sendMessage()

        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            elif shutdown == "no":
                 continue
            
        elif "sleep the system" in query:
            speak("Are You sure you want to sleep")
            shutdown = input("Do you wish to sleep your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /h")
            elif shutdown == "no":
                 continue
            
        elif "restart the system" in query:
            speak("Are You sure you want to restart")
            shutdown = input("Do you wish to restart your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /r /t 1")
            elif shutdown == "no":
                 continue
            
        elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #bytes - Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

        elif "facts" or "another one" in query:
             x = randfacts.get_Fact()
             print(x)
             speak("Did you know that, " + x)

        elif "quit" in query:
             speak( "Now i will stop.    It was a pleasure to help you.     Have a nice day.    Thank you")
             break
        
  
