import pyautogui
import time

time.sleep(2)

while True:
    pyautogui.press('up')
    pyautogui.hotkey('command', 'a')  
    pyautogui.press('delete')  
    pyautogui.press('delete')  
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.click(button='left')

    time.sleep(0)
