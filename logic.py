import requests
import pyttsx3

def fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("text", "no fact")
    else:
        return "Нет данных"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()