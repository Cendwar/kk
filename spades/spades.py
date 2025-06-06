#spades.py

import pywinctl, pyautogui, time, basics

PIXELRANGE = 5
DEBUG = True

def color_match(actual, expected, tolerance=PIXELRANGE):
    return all(abs(a - e) <= tolerance for a, e in zip(actual, expected))

def gamestate(banner):
    # S1 - Play
    r1, g1, b1 = pyautogui.pixel(1097, 1035)
    r2, g2, b2 = pyautogui.pixel(1184, 825)
    if color_match((r1, g1, b1), (160, 185, 159)):
        if color_match((r2, g2, b2), (26, 152, 0)):
            return "play"

    if(DEBUG):
        print(f"DEBUG: Play r, g, b: {r1} {g1} {b1} && {r2} {g2} {b2}")

    # S2 - Select your bid
    if banner:
        r1, g1, b1 = pyautogui.pixel(1185, 890)
        r2, g2, b2 = pyautogui.pixel(1198, 877)
        if color_match((r1, g1, b1), (28, 145, 243)):
            if color_match((r2, g2, b2), (255, 254, 252)):
                return "bid"
    else:
        r1, g1, b1 = pyautogui.pixel(1185, 850)
        r2, g2, b2 = pyautogui.pixel(1198, 837)
        if color_match((r1, g1, b1), (28, 145, 243)):
            if color_match((r2, g2, b2), (255, 254, 252)):
                return "bid"

    if(DEBUG):
        print(f"DEBUG: Bid r, g, b: {r1} {g1} {b1} && {r2} {g2} {b2}")

    # S3 - Game Won
    r1, g1, b1 = pyautogui.pixel(1170, 404)
    r2, g2, b2 = pyautogui.pixel(1201, 521)
    if color_match((r1, g1, b1), (255, 253, 254)):
        if color_match((r2, g2, b2), (254, 216, 75)):
            return "won"

    if(DEBUG):
        print(f"DEBUG: Won r, g, b: {r1} {g1} {b1} && {r2} {g2} {b2}")

    # S4 - Round Results
    if banner:
        r1, g1, b1 = pyautogui.pixel(1091, 856)
        r2, g2, b2 = pyautogui.pixel(1277, 870)
        if color_match((r1, g1, b1), (27, 70, 197)):
            if color_match((r2, g2, b2), (0, 247, 88)):
                return "round"
    else:
        r1, g1, b1 = pyautogui.pixel(1091, 816)
        r2, g2, b2 = pyautogui.pixel(1277, 830)
        if color_match((r1, g1, b1), (27, 70, 197)):
            if color_match((r2, g2, b2), (0, 247, 88)):
                return "round"

    if(DEBUG):
        print(f"DEBUG: Round r, g, b: {r1} {g1} {b1} && {r2} {g2} {b2}")

    # S5 - Game Lost
    r1, g1, b1 = pyautogui.pixel(1170, 404)
    r2, g2, b2 = pyautogui.pixel(1416, 505)
    if color_match((r1, g1, b1), (255, 253, 254)):
        if color_match((r2, g2, b2), (250, 251, 147)):
            return "lost"

    if(DEBUG):
        print(f"DEBUG: Lost r, g, b: {r1} {g1} {b1} && {r2} {g2} {b2}")
    return "unsure"
    
def initialize_game(banner):
    #Activate Window
    window = basics.activate_window()
    basics.sleep(1)
    #Open game and wait for load if it's not open already
    if (gamestate(banner) == "unsure"):
        basics.click_routine(1104, 800)
        basics.sleep(11)
    banner = banner_check(banner)
    return window, banner
    
def banner_check(banner):
    #Do we have an advertisement banner?
    r, g, b = pyautogui.pixel(1253, 335)
    #If not y=260 will be white
    if (not (color_match((r, g, b), (252, 252, 255)) or color_match((r, g, b), (66, 68, 68)))):
        if(DEBUG):
            print(f"DEBUG: No banner detected")
        banner=False
    else:
        if(DEBUG):
            print(f"DEBUG: Banner detected")
        banner=True
    return banner
    
    
def main():
    print("Starting Spades...")
    won = 0
    lost = 0
    banner = False
    start_time = time.time()
    end_time = time.time()
    elapsed_time = end_time - start_time
    game_times = []
    
    try:
        while True:
            window, banner = initialize_game(banner)
            while True:
                #Where were we? (Main Loop)
                banner = banner_check(banner)
                window = basics.activate_window()
                state = gamestate(banner)
                if (state == "unsure"):
                    if(DEBUG):
                        print("DEBUG: State was unsure. Attempting to get state once more...")
                    basics.sleep(8)
                    state = gamestate(banner)
                if(DEBUG):
                    print("DEBUG: Detected state: "+str(state))
                #Start
                match state:
                    case "bid":
                        #In some cases. We "win or lose" and an ad jumps in before we can record it
                        #We have no way of knowing if it's a W/L right now
                        # end_time = time.time()
                        # elapsed_time = end_time - start_time
                        # if elapsed_time >= 120:
                            # print(f"Elapsed time: {elapsed_time} seconds for this game")
                            # game_times.append(elapsed_time)
                        # start_time = time.time()
                        if banner:
                            #Click bid
                            basics.click_routine(1185, 888)
                            basics.sleep(0.5)
                            #Click play
                            basics.click_routine(1312, 888)
                            basics.sleep(4)
                        else:
                            #Click bid
                            basics.click_routine(1185, 848)
                            basics.sleep(0.5)
                            #Click play
                            basics.click_routine(1312, 848)
                            basics.sleep(4)
                    case "play":
                        #Click helper lightbulb
                        basics.click_routine(1097, 1035)
                        basics.sleep(0.2)
                        #A card should light up
                        clicked = False
                        for x in range(1074, 1483, 5): #Skip over incriments of 5 pixels for speed
                            r, g, b = pyautogui.pixel(x, 1060)
                            #print("DEBUG: r, g, b = "+str(r)+" "+str(g)+" "+str(b))
                            if color_match((r, g, b), (227, 235, 245)):
                                #We found our popup card. Try clicking it in different spots
                                basics.click_routine(x+5, 1070)
                                basics.sleep(0.1)
                                basics.click_routine(x, 1070)
                                basics.sleep(0.1)
                                basics.click_routine(x-5, 1070)
                                clicked = True
                                break
                        if not clicked:
                            print("Something went wrong trying to click our card.")
                            basics.exit_routine()
                            basics.sleep(2)
                            break
                        basics.sleep(5)
                    case "won":
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        print(f"Elapsed time: {elapsed_time} seconds for this game")
                        game_times.append(f"{elapsed_time:.0f}")
                        start_time = time.time()
                        #Click New Game
                        basics.click_routine(1269, 891)
                        basics.sleep(11)
                        #Do our bid routine afterwards
                        
                        won = won + 1
                        print("Current W/L: "+str(won)+"/"+str(lost))
                    case "round":
                        if banner:
                            #Click Continue
                            basics.click_routine(1277, 910)
                            basics.sleep(5)
                            #Do our bid routine afterwards
                        else:
                            #Click Continue
                            basics.click_routine(1277, 870)
                            basics.sleep(5)
                    case "lost":
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        print(f"Elapsed time: {elapsed_time} seconds for this game")
                        game_times.append(f"{elapsed_time:.0f}")
                        start_time = time.time()
                        #Click New Game
                        basics.click_routine(1269, 891)
                        basics.sleep(11)
                        #Do our bid routine afterwards
                        
                        lost = lost + 1
                        print("Current W/L: "+str(won)+"/"+str(lost))
                    case "unsure":
                        print("Case was unsure twice. Probably an ad... probably...")
                        basics.exit_routine()
                        basics.sleep(2)
                        break

    except KeyboardInterrupt:
        print("List of "+str(len(game_times))+" game durations: "+str(game_times))


    
if __name__ == "__main__":
    main()
    
    