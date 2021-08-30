'''import sys 
import pyttsx3
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import random 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
r=sr.Recognizer()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def listen():		
	with sr.Microphone() as source:
		print('How may i help you!')
		print("listening!...")
		r.pause_threshold = 1
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio,language='en-in')
			text = "you said "+text
			speak(text)
			print(text)
		except Exception as e:
			speak("sorry sound was not clear")
			print("sorry sound was not clear")
			return "None"
	return text
def truthordare():
	game=input("enter the choices : rock,paper or scissors:")
	
	a=random.randint(1,3)
	if game =='rock':
		if a==1:
			print('tie')
		elif a==2:
			print('it was scissor,you lost')
		else:
			print('it was paper,you won')
	elif game=='scissors':
		if a==1:
			print('rock,you lost')
		elif a==2:
			print('tie')
		else :
			print('paper,you won')
	elif game=='paper':
		if a==1:
			print('rock,you won')
		elif a==2:
			print('scissors,you lost')
		else:
			print('you won')
	else :
	    print('Error!')
	w=input('wanna play again?:y/n :')
	
	if  w=='y':
		truthordare()
	elif w=='n':
		print("Thank You For playing!")
	else:
		print("Error!")

if __name__ =="__main__":
	speak("Hey its shaktimaan how may i help you!")
	while True:
		text = listen().lower()
		if 'wikipedia' in text:
			result=wikipedia.summary(text,sentences=2)
			speak("according to wikipedia " + result)
			print(result)
		elif 'open youtube' in text:
			webbrowser.open("youtube.com")
		elif 'open google' in text:
			webbrowser.open("google.com")
		elif 'game' in text:
			truthordare()
		elif 'shutdown pc' in text:
			os.system("shutdown /s /t 1")
		elif 'restart pc' in text:
			os.system("shutdown /r /t 1")
		elif 'thankyou shaktimaan' or 'exit shaktimaan' or 'quit shaktimaan' in text:
			speak("have a nice day ahead!Bye.")
			break
	'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/'
r = requests.get(url)
htmlcontent = r.content

soup= BeautifulSoup(htmlcontent,'html.parser')
print(soup.title)