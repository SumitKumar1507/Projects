# write a program to mimic a library management system

import tempCodeRunnerFile ; tempCodeRunnerFile.clear()

import time

class Main():

	options = ["List Books", "Borrow Books", "Return Books", "Exit"]

	def __init__(self, name):
		self.name = name

	def start(self):
		tempCodeRunnerFile.clear()

		print(f"Welcome to the Library, {self.name}")

		for n, i in enumerate(self.options, start=1):
			print(f"{n}. {i}")

		user_choice = input("Enter your choice: ")
		
		while user_choice not in ["1", "2", "3", "4"]:
			print(f"Invalid Choice!! Restarting!")
			time.sleep(0.5)
			self.start()

		if user_choice == "List" or user_choice == "1":
			pass
		elif user_choice == "Borrow" or user_choice == "2":
			pass
		elif user_choice == "Return" or user_choice == "3":
			pass
		elif user_choice == "Exit" or user_choice == "4":
			pass

		
		

m = Main("Sumit").start()
		
