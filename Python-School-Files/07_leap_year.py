# Write a program to check whether the given year is a leap year or not

def school_method():
	year = int(input("Enter year: "))
	if year % 4 == 0:
		print(year, " is a leap year")
	else:
		print(year, " is not a leap year")

def my_method():
	x = int(input("Enter year: "))
	test = [True if x%4==0 else False]
	print(f"{x} is a leap year" if test else f"{x} is not a leap year")

my_method()
