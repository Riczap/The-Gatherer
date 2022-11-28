import curses
from curses import wrapper
import cv2
from time import time, sleep
import torch
import numpy as np
import keyboard
#Modules
from window_capture import WindowCapture
from paint import Prints
from bot_thread import Move
from functions import get_center, get_rectangles, toggle_vision                                                    

def main():
    wrapper(vision)

def vision(stdscr):
    #Inizializate display class
    display = Prints()
    display.update_print(stdscr)
    display.loading_screen()
    #Load Yolov5 model with custom weights "best.pt"
    model = torch.hub.load('ultralytics/yolov5','custom', path = 'best1.pt', force_reload=True)

    stdscr.addstr("Complete", display.C_GREEN)
    stdscr.refresh() 
    sleep(1.5)
    stdscr.clear()
    stdscr.refresh()

    #Call Classes
    wincap = WindowCapture(None)
    go = Move()
    go.start()

    #Determine if bot is on or off
    bot_status = False
    
    #Determine if vision is on or off
    vision_status = False
    
    #Start Loop Timer
    loop_time = time()
    
    #Create pad for the bot display
    rec_win = curses.newpad(10, 35)

    while True:       
        display.update_print(stdscr)
        #Grab screen image
        screenshot = wincap.get_screenshot()

        #Process image with custom model
        results = model(screenshot)
        
        #Display BOT, VISION and FPS
        display.display_bot_status(bot_status)
        display.display_vision_status(vision_status)
        display.fps_counter(loop_time)
        
        #Display Commands
        display.display_commands()

        #Convert processed img to a cv2 compatible format
        frame = np.squeeze(results.render())
        
        #Display Bot View
        toggle_vision(vision_status, frame)

        #Get rectangles position of detected objects
        rectangles = get_rectangles(results)
        #Get the center position of the rectangles
        centers = get_center(rectangles)
        

        loop_time = time()

        #Event Keys
        #Toggle Bot
        if keyboard.is_pressed("n"):
            bot_status = True
 
        if keyboard.is_pressed("m"):
            bot_status = False
            rec_win.clear()

        #Toggle Vision
        if keyboard.is_pressed("v"):
            vision_status = True
 
        if keyboard.is_pressed("b"):
            vision_status = False


        #Call update function of the bot actions thread passing the curses screen and the center position
        go.update(centers, rec_win, bot_status)


        #Break while on opencv screen ("q") or in the cmd window ("r")
        if cv2.waitKey(1) == ord("q") or keyboard.is_pressed("r"):
            #Stop bot actions
            go.stop()
            cv2.destroyAllWindows()
            break


main()