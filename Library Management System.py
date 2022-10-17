# Write a program to mimic a Library Management System
import tempCodeRunnerFile 

import os
import time

# print(time.strftime("%d %h %Y %H:%S:%M"))

class Main():

	choices = {
		"1" : "View Books",
		"2" : "Borrow Books",
		"3" : "Return Books",
		"4" : "Exit"
	}
	access = {
		"1" : "Add Books",
		"2" : "Remove Books"
	}
	return_books = []
	borrowed_books = []
	available_books = ["Physics", "Chemistry", "Maths", "English"]

	tempCodeRunnerFile.clear()

	def __init__(self, name:str = input("Enter your name:")):
		self.name = name
		self.time = time.strftime("%d %h %Y %H:%S:%M")

	def start(self):

		tempCodeRunnerFile.clear()

		if self.admin1 != 0 or self.admin2 != 0:
			self.admin()

		print(f"Welcome to our Library, {self.name}\t\t\t\t\t\t{self.time}\n")

		for key, values in self.choices.items():
			print(f"{key}. {values}")
		
		self.book = input("\nEnter your choice (1-4): ")

		if self.book not in self.choices.keys():
			if self.book == "5":
				self.start()
			else:
				print("The entered option was not found. Restarting!")
				time.sleep(1)
				os.system("clear") ; self.start()
		else:
			self.logic()

	def logic(self):

		if self.book == "1":
			print("\nAvailable books are: ")

			if len(self.borrowed_books) != 0:
				print(self.borrowed_books)
				for x in self.borrowed_books:
					self.available_books.remove(x)
	
			for num, items in enumerate(self.available_books, start = 1):
				print(f"{num}. {items}")

			time.sleep(2.5)
			self.start()
		
		elif self.book == "2":
			b_book = input("Which book you want to borrow (book's name): ").capitalize()
			if b_book in self.available_books:
				print(f"{b_book} successfully issued to {self.name}")
				self.borrowed_books.append(b_book)
			else:
				print(f"{b_book} was not found in our database!! Exitting")
			time.sleep(1.2)
			self.start()

		elif self.book == "3":
			r_book = input("Which book you want to return (book's name): ").capitalize()
			if r_book in self.borrowed_books:
				print(f"{r_book} successfully returned by {self.name}")
				self.borrowed_books.remove(r_book)
				self.available_books.append(r_book)
			else:
				print(f"{r_book} was never borrowed from us!! Exitting")
			time.sleep(1.2)
			self.start()

m = Main().start()