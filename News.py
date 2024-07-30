import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
rate = engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=48dc548bf95d4f58b27637b83b823821",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=48dc548bf95d4f58b27637b83b823821",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=48dc548bf95d4f58b27637b83b823821",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=48dc548bf95d4f58b27637b83b823821",
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=48dc548bf95d4f58b27637b83b823821",
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=48dc548bf95d4f58b27637b83b823821"}
    content = None
    url = None
    speak("Which Field news do you want, [business], [health], [technology], [entertainment], [sports], [science]")
    field = input("Type field news that you want to hear : ")

    for key, value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
                print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news")
    arts = news["articles"]
    for articles in arts:
        articles = articles["title"] 
        print(articles)
        speak(articles)
        news_url = articles["url"]
        print(f"for more info visit : {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if int(a) == "1":
            pass
        elif int(a) == "2":
            break
        
    speak("thats all")

