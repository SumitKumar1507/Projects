# Write a program which will tell whether the given number is an armstrong number or not

num = input("Enter number: ")

data = [int(i) for i in num]
data_sum = [j**3 for j in data]

print(f"{num} is an armstrong number" if sum(data_sum) == int(num) else f"{num} is not an armstrong number")