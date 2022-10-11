
import pyautogui
import time
time.sleep(5)
count =1
#any message
msg="I am sorry"
#while loop for counting no of messages
while count<10:
    
    pyautogui.typewrite(msg)
    pyautogui.press('Enter')

    time.sleep(1)
    count+=1
