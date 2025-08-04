#monobingo.py
#This is played at "scrcpy -m1024 --capture-orientation=0" since it's a "sideways" game
#v0.1

import pywinctl, pyautogui, pytesseract, time, datetime, keyboard, sys, basics

#Parameters
DEBUG = True
EXIT_KEY = 'c'
KEEPALIVE_MAX = 180
UNCERTAINTY_TIMELAPSE = 120

def interrupt_routine(game_start_time):
    global interrupted
    interrupted = True
    hrs = (time.time() - game_start_time)/3600
    mins = (hrs - int(hrs))*60
    print(f"Elapsed time: {hrs:.0f}hr(s) and {mins:.0f}min(s) for this session")
    sys.exit(0)
    
def check_keepalive(keepalive, keepalive_lastclick):
    if keepalive > (KEEPALIVE_MAX + keepalive_lastclick):
        if(DEBUG):
            current_datetime = datetime.datetime.now()
            formatted_time = current_datetime.strftime("%H:%M")
            print(f"DEBUG: [{formatted_time}] Keeping us alive! {(keepalive - keepalive_lastclick):.1f}s")
        basics.click_routine(1284, 724)
        keepalive_lastclick = time.time()
    keepalive = time.time()
    return keepalive, keepalive_lastclick

def find_color(x, y):
    #Detect Color For Letter/Number call
    r1, g1, b1 = pyautogui.pixel(x, y)
    if basics.color_match((r1, g1, b1), (42,  194, 241)):
        return "blue"
    if basics.color_match((r1, g1, b1), (44,  240, 16)):
        return "green"
    if basics.color_match((r1, g1, b1), (239,  33, 111)):
        return "red"
    if basics.color_match((r1, g1, b1), (247, 178, 18)):
        return "yellow"
    if basics.color_match((r1, g1, b1), (175, 60, 232)):
        return "purple"

    return ""

def click_all_matching_column_numbers(color, c1, c2, c3, c4):
    x_set = []
    y_set = []
    
    if color == "blue":
        if c1:
            x_set = [1123]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c2:
            x_set = [1123]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c3:
            x_set = [1518]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c4:
            x_set = [1518]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    #This is a bad dumb way to fix a bug where the last row in the last card never gets clicked for some reason
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
    if color == "purple":
        if c1:
            x_set = [1150]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c2:
            x_set = [1150]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c3:
            x_set = [1553]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c4:
            x_set = [1553]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
    if color == "green":
        if c1:
            x_set = [1087]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c2:
            x_set = [1087]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c3:
            x_set = [1480]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c4:
            x_set = [1480]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
    if color == "yellow":
        if c1:
            x_set = [1055]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c2:
            x_set = [1055]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c3:
            x_set = [1447]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c4:
            x_set = [1447]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
    if color == "red":
        if c1:
            x_set = [1015]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c2:
            x_set = [1015]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c3:
            x_set = [1412]
            y_set = [542, 577, 609, 644, 675]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)
        if c4:
            x_set = [1412]
            y_set = [773, 810, 840, 876, 910]
            for x in x_set:
                for y in y_set:
                    pyautogui.click(x, y)
                    time.sleep(0.001)
                    if y == y_set[-1]:
                        pyautogui.click(x, y)

def find_bingo_cards():
    
    tr = 0
    br = 0
    tl = 0
    bl = 0

    #Find Top Right Bingo Card
    r1, g1, b1 = pyautogui.pixel(1425, 525)
    if basics.color_match((r1, g1, b1), (236, 60, 112)):
        r2, g2, b2 = pyautogui.pixel(1460, 525)
        if basics.color_match((r2, g2, b2), (244, 181, 51)):
            r3, g3, b3 = pyautogui.pixel(1495, 525)
            if basics.color_match((r3, g3, b3), (109, 244, 32)):
                r4, g4, b4 = pyautogui.pixel(1530, 525)
                if basics.color_match((r4, g4, b4), (61, 189, 232)):
                    r5, g5, b5 = pyautogui.pixel(1565, 525)
                    if basics.color_match((r5, g5, b5), (169, 55, 235)):
                        tr = 1
                        #if (DEBUG):
                        #    print("tr True")

    #Find Bottom Right Bingo Card
    r1, g1, b1 = pyautogui.pixel(1425, 760)
    r2, g2, b2 = pyautogui.pixel(1460, 760)
    r3, g3, b3 = pyautogui.pixel(1495, 760)
    r4, g4, b4 = pyautogui.pixel(1530, 760)
    r5, g5, b5 = pyautogui.pixel(1565, 760)
    
    if basics.color_match((r1, g1, b1), (236, 60, 112)):
        if basics.color_match((r2, g2, b2), (244, 181, 51)):
            if basics.color_match((r3, g3, b3), (109, 244, 32)):
                if basics.color_match((r4, g4, b4), (61, 189, 232)):
                    if basics.color_match((r5, g5, b5), (169, 55, 235)):
                        br = 1
                        #if (DEBUG):
                        #    print("br True")

    #Find Top Left Bingo Card
    r1, g1, b1 = pyautogui.pixel(1010, 525)
    r2, g2, b2 = pyautogui.pixel(1045, 525)
    r3, g3, b3 = pyautogui.pixel(1080, 525)
    r4, g4, b4 = pyautogui.pixel(1115, 525)
    r5, g5, b5 = pyautogui.pixel(1150, 525)
    
    if basics.color_match((r1, g1, b1), (236, 60, 112)):
        if basics.color_match((r2, g2, b2), (244, 181, 51)):
            if basics.color_match((r3, g3, b3), (109, 244, 32)):
                if basics.color_match((r4, g4, b4), (61, 189, 232)):
                    if basics.color_match((r5, g5, b5), (169, 55, 235)):
                        tl = 1
                        #if (DEBUG):
                        #    print("tl True")

    #Find Bottom Left Bingo Card
    r1, g1, b1 = pyautogui.pixel(1010, 760)
    r2, g2, b2 = pyautogui.pixel(1045, 760)
    r3, g3, b3 = pyautogui.pixel(1080, 760)
    r4, g4, b4 = pyautogui.pixel(1115, 760)
    r5, g5, b5 = pyautogui.pixel(1150, 760)
    
    if basics.color_match((r1, g1, b1), (236, 60, 112)):
        if basics.color_match((r2, g2, b2), (244, 181, 51)):
            if basics.color_match((r3, g3, b3), (109, 244, 32)):
                if basics.color_match((r4, g4, b4), (61, 189, 232)):
                    if basics.color_match((r5, g5, b5), (169, 55, 235)):
                        bl = 1
                        #if (DEBUG):
                        #    print("bl True")
    
    if (tl or bl or tr or br):
        return (True, tl, bl, tr, br)

    return (False, 0, 0, 0, 0)

def detect_winners():
    #For bingo cards that have to manually be claimed
    for x in [1132, 1442]:
        for y in [707, 941]:
            r1, g1, b1 = pyautogui.pixel(x, y)
            #if (DEBUG):
            #    print(f"{r1} {g1} {b1} vs (39, 255, 88)")
            if basics.color_match((r1, g1, b1), (39, 255, 88)):
                pyautogui.click(x, y)
                print("Bingo!")
                pyautogui.click(x, y)
    
def gamestate():   

    #Choose A Bingo
    #Classic Orange Left Side
    r1, g1, b1 = pyautogui.pixel(1235, 669)
    #Classic Orange Right Side
    r2, g2, b2 = pyautogui.pixel(1320, 669)
    #Pay Button should be G>190
    r3, g3, b3 = pyautogui.pixel(1240, 866)
    if basics.color_match((r1, g1, b1), (242, 152, 23)):
        if basics.color_match((r2, g2, b2), (242, 152, 23)):
            if basics.color_match((r3, g3, b3), (49, 191, 61)):
                return "cab"

    active_cards = find_bingo_cards()
    if active_cards[0] == True:
        return "bingo"


    r1, g1, b1 = pyautogui.pixel(1514, 524)
    r2, g2, b2 = pyautogui.pixel(1531, 524)
    if basics.color_match((r1, g1, b1), (134, 210, 253)):
        if basics.color_match((r2, g2, b2), (133, 210, 254)):
            return "ad1"
    
    return "unsure"

def update_last_5(last5):
    for x, y in {0: 555, 1: 636, 2: 713, 3: 790, 4: 867}.items():
        last5[x] = find_color(1285, y)
    #if(DEBUG):
    #    print("last 5: "+str(last5))
    return last5
    
def main():
    
    global interrupted
    interrupted = False
    previous_state = ""
    rounds = 1
    last5 = ["", "", "", "", ""]
    old_list = ["", "", "", "", ""]
    game_start_time = time.time()
    keepalive = time.time()
    keepalive_lastclick = time.time()
    keyboard.add_hotkey(EXIT_KEY, lambda: interrupt_routine(game_start_time))
    print("Starting... Press '"+EXIT_KEY+"' to exit.")
    
    try:
        while not interrupted:
            window = basics.activate_window()
            while not interrupted:
                keepalive, keepalive_lastclick = check_keepalive(keepalive, keepalive_lastclick)
                state = gamestate()

                if(DEBUG and previous_state != state):
                    print("DEBUG: Detected new state: "+state)

                #A special lazy case after we finish a bingo game to click shit along
                if (previous_state == "bingo" and state == "unsure"):
                    basics.sleep(2)
                    basics.click_routine(1586, 898)

                #Our main blueprint
                match state:
                    case "cab":
                        #We always play classic for now (4 cards)
                        basics.click_routine(1240, 866)
                        keepalive_lastclick = time.time()
                        basics.sleep(1)
                        rounds = 1
                    case "bingo":
                        #What cards do we have up?
                        ig, c1, c2, c3, c4 = find_bingo_cards()
                        #What are the last 5 colors from top to bottom?
                        last5 = update_last_5(last5)
                        #We should have a list with n many non-empty strings as rounds have passed (up to 5)
                        len_last5 = sum(bool(item) for item in last5)
                        #How do we detect a change and avoid empty values from animations?
                        #If the two lists are not the same and the NEWEST value is not ""
                        #This only fails if you get 6 of the same color in a row
                        if ((last5 != old_list) and (last5[0] != "") and (len_last5 >= rounds)):
                            if (DEBUG):
                                print("Last 5: "+str(last5))
                                print("Old List: "+str(old_list))
                                print("Rounds: "+str(rounds))
                            click_all_matching_column_numbers(last5[0], c1, c2, c3, c4)
                            keepalive_lastclick = time.time()
                            #detect_winners()
                            old_list = last5[:]
                            if(rounds < 5):
                                rounds += 1
                        #basics.sleep(1)
                        #Some brute forcing
                        #detect_winners()
                    case "ad1":
                        basics.click_routine(1531,524)
                        keepalive_lastclick = time.time()
                        basics.sleep(2)
                    case "unsure":
                        if interrupted:
                            break
                        else:
                            #pyautogui.moveTo(1779, 496)
                            #basics.sleep(1)
                            unsure_time = time.time()
                            curr_time = time.time()
                            while (state == "unsure" and (curr_time - unsure_time) < UNCERTAINTY_TIMELAPSE and not interrupted):
                                basics.sleep(1)
                                curr_time = time.time()
                                if(DEBUG):
                                    print("DEBUG: Time Elapsed: "+f"{curr_time - unsure_time:.2f}")
                                state = gamestate()
                            if (curr_time - unsure_time > UNCERTAINTY_TIMELAPSE):
                                if(DEBUG):
                                    print("We've been unsure where we are for too long. Quitting.")
                                hrs = (time.time() - game_start_time)/3600
                                mins = (hrs - int(hrs))*60
                                print(f"Elapsed time: {hrs:.0f}hr(s) and {mins:.0f}min(s) for this session")
                                interrupted = True
                                break

                
                previous_state = state
                
    except KeyboardInterrupt:
        sys.exit(0)
    
if __name__ == "__main__":
    main()