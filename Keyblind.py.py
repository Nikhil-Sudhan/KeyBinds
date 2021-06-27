import pyautogui as pya
import pyperclip
import time
import keyboard
import webbrowser

lst = []

def copy_clipboard():
    pyperclip.copy("")
    pya.hotkey('ctrl','c')
    time.sleep(.1)
    return pyperclip.paste()

def double_click_copy():
    pya.doubleClick(pya.position())
    pya.click(pya.position())
    var=copy_clipboard()
    lst.append(var)
    print(lst)
    webbrowser.open('https://stackoverflow.com/')
    time.sleep(3)
    pya.hotkey('ctrl','v')
    pya.press('enter')

keyboard.add_hotkey('ctrl+f9',double_click_copy)
keyboard.wait()
 