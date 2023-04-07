import threading
from time import sleep
import pyautogui
import random
import math
import cv2
import numpy

def get_center(rectangles):
    centers = []
    for i in rectangles:
        x = int((i[0]+(i[0]+i[2]))/2)
        y = int((i[1]+(i[1]+i[3]))/2)
        centers.append([x, y])
        #print(centers)
    return centers


def get_rectangles(results):
    rectangles = []
    x = results.xyxy[0].tolist()
    for i in x:
        rectangles.append(i[:-2])
    return rectangles


class Move:
	def __init__(self):
		#Lock the thread
		self.lock = threading.Lock()


		
	def nearest_object(self, screen_center):
		dictionary = {}
		for i in range(len(self.centers)):
			object_location = self.centers[i]
			#Calculate distance between an object and the character
			distance = math.dist(object_location, screen_center)
			#Add result to dictionary
			dictionary[i] = distance 

		#print(dictionary)
		sort_dictionary = sorted(dictionary, key=dictionary.get, reverse=False)
		closest_object = self.centers[sort_dictionary[0]]
		return closest_object

	#Move player to mine rock
	def go_to(self, waiting_time, screen_center):
		b = 0
		rand_pos = [[660, 500], [424, 226]]

		if len(self.centers)>0:
			print(f"Waiting {waiting_time} seconds")
			#Find the closest object to the player
			closest_object = self.nearest_object(screen_center)
			print(closest_object)
			
			#Display moving position
			print(f"Moving to: {closest_object[0]}, {closest_object[1]}")

			#Action 1 (Move mouse)
			pyautogui.moveTo(closest_object[0],closest_object[1],duration=0.5)
			print("click\n")
			#Action 2 (Movement click)
			pyautogui.click(button="left")
			sleep(waiting_time)

		else:
			print(f"Waiting 2.5 seconds")
			print("No results")
			#Choose "random" position to move
			b = random.randint(0,1)
			
			#Display moving position
			print(f"Stuck, moving to: {rand_pos[b][0]}, {rand_pos[b][1]}")
			
			#Action 1 (Move mouse)
			pyautogui.moveTo(rand_pos[b][0],rand_pos[b][1],duration=0.5)
			print("click\n")

			
			#Action 2 (Movement click)
			pyautogui.click(button="left")
			sleep(2.5)
			
			#Reset var
			b = 0

    #Thread Functions
	def start(self):
		self.stopped = False
		self.state = 0
		self.t = threading.Thread(target=self.run)
		self.t.start()
    
	def update(self, centers, bot_status, waiting_time, screen_center):
		self.screen_center = screen_center
		self.waiting_time = waiting_time
		#print(f"Bot Status Thread: {bot_status}")
		if bot_status==True:
			self.state = 1
		elif bot_status==False:
			self.state = 0
		self.centers = centers


	def stop(self):
		self.stopped = True
		print("Terminating...")


	def run(self):
		while not self.stopped:
			if self.state == 0:
				sleep(3)

			elif self.state == 1:
				self.lock.acquire()
				self.go_to(self.waiting_time, self.screen_center)
				self.lock.release()
