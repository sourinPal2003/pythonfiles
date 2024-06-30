
##pip install pyttsx3
import pyttsx3

while True:
    x = input("Enter: ")
    if(x=="exit!"):
        break

    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
  




##to voice available and change:
# engine = pyttsx3.init()
# v= engine.getProperty('voices')
# engine.setProperty('voices',v[1].id)
# print(v[1].id)
