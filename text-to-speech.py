# Pyttsx3 has 3 properties, VOICES, RATE & VOLUME
# To change them we first will have to know the current values of these properties and this can be done by

import pyttsx3
engine = pyttsx3.init()
speed = engine.getProperty('rate')
print(speed)
#engine.setProperty('rate', 100) | This sets the rate to 100

volume = engine.getProperty('volume')
print(volume)
#engine.setProperty('volume', 0.5) | This sets the volume to .5

voice = engine.getProperty('voices')
print(voice)
engine.setProperty('voice', voice[1].id) #Voice id 1 is for male 

engine.say("Hello world")
engine.runAndWait()