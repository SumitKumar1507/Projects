# Write a program to mimic a library management system

import tempCodeRunnerFile ; tempCodeRunnerFile.clear()

import time

class Main():

	choice = ["List Books", "Borrow Book", "Return Book", "Exit"]
	available_books = ["Maths", "English", "Science"]
	borrowed_book = []
	returned_book = []

	def __init__(self, name):
		self.name = name
	
	def start(self):
		tempCodeRunnerFile.clear()

		print(f"Welcome to the Library {self.name}\nWhat your want to do: ")

		for n, i in enumerate(self.choice, start=1):
			print(f"{n}. {i}")

		user_choice = input("Enter your choice: ")
		while user_choice not in ["1", "2", "3", "4"]:
			print("That's an invalid choice. Restarting!!")
			self.start()
		
		if user_choice == "1":
			print("Available Books are: ")
			for n, i in enumerate(self.available_books, start=1):
				print(f"{n}. {i}")
		
		



m = Main("Sumit")
