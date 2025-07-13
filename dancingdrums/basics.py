#basics.py

import pywinctl
import pyautogui
import time
import win32gui
import win32con
import win32api
import random

PIXELRANGE = 20

#Color Methods
def color_match(actual, expected, tolerance=PIXELRANGE):
    return all(abs(a - e) <= tolerance for a, e in zip(actual, expected))


#Screen methods
def click_routine(x, y):
    try:
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        sleep(0.024)
        pyautogui.mouseUp()
    except Exception as e:
        print("Click routine failed: "+str(e))

def exit_routine():
    try:
        #Bottom of screen
        pyautogui.moveTo(1286, 1228)
        pyautogui.mouseDown()
        time.sleep(0.1)
        #Slide up for home bar
        pyautogui.moveTo(1286, 1179)
        pyautogui.mouseUp()
        time.sleep(0.3)
        #Click all running tasks
        click_routine(1148, 1198)
        time.sleep(1)
        #Click close all
        click_routine(1279, 1008)
        time.sleep(1)
    except Exception as e:
        print("Exit routine failed: "+str(e))

def activate_window(WINDOW_TITLE = "SM-A356U"):
    try:
        window = pywinctl.getWindowsWithTitle(WINDOW_TITLE)[0]
        if window == False:
            #No window means something is horribly wrong
            sys.exit(1)
        window.activate()
        width, height = window.size
        if width == 488 and height == 1063:
            return window
        else:
            return False
    except IndexError:
        print(f"Window with title '{WINDOW_TITLE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def sleep(x):
    delta = random.random() % 0.75
    time.sleep(x+delta)
