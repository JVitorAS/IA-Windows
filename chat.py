import pyttsx3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime as date
import os
import time
from selenium import webdriver

username = os.getlogin()

engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('volume', 0.9)  

def hora_local():
    return date.datetime.now().strftime("%H:%M")

def execute_date_time():
    current_time = date.datetime.now().strftime("%H:%M")
    current_date = date.datetime.now().strftime("%Y-%m-%d")
    print(current_date)
    print(current_time)
    fal = f"Today is {current_date} and the current time is {current_time}"
    engine.say(fal)
    engine.runAndWait()

def exe_search(query):
    chrome = webdriver.Chrome()
    chrome.get(f"https://www.google.com/search?q={query}")
    input("Pressione Enter para fechar o navegador...")
    chrome.quit()
    

def exe_song(query):
    if query is not None:
        try:
            os.system("start Spotify.exe")
        except Exception as e:
            print("Erro ao pesquisar a música:", e)

def open_application(query):
    if query is not None:
        try:
            os.system(f"{query}.exe")
        except Exception as e:
            print("Erro ao abrir o aplicativo:", e)

def close_application(query):
    if query is not None:
        try:
            os.system(f'taskkill /f /im {query}.exe')
        except Exception as e:
            print("Erro ao fechar o aplicativo:", e)

def poweroff_computer():
    os.system('shutdown -s -t 0')


if hora_local() >= "05:00" and hora_local() <= "12:30":
    fal = f"Good day, {username}!"
elif hora_local() >= "12:31" and hora_local() <= "18:00":
    fal = f"Good afternoon, {username}"
else:
    fal = f"Good night, {username}"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

engine.say(fal)
engine.runAndWait()
