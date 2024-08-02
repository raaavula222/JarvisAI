import pyttsx3
import speech_recognition as sr

# Speak Engine
# engine = pyttsx3.init() #Takes reference from pyttsc3
# voice = engine.getProperty('voices')
# engine.setProperty('voice', voice[1].id)
# engine.say(text)
# engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))