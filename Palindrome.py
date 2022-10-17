# write a program to simulate a palindrome
# Logic: you should check each and every word of the string
# Test Case: pratap, madam, arora, hello world
import tempCodeRunnerFile ; tempCodeRunnerFile.clear()

class Main():

	def __init__(self, word:str):
		self.cond = []
		self.var2 = -1
		self.word = word.lower()

	def logic(self):
		for i in range(len(self.word)-1):
			if self.word[i] == self.word[self.var2]:
				self.cond.append(True)
			else:
				self.cond.append(False)
			self.var2 -= 1
		self.check()

	def check(self):
		if False in self.cond: 
			print(f"{self.word} is not a palindrome")
		else: 
			print(f"{self.word} is a palindrome")

m = Main(input("Enter word: ")).logic()
