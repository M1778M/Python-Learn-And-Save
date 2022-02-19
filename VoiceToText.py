import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as sourse:
        print("listen...")
        voice = listener.listen(sourse)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
except:
    pass
