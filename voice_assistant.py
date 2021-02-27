import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

rate = engine.getProperty('rate')                         
engine.setProperty('rate', 130)  
listener.energy_threshold = 300

def talk(text):
	engine.say(text)
	engine.runAndWait()

def take_command():
	try:
		with sr.Microphone() as source:
			print("listening....")
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			command=command.lower()
			
	except sr.UnknownValueError:
		print('please say that again sir')
		return 'inaudible'
	return command

def run():

	while True:
	
		command=take_command()
		if 'play' in command:
			song=command.replace('play','')
			talk('playing' + song)
			pywhatkit.playonyt(song)
			
		elif 'time' in command:
			time=datetime.datetime.now().strftime('%I:%M %p')
			talk('current time is '+time)
			print(time)

		elif 'day' in command:
			day=datetime.datetime.now().strftime('%A')
			talk('today is '+day)
			print(day)
			
		elif 'date' in command:
			dt=datetime.datetime.now().strftime('%d:%b:%y')
			talk('todays date is '+dt)
			print(dt)
		
		elif 'notepad' in command:
			talk('opening notepad')
			os.system("C:\\Windows\\notepad.exe")

		elif 'paint' in command:
			talk('opening paint')
			os.system("mspaint")

		elif 'task manager' in command:
			talk('opening task manager')
			os.system("taskmgr")

		elif 'code' in command:
			talk('opening v s code')
			os.system("code .")

		elif 'google' in command:
			talk('opening google')
			webbrowser.open("www.google.com")

		elif 'youtube' in command:
			talk('opening youtube')
			webbrowser.open("www.youtube.com")

		elif 'calculator' in command:
			talk('opening calculator') 
			os.system("C:\\Windows\\System32\\calc.exe")
		
		elif 'quit' in command:
			talk('Bye see you again')
			print('Bye see you again')
			break

		elif 'inaudible' in command:
			talk('please say that again')

		else:
			talk('sorry the task cant be performed')
		
engine.say('hi how can i help you')
engine.runAndWait()

run()
