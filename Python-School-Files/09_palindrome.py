# Write a program which will tell wheter the given word is a palindrome or not

# Palindrome : Words that are a word, phrase, or sequence that reads the same backwards as forwards.

def method_one():

	word = input("Enter word: ")
	correct_order = []
	for items in word:
		correct_order.append(items)

	reversed_order = correct_order[::-1]

	if reversed_order == correct_order:
		print(word, "is a palindrome")
	else:
		print(word, "is not a palindrome")

def method_two():

	word = input("Enter word: ")
	correct_order = [i for i in word]

	print(f"{word} is a palindrome." if correct_order == correct_order[::-1] else f"{word} is not a palindrome")

def method_three():
	str = input("Enter word: ")

	cond = str == str[::-1]
	print(f"{str} is a palindrome" if cond else f"{str} is not a palindrome")

def school_method():
	str = input("Enter word: ")
	
	x = len(str)
	var1 = 0
	var2 = 1

	for i in range(-x, 0):
		if str[-var2] == str[var1]:
			cond = True
		else:
			cond = False
		var1 += 1
		var2 += 1

	if cond == True:
		print(f"{str} is a palindrome")
	else:
		print(f"{str} is not a palindrome")

method_three()
# Both methods are exact same. method_two is some what more advanced
