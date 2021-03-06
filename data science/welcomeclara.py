import webbrowser as wb
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import search_google.api

#the user is asking for their news media sources here
#we will say clara tell me news about refugees

def facebook(name):
	speak("Okay! I will redirect you to the news on "+Syria+" today")
	wb.open("https://cse.google.com/cse/publicurl?cx=011280802754178364990:9vsakoduksg")
	
def locations(name):
	data = data.split(" ")
	location = data[2]
	speak("Where can I find information about the Syrian conflict or crisis in data?")
	wb.open("ttps://cse.google.com/cse/publicurl?cx=011280802754178364990:9vsakoduksg")


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")
    

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:audio = r.listen(source)
		#print ("Here is where we speak")
 
    # Speech recognition using Google Speech Recognition with Google Search Speech API
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def PA(topic, name):
	if "What's new in the Middle East" in data:
		speak("I'm Michael.")
	
	if "where is syria in terms of the conflict" in data:
		locations(name)	
		
	if "I would like to search for news about Syria" in data:
		facebook(name)
	
	if "goodbye" in data:
		speak("Good bye ! ,"+name+" ,take care!!")
		exit()
 
# initialization

speak("Hello! What type of news would you like to see today?")
topic=input()
speak("Okay I'll try to see if I can find the most factual articles on "+topic+"for you today")

while 1:
    print("Speak. . .")
    data = recordAudio()
    print ("Processing. . .")
    PA(data,name)
