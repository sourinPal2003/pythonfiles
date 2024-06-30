import speech_recognition as sr

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

if __name__ == "__main__":

    while True:
        x=speech_to_text()
        if(x=='stop' or x=='Stop'):
            print('Thanks to talking with me.')
            break
