#Variables
rickrolllink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

#imports
import webbrowser
import time
import pyautogui
import pywinauto

#Open Never Gonna Give You Up
webbrowser.open(rickrolllink)

#Increase to Max Volume
for x in range(0, 40):
    pyautogui.press('volumeup')

#Wait 1 Second
time.sleep(3)

#Make It Full Screen
pyautogui.press('F')

#Finish Program
print("Program Complete. GET RICK ROLLED KEKEKEK!")