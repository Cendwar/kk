#dancingdrums.py
#v0.1

import pywinctl, pyautogui, time, keyboard, sys, basics

#Parameters
UNCERTAINTY_TIMELAPSE = 12
DEBUG = True
EXIT_KEY = 'c'
KEEPALIVE_MAX = 120

def interrupt_routine(game_time):
    global interrupted
    interrupted = True
    hrs = (time.time() - game_time)/3600
    mins = (hrs - int(hrs))*60
    print(f"Elapsed time: {hrs:.0f}hr(s) and {mins:.0f}min(s) for this session")
    sys.exit(0)
    
def close_sidebar():
    #Coin Spot 1
    r1, g1, b1 = pyautogui.pixel(1429, 666)
    if basics.color_match((r1, g1, b1), (24, 99, 211)):
        basics.click_routine(1399, 747)
        basics.sleep(1)

def check_keepalive(keepalive, keepalive_lastclick):
    if keepalive > (KEEPALIVE_MAX + keepalive_lastclick):
        if(DEBUG):
            print(f"DEBUG: Keeping us alive! {(keepalive - keepalive_lastclick):.1f}s")
        basics.click_routine(1266, 858)
        keepalive_lastclick = time.time()
    keepalive = time.time()
    return keepalive, keepalive_lastclick
    
def gamestate():   
    #Coin Flip state
    #Coin Spot 1
    r1, g1, b1 = pyautogui.pixel(1164, 805)
    #Coin Spot 2
    r2, g2, b2 = pyautogui.pixel(1164, 910)
    if basics.color_match((r1, g1, b1), (255, 219, 0)):
        if basics.color_match((r2, g2, b2), (224, 149, 0)):
            return "coinflip"

    #Egg upgrade/won state
    #Upgrade Arrow
    r1, g1, b1 = pyautogui.pixel(1281, 724)
    #Green Collect
    r2, g2, b2 = pyautogui.pixel(1108, 846)
    r3, g3, b3 = pyautogui.pixel(1112, 817)
    if basics.color_match((r1, g1, b1), (7, 139, 248)):
        if basics.color_match((r2, g2, b2), (53, 129, 0)) or basics.color_match((r3, g3, b3), (96, 188, 0)):
            return "eggwon"

    #This is for our "pick a free game" state
    #Golden Line
    r1, g1, b1 = pyautogui.pixel(1266, 858)
    #Purple Background
    r2, g2, b2 = pyautogui.pixel(1073, 906)
    if basics.color_match((r1, g1, b1), (255, 219, 127)):
        if basics.color_match((r2, g2, b2), (88, 3, 108)):
            return "frgamespick"

    #Out Of Coins
    #Purple Multiply Button
    r1, g1, b1 = pyautogui.pixel(1290, 834)
    #Blue Top Bar
    r2, g2, b2 = pyautogui.pixel(1173, 574)
    if basics.color_match((r1, g1, b1), (245, 0, 164)):
        if basics.color_match((r2, g2, b2), (5, 71, 153)):
            return "broke"

    #10n Levels
    #Purple Multiply Button
    r1, g1, b1 = pyautogui.pixel(1290, 839)
    #Gold Symbol
    r2, g2, b2 = pyautogui.pixel(1294, 600)
    if basics.color_match((r1, g1, b1), (255, 57, 198)):
        if basics.color_match((r2, g2, b2), (255, 143, 2)):
            return "levelup"

    #"Free games are playing out" state
    #Red Stop Button
    r1, g1, b1 = pyautogui.pixel(1383, 1183)
    #r2, g2, b2 = pyautogui.pixel(1073, 906)
    if basics.color_match((r1, g1, b1), (170, 33, 32)):
        #if basics.color_match((r2, g2, b2), (26, 152, 0)):
        return "frgames"

    #Spinning/Playing
    #Purple Stop Button
    r1, g1, b1 = pyautogui.pixel(1380, 1167)
    #Red Side Background
    r2, g2, b2 = pyautogui.pixel(1047, 1070)
    if basics.color_match((r1, g1, b1), (210, 83, 239)):
        if basics.color_match((r2, g2, b2), (109, 1, 41)):
            return "spinning"

    return "unsure"
    
def main():
    
    global interrupted
    interrupted = False
    previous_state = ""
    game_time = time.time()
    keepalive = time.time()
    keepalive_lastclick = time.time()
    keyboard.add_hotkey(EXIT_KEY, lambda: interrupt_routine(game_time))
    print("Starting Casino... Press '"+EXIT_KEY+"' to exit.")
    
    try:
        while not interrupted:
            window = basics.activate_window()
            #We play at a lower bid for longevity
            #A closer to white value means the bid select is not greyed out and we haven't started yet
            #r, g, b = pyautogui.pixel(1130, 1180)
            #if basics.color_match((r, g, b), (246, 246, 246)):
            #    for x in range (0,2):
            #        basics.click_routine(1128, 1180)
            while not interrupted:
                keepalive, keepalive_lastclick = check_keepalive(keepalive, keepalive_lastclick)
                close_sidebar()
                state = gamestate()
                if(DEBUG and previous_state != state):
                    print("DEBUG: Detected new state: "+state)
                
                match state:
                    case "frgamespick":
                        #We always go for the 3 games
                        basics.click_routine(1359, 993)
                        keepalive_lastclick = time.time()
                        basics.sleep(1)
                    case "frgames":
                        #Nothing to do here, but we should still recognize the state just incase
                        basics.sleep(1)
                    case "coinflip":
                        #Iterate through the field
                        #We only need to click 9/12 since there are 4 outcomes
                        for x in range(1464, 1164, -100):
                            for y in range(1015, 804, -105):
                                basics.click_routine(x, y)
                                keepalive_lastclick = time.time()
                                basics.sleep(2)
                    case "eggwon":
                        basics.click_routine(1108, 846)
                        basics.click_routine(1112, 817)
                        keepalive_lastclick = time.time()
                        basics.sleep(10)
                        #Collect after opening
                        basics.click_routine(1283, 840)
                        keepalive_lastclick = time.time()
                        basics.sleep(5)
                    case "spinning":
                        #Nothing to do here, but we should still recognize the state just incase
                        basics.sleep(1)                        
                    case "broke":
                        basics.click_routine(1250, 834)
                        basics.sleep(1)
                        keepalive_lastclick = time.time()
                        #print("Alas we are broke and I'm too dumb to watch ads. Time to stop")
                        #print(f"Elapsed time: {(time.time() - game_time):.1f} seconds for this session")
                        #interrupted = True
                    case "levelup":
                        basics.click_routine(1174, 852)
                        keepalive_lastclick = time.time()
                        basics.sleep(1)
                    case "unsure":
                        r1, g1, b1 = pyautogui.pixel(1380, 1167)
                        if g1 >= 150:
                            if(DEBUG):
                                print("DEBUG: Spin button looks green. Pressing it.")
                            pyautogui.moveTo(1380, 1167)
                            pyautogui.mouseDown()
                            basics.sleep(2)
                            pyautogui.mouseUp()
                        basics.sleep(1)
                        
                previous_state = state        
                
    except KeyboardInterrupt:
        sys.exit(0)
    
if __name__ == "__main__":
    main()