#basics.py

import pywinctl
import pyautogui
import time
import win32gui
import win32con
import win32api
import random

#Screen methods
def click_routine(x, y):
    try:
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(0.1)
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

def sideways_exit():
    try:
        #Bottom of screen
        pyautogui.moveTo(2064, 439)
        pyautogui.mouseDown()
        time.sleep(0.1)
        #Slide up for home bar
        pyautogui.moveTo(2008, 439)
        pyautogui.mouseUp()
        time.sleep(0.3)
        #Click all running tasks
        click_routine(2034, 573)
        time.sleep(1)
        #Click close all
        click_routine(1556, 620)
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
            sideways_exit()
            return False
    except IndexError:
        print(f"Window with title '{WINDOW_TITLE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def sleep(x):
    delta = random.random() % 0.235
    time.sleep(x+delta)

#Direct app window methods
# def scr_to_app_xy(x, y, handle):
    # try:
        # a, b = win32gui.ScreenToClient(handle, (x, y))
        # return a, b
    # except Exception as e:
        # print("scr_to_app_xy failed: "+str(e))
        
# def click(x, y, hWnd):
    # Convert screen coordinates to client coordinates
    # x, y = win32gui.ScreenToClient(hWnd, (x, y))
    
    # Send left mouse button down message
    # win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
    # time.sleep(0.1)
    # Send left mouse button up message
    # win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(x, y))

# def get_window_handle(name = "SM-A356U"):
    # try:
        # hwnd = win32gui.FindWindow(None, name)
        # return hwnd
    # except Exception as e:
        # print("get_window_handle failed: "+str(e))