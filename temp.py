import tempCodeRunnerFile

data = ["act", "arrive", 1, 3, "car", "orange"]
empty = []

def attempt():
	for i in data:
		if type(i) == str:
			for j in i:
				if j.startswith("a"):
					empty.append(i)

	print(empty)

def second():
	for i in data:
		if type(i) == str:
			if i.startswith("a"):
				empty.append(i)
	print(empty)

def third():
	for i in data:
		if type(i) == str:
			if i[0] == "a":
				empty.append(i)
	print(empty)

def fourth():
	tempCodeRunnerFile.clear()

	a = input("Enter anything: ")
	print(a[::-1])

fourth()