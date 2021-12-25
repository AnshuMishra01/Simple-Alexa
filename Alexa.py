""" 
Install the SpeechRecognition
Install the PyAudio
Install text to speech
Install pyjokes
Install python wikipedia
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
 engine.say("text")
 engine.runAndWait()
 
 def take_command():
        try:
          with sr.Microphone() as source:
           print('listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(audio_data)
          command = command.lower()
          if "alexa" in command:
                 command = command.replace('alexa', ' ')
                 talk(command)
        except:
                pass
        return command

def run_alexa():
        command = take_command()
        if 'play' in command:
          song = command.replace('play', '')
          talk('wait for a second im searching any romantic song for you' + song)
          pywhatkit.playonyt(song)
        elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('current time is ' + time)
        elif 'who' in command:
                person = command.replace ('who', '')
                info = wikipedia.summary(person, 5)
                print(info)
                talk(info)
        elif 'date' in command:
                talk('sorry, I have a headache')
        elif 'are you single' in command:
                talk('sorry, I am in a relationsip with wifi')
        elif 'joke' in command:
                talk(pyjokes.get_jokes())
        else:
                talk('Can you please say it again')
while True:               
 run_alexa()

#have Fun and Follow me for more such Programing Projects ;)
