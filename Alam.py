import pyttsx3
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarm.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarm.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
        timeset = str(time)
        timenow = timeset.replace("jerry", "")
        timenow = timenow.replace("set an alarm","")
        timenow = timenow.replace(" and ",":")
        Alaramtime = str(timenow)
        print(Alaramtime)
        while True:
            currenttime = datetime.datetime.now().strftime("%H:%M:%S")        
            if currenttime == Alaramtime:
                speak("Alarm ringing, mam")
                codePath = "C:\\Users\\HP\\Music\\Baby_192(PaglaSongs).mp3"
                os.startfile(codePath)
            elif currenttime + "00:00:30" == Alaramtime:
                 exit()
ring(time)
