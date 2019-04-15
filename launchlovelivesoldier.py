#Variables
soldiergamelink = 'https://www.youtube.com/watch?v=6_YUxyhwk2I'

#imports
import webbrowser
import time
import pyautogui
import pywinauto

#Open Never Gonna Give You Up
webbrowser.open(soldiergamelink)

#Increase to Max Volume
for x in range(0, 60):
    pyautogui.press('volumeup')

#Wait 1 Second
time.sleep(5)

#Make It Full Screen
pyautogui.press('F')

#Finish Program
print("Program Complete. GET RICK ROLLED KEKEKEK!")

