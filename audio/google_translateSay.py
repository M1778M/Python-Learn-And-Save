import pyttsx3 as ptt

eng = ptt.init()

eng.say('Hello World') # man sound
eng.runAndWait()

voices = eng.getProperty('voices')

eng.setProperty('voice',voices[1].id) # woman sound

eng.say('The Best')

eng.runAndWait()
