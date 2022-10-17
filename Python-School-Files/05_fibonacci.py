# Write a program to print the fibanocci series

x, y = 0, 1
length = int(input("Enter length of the series: "))

print(f"{x}\n{y}")
for i in range(1, length+1):
	z = x + y
	print(z)
	x, y = y, z
