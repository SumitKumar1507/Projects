# Make a rock paper scissor program
import tempCodeRunnerFile ; tempCodeRunnerFile.clear()

import os
import time
import random

class Main():

	options = ["Rock", "Paper", "Scissor"]

	def __init__(self, name):
		self.name = name
		self.tries = 5
		self.score = 0
		self.cs = 0

	def start(self):
		os.system("clear")
		print("Welcome to the game. Computer has made it's choice.")
		self.wc()

	def wc(self):

		os.system("clear")

		if self.tries != 0:
			pass
		else:
			print("You ran out of tries!!")
			print(f"Your final score was: {self.score} - {self.cs}")
			exit()

		self.choice = input("Enter your choice (4 to exit): ").capitalize()
		if self.choice not in self.options:
			if self.choice == "4":
				exit()
			else:
				print("Invalid Choice!! Restarting...")
				self.start()
		else: pass

		self.logic()
	
	def logic(self):

		self.cc = random.choice(self.options)

		if self.choice == self.cc:
			print("Game Tied")
			time.sleep(1.5)
			self.tries -= 1
			self.score += 0
			self.wc()
		
		elif self.choice == "Rock" and self.cc == "Scissor" or self.choice == "Paper" and self.cc == "Rock" or self.choice == "Scissor" and self.cc == "Paper":
			print(f"{self.name} won the game!!")
			time.sleep(1.5)
			self.tries -= 1
			self.score += 1
			self.wc()

		else:
			print("Computer won the game!")
			time.sleep(1.5)
			self.tries -= 1
			self.cs += 1
			self.wc()
		
m = Main(input("Enter your name: ")).start()

