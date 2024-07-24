import pyttsx3
engine = pyttsx3.init() #Takes reference from pyttsc3
text = input('Enter Your Text \n')
engine.say(text)
engine.runAndWait()