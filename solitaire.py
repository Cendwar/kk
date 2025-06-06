#Solitaire Solver written by Cendwar
#v0.1
#05/25/25 Challenge
#Start from home screen

import pywinctl
import pyautogui
import time

# Configuration
WINDOW_TITLE = "SM-A356U"

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
        pyautogui.moveTo(1286, 1228)
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.moveTo(1286, 1179)
        pyautogui.mouseUp()
        time.sleep(0.3)
        click_routine(1148, 1198)
        time.sleep(1)
        click_routine(1279, 1008)
        time.sleep(1)
    except Exception as e:
        print("Exit routine failed: "+str(e))
        
        
def activate_window(WINDOW_TITLE):
    try:
        window = pywinctl.getWindowsWithTitle(WINDOW_TITLE)[0]
        window.activate()
    except IndexError:
        print(f"Window with title '{WINDOW_TITLE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Start
def main():
    print("Starting Solitaire Solver...")

    while True:
        while True:
            activate_window(WINDOW_TITLE)
            time.sleep(1)
            
            #Open Game
            click_routine(1187,667)
            time.sleep(10)
            
            #Open Challenge
            r, g, b = pyautogui.pixel(1112, 1055)
            if (r != 255 and g != 255 and b != 255):
                exit_routine()
                break
            click_routine(1112, 1055)
            time.sleep(1)
            click_routine(1112, 1055) #May 25 Challenge in same spot
            time.sleep(1)
            #Click Play
            click_routine(1219, 1172)
            
            #Wait for game to open, animation to play
            time.sleep(3)
            r, g, b = pyautogui.pixel(1281, 847)
            if (r != 182 and g != 227 and r != 178):
                exit_routine()
                break
            #Go through the challenge
            click_routine(1084, 556)
            time.sleep(4)
            for i in range(4):
                click_routine(1278, 572)
                time.sleep(0.5)
            #KKQQ Handled
            for i in range(4):
                click_routine(1342, 580)
                time.sleep(0.5)
            #9J Handled
            for i in range(2):
                click_routine(1409, 597)
                time.sleep(0.5)
            
            for i in range(2):
                click_routine(1471, 597)
                time.sleep(0.5)
            
            #Open the 4C
            click_routine(1474, 459) #Pile
            time.sleep(0.5)
            #Move the 4C
            click_routine(1403, 450) #OpenCard
            time.sleep(0.5)
            #Move the 3D
            click_routine(1471, 597)
            time.sleep(0.5)
            #Move the AD
            click_routine(1474, 459) #Pile
            time.sleep(1)
            #Show the 9H
            click_routine(1474, 459) #Pile
            time.sleep(0.5)
            #Move the 9H
            click_routine(1403, 450) #OpenCard
            time.sleep(0.5)
            #Move the 8S from Foundation
            click_routine(1086, 463)
            time.sleep(0.5)
            #Move the 7D
            click_routine(1406, 540)
            time.sleep(20)
            #Done
            exit_routine()
            
if __name__ == "__main__":
    main()

