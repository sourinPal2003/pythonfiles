import speech_recognition as sr
import pyautogui as pag
import time
import pyttsx3

def autoMsg(x):
    pag.write(f"{x}", interval=0.2)
    pag.press("Enter")


def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Error connecting to Google Speech Recognition service:", e)


def roboSpeak(x):
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()


def waAssistance():

    print("Prosses start in 5 sec...")
    time.sleep(5)
    roboSpeak('Your Whatsapp Apk is start now.')
    print('Your Whatsapp Apk is start now.')

    i=0
    while True:
        x=speech_to_text()
        if(x!=None):
             i=i+1

        if(x=='stop' or x=='stops' or x=='Stop'):
                roboSpeak('Thanks for use me.')
                print('Thanks for use me.')
                break


        if(x==None):
                roboSpeak('Could not understand.Please speak again')
                continue
    
        autoMsg(x)



        ##Remainder for using apk
        if(i%5==0):
            roboSpeak('Do you want to stop me?')
            x=speech_to_text()
            if(x=='yes' or x=='Yes' or x=='stop' or x=='Stop'):
                roboSpeak('Thanks for use me.')
                print('Thanks for use me.')
                break
            else:
                continue




if __name__ == "__main__":
     waAssistance()
