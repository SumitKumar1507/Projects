# Write a program to find the factorial of a number
from math import factorial

def school_method():
	num = int(input("Enter number: "))
	fact = 1

	for i in range(1, num+1):
		fact = fact * i

	print(fact)

def my_method():
	num = int(input("Enter number: "))
	print(factorial(num))

# You decide which one is better!!
