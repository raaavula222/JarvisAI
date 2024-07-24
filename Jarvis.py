import pyttsx3
engine = pyttsx3.init() #Takes reference from pyttsc3
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
text = input('Enter Your Text \n')
engine.say(text)
engine.runAndWait()