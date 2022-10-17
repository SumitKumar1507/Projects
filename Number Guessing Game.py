# Write a program to simulate a number guessing game
import tempCodeRunnerFile ; tempCodeRunnerFile.clear()

import os
import time
import random

class Main():

	def __init__(self, tries, number):
		self.tries = tries
		self.number = number

	def start(self):
		print("Hello")
		# os.system("cls")
		print("Welcome to the game! Computer has guessed it's number\nGood Luck guessing it")
		self.wc()

	def wc(self):

		os.system("cls")

		if self.tries != 0:
			pass
		else:
			print(f"You ran out of tries!\nThe number was {self.number}")
			exit()

		self.user_input = input(f"Enter your guess (1-20): ")
		if self.user_input.isnumeric():
			self.user_input = int(self.user_input)
			self.logic()
		else:
			print("Invalid Choice! Restarting.")
			self.start()

	def logic(self):

		if self.user_input == self.number:
			print(f"You guessed the right number!")
			exit()
		
		elif self.user_input > self.number:
			print("You guess was a bit too high!!")
			self.tries -= 1
			time.sleep(1)
			self.wc()

		elif self.user_input < self.number:
			print("You guess was a bit too low!!")
			self.tries -= 1
			time.sleep(1)
			self.wc()

m = Main(5, random.randint(1, 20)).start()