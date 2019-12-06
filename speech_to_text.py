import speech_recognition as sr
import pyaudio,sys
def talk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")
        if text == 'quit':
            sys.exit()
        else:
            talk()

talk()