'''Voice recognition Package with google voice recognition api'''

import speech_recognition as sr


#Record Audio
def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something!\n")
        audio = r.listen(source)

    try:
        print("You said: " + r.recognize_google(audio)+ "\n")
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("could not request results from Googke Speech REcognition service")
