import pyautogui
import time

limit = input("limit:- ")
message = input("enter your message:- ")
i = 0
time.sleep(10)

while i < int(limit):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    i+=1