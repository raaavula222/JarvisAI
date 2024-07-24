import pyttsx3
engine = pyttsx3.init() #Takes reference from pyttsc3
text = "Hello world!"
engine.say(text)
engine.runAndWait()