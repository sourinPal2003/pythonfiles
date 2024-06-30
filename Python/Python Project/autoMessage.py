import pyautogui as pag
import time

print("Waiting for go to whatsapp for 5sec....")
time.sleep(5)

for i in range(1,400):
    pag.write(f"hehee...")
    pag.press("Enter")




