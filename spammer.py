import pyautogui, time
.sleep(10)
f = open("script.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
