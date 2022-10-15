# Write a program to print the table of a number

def easy_method():
	num = int(input("Enter number: "))
	for i in range(1, 11):
		print(num*i)

def medium_method():
	num = int(input("Enter number: "))
	for i in range(1, 11):
		print(f"{num} x {i} = {num*i}")

def hard_method():
	num = int(input("Enter number: "))
	table = [num*i for i in range(1, 11)]
	for numbers, items in enumerate(table):
		print(f"{num} x {numbers+1} = {items}")

