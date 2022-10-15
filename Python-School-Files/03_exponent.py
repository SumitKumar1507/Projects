# Write a program to find a raised to b.

def school_method():
	num1 = int(input("Enter 1st number: "))
	num2 = int(input("Enter 2nd number: "))

	for i in range(1, num2+1):
		num1 = num1 * i

	print(num1)

def my_method():
	q = ["number", "exponent"]
	numbers = [int(input(f"Enter {q[i]}: ")) for i in range(2)]
	print(f"The answer is {numbers[0]**numbers[1]}")

my_method()
