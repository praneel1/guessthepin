import pyautogui
from time import sleep

sleep(2)

for i in range(1000,10000):
    print("Trying", i)
    pyautogui.click(500,480)
    pyautogui.write(str(i))
    sleep(0.01)
    pyautogui.click(830,470)
    sleep(0.8)



#while(True):
 #    print(pyautogui.position())
 #    sleep(0.5)



#   500,480 => pin
#   830,470 => button
