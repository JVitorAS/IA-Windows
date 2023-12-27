import speech_recognition as sr
import os
from googletrans import Translator
import chat  # Importe o arquivo chat.py (certifique-se de que esteja no mesmo diretório)

recognizer = sr.Recognizer()
translator = Translator()

while True:
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
        
    try:
        recognized_text = recognizer.recognize_google(audio)
        print("You said:", recognized_text)
        
        # Ver Data e Hora
        if 'date and time' in recognized_text.lower():
            chat.execute_date_time()  
       
        # Pesquisar no navegador (Testando no Chrome)
        elif 'search' in recognized_text.lower():
            words = recognized_text.split(' ')
            query_index = words.index('search') + 1
            query = ' '.join(words[query_index:]) 
            chat.exe_search(query)
        
        # Verificar se for musica e pesquisar qual a musica
        elif 'music' in recognized_text or 'song' in recognized_text:
            music_command = recognized_text.replace("play ", "").strip().lower()
            chat.exe_song(music_command)
        
        # Abrir algum programa
        elif 'application' in recognized_text or 'execute' in recognized_text:
            app_name = recognized_text.split(' ')[1:]
            command = ' '.join(app_name).strip()
            chat.open_application(command)
        
        #fechar um progerama
        elif 'close' in recognized_text:
            app_name = recognized_text.split(' ')[1:]
            command = ''.join(app_name).strip()
            chat.close_application(command)

        # Desligar o computador
        elif 'power off' in recognized_text or 'shutdown' in recognized_text:
            chat.poweroff_computer()

        #Parar o bot
        elif 'stop' in recognized_text or 'pause' in recognized_text:
            break

    except sr.UnknownValueError:
        print("It was not possible to understand the speech.")
    except sr.RequestError as e:
        print("Error when making a request to the speech recognition service; {0}".format(e))

    #Em breve mais atualização