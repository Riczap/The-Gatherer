import threading
from time import sleep
import pyautogui
import random
import curses
from curses.textpad import rectangle
import math

class Move:
	def __init__(self):
		self.lock = threading.Lock()
		#Inizializate Colors
		curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
		self.C_GREEN = curses.color_pair(1)

		curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
		self.C_RED = curses.color_pair(2)

		#Center of the screen
		self.screen_center = [512, 284]


	#Default parameter for refreshing the pad
	def rec_refresh(self):
		self.rec_win.refresh(0,0,10,0,17,35)
		
	def nearest_object(self):
		dictionary = {}
		for i in range(len(self.centers)):
			object_location = self.centers[i]
			#Calculate distance between an object and the character
			distance = math.dist(object_location, self.screen_center)
			#Add result to dictionary
			dictionary[i] = distance 

		#print(dictionary)
		sort_dictionary = sorted(dictionary, key=dictionary.get, reverse=False)
		closest_object = self.centers[sort_dictionary[0]]
		return closest_object

	#Move player to mine rock
	def go_to(self, rec_win):
		b = 0
		rand_pos = [[660, 500], [424, 226]]

		if len(self.centers)>0:
			
			closest_object = self.nearest_object()
			
			rec_win.move(0,0)
			rec_win.clrtobot()
			self.rec_refresh()
			rectangle(rec_win, 0, 0, 4, 20)
			rec_win.addstr(1,1, "Results", self.C_GREEN)
			#Display moving position
			rec_win.addstr(2,1, f"Moving to: {closest_object[0]}, {closest_object[1]}")
			self.rec_refresh()
			#Action 1 (Move mouse)
			pyautogui.moveTo(closest_object[0],closest_object[1],duration=0.5)
			rec_win.addstr(3,1, "click")
			#Action 2 (Movement click)
			pyautogui.click(button="left")
			self.rec_refresh()
			sleep(3.5)

		else:
			rec_win.move(0,0)
			rec_win.clrtobot()
			self.rec_refresh()
			rectangle(rec_win, 0, 0, 4, 28)
			rec_win.addstr(1,1, "No results", self.C_RED)
			#Choose "random" position to move
			b = random.randint(0,1)
			
			#Display moving position
			rec_win.addstr(2,1, f"Stuck, moving to: {rand_pos[b][0]}, {rand_pos[b][1]}")
			self.rec_refresh()
			
			#Action 1 (Move mouse)
			pyautogui.moveTo(rand_pos[b][0],rand_pos[b][1],duration=0.5)
			rec_win.addstr(3,1, "click")
			self.rec_refresh()
			
			#Action 2 (Movement click)
			pyautogui.click(button="left")
			sleep(3.5)
			
			#Reset var
			b = 0

    #Thread Functions
	def start(self):
		self.stopped = False
		self.state = 0
		self.t = threading.Thread(target=self.run)
		self.t.start()
    
	def update(self, centers, rec_win, bot_status):
		self.rec_win = rec_win
		if bot_status:
			self.state = 1
		else:
			self.state = 0
			rec_win.move(2,0)
			rec_win.clrtobot()
			self.rec_refresh()
		self.centers = centers


	def stop(self):
		self.stopped = True
		print("Terminating...")


	def run(self):
		while not self.stopped:
			if self.state == 0:
				sleep(2)

			elif self.state == 1:
				self.lock.acquire()
				self.go_to(self.rec_win)
				self.lock.release()
