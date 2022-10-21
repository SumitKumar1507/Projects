# Pattern Question
from tempCodeRunnerFile import clear; clear()

def question_one():

	for i in range(1, 4+1):
		for j in range(1, i+1):
			print(i, "\t", end="")
		print("\n")

# Fibanocci series

def question_two():

	limit = int(input("Enter limit: "))

	var1, var2 = 0,1 
	print(var1,"\n",var2)

	for i in range(limit+1):
		x = var1 + var2; print(x)
		var1 = var2
		var2 = x

question_two()
		