import pyautogui as spam
import time 

limit = input("Enter your limit: ")
msg = input("Enter your message: ")
i = 0

time.sleep(10)

while i<int(limit):
    
    spam.typewrite(msg)
    spam.press('Enter')
    
    i+=1