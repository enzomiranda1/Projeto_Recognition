import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # estava faltando o "s" em voices e o índice correto da voz

def talk(text):
    engine.say(text)
    engine.runAndWait()  

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)  # estava faltando um espaço após a palavra "is"
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)  # estava faltando a atribuição do resultado da busca à variável "info"
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with the wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())  # estava faltando o "s" em "get_joke"
    elif 'break' in command:
        talk('Close console')
        exit()
    elif 'brother' in command:
        talk('The bombado brother')
    elif 'intruder alert' in command:
        talk('you choose the wrong house baby')
        pywhatkit.playonyt('welcome to the jungle')
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
