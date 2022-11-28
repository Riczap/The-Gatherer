import curses
from curses.textpad import rectangle
from time import time

class Prints():
    def __init__(self):
        #Init Colors
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.C_GREEN = curses.color_pair(1)

        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        self.C_RED = curses.color_pair(2)

    #Get updated screen/cmd
    def update_print(self, stdscr):
        self.stdscr = stdscr

        #Toggle from Red and Green depending on status
    def toggle_RG(self, y, x, condition):
        #Conditions  
        if condition:
            self.stdscr.addstr(y, x, str(condition), self.C_GREEN)
        else:
            self.stdscr.addstr(y, x, str(condition), self.C_RED)
    
   
    def display_bot_status(self, bot_status):
        #Clear the line to avoid overwritting
        self.stdscr.move(1,0)
        self.stdscr.clrtoeol()

        
        self.stdscr.addstr(1,1, f"Bot Activated: ")
        
        self.toggle_RG(1, 16, bot_status)
        
        self.stdscr.refresh()

    def display_vision_status(self, vision_status):
        #Clear the line to avoid overwritting
        self.stdscr.move(2,0)
        self.stdscr.clrtoeol()
        #Rectangle for FPS, BOT and VISION (Maybe move later)
        rectangle(self.stdscr, 0, 0, 4, 25 )
        self.stdscr.addstr(2,1, f"Vision Activated: ")
        self.toggle_RG(2, 19, vision_status)
        
        self.stdscr.refresh()

    def fps_counter(self, loop_time):
        #Counter
        fps_text = "{}".format(round(1/(time() - loop_time), 5))
        
        #Display
        self.stdscr.addstr(3,1, "Fps: ")
        self.stdscr.addstr(3,6, fps_text, self.C_GREEN)
        self.stdscr.refresh()

    def display_commands(self):
        #Bot commands
        self.stdscr.addstr(6,2, "Toggle Bot")
        self.stdscr.addstr(7,2, "n: ")
        self.stdscr.addstr(7,5, "On", self.C_GREEN)
        self.stdscr.addstr(8,2, "m: ")
        self.stdscr.addstr(8,5, "Off", self.C_RED)
        rectangle(self.stdscr, 5, 0, 9, 13)
        
        #Vision commands
        self.stdscr.addstr(6, 17, "Toggle Vision")
        self.stdscr.addstr(7,17, "v: ")
        self.stdscr.addstr(7,21, "On", self.C_GREEN)
        self.stdscr.addstr(8,17, "b: ")
        self.stdscr.addstr(8,21, "Off", self.C_RED)        
        rectangle(self.stdscr, 5, 15, 9, 31)

        #Exit command
        self.stdscr.addstr(2, 29, "Exit: ")
        self.stdscr.addstr(2, 35, "r", self.C_GREEN)
        rectangle(self.stdscr, 1, 27, 3, 37)

        self.stdscr.refresh()

    def loading_screen(self):
        ascii_art = """
 $$$$$$$  $$  $$$       $$                            $$$$$$$              $$      
$$  __$$  $$ |$$ |      $__|                          $$  __$$             $$ |    
$$ /  $$ |$$ |$$$$$$$$  $$   $$$$$$   $$$$$$$         $$ |  $$ | $$$$$$  $$$$$$    
$$$$$$$$ |$$ |$$  __$$  $$ |$$  __$$  $$  __$$        $$$$$$$  |$$  __$$  _$$  _|  
$$  __$$ |$$ |$$ |  $$ |$$ |$$ /  $$ |$$ |  $$ |      $$  __$$  $$ /  $$ | $$ |    
$$ |  $$ |$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ | $$ |$$  
$$ |  $$ |$$ |$$$$$$$  |$$ | $$$$$$  |$$ |  $$ |      $$$$$$$  | $$$$$$  |  $$$$  |
$__|  $__|$__|$_______/ $__|  ______/  __|   __|       _______/   ______/    ____/ 

 __          __             _           _               ______           
 \ \        / /            | |         (_)             |  ____|          
  \ \  /\  / /_ _ _ __   __| | ___ _ __ _ _ __   __ _  | |__  _   _  ___ 
   \ \   \  / _` | '_ \ / _` |/ _ \ '__| | '_ \ / _` | |  __|| | | |/ _ \
    \  /\  / (_| | | | | (_| |  __/ |  | | | | | (_| | | |___| |_| |  __/
     \   \  \__,_|_| |_|\__,_|\___|_|  |_|_| |_|\__, | |______ __, | ___|
                                                 __/ |         __/ |     
                                                |___/         |___/   
                                                          



"""                               
        for y, line in enumerate(ascii_art.splitlines(), 2):
            self.stdscr.addstr(y, 2, line)
        self.stdscr.addstr("Loading Model... ")
        self.stdscr.refresh()