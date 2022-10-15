# Write a program which will tell whether the given number is a prime number or not

def method_one():

	num = int(input("Enter number: "))
	flag = False

	if num > 1:
		for i in range(2, num):
			if num%i == 0:
				flag = True
				break
	
	if flag:
		print(num, "is not a prime number")
	else:
		print(num, "is a prime number")


def method_two():

	num = int(input("Enter number: "))
	if num < 1: exit()

	flag = [True if num % i == 0 else False for i in range(2, num)]
	print(f"{num} is not a prime number" if True in flag else f"{num} is a prime number.")

# Method 1 and Method 2 are exact same. The second method is sort of a compressed version of method one. I don't know what am i even saying at this point.  

def method_three():

	num = int(input("Enter number: "))

	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				print("Not Prime Number")
				break
			else:
				print("Prime Number")
				break

