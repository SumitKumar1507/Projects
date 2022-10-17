# Write a program which will tell wheather a number is a perfect number or not

def perfect_number(num):

	data = []
	for i in range(1, num+1):
		if num % i == 0 and i != num:
			data.append(i)

	check = [True if sum(data) == num else False]
	print(f"{num} is a perfect number" if True in check else f"{num} is not a perfect number")
