# Count and display the number of vowels, consonants, uppercase, lowercase characters in string.

def main():

    word = input("Enter word: ")

    upper = [i for i in word if i.isupper()]
    lower = [i for i in word if i.islower()]
    consonants = [i for i in word if i not in ["a", "i", "o", "e", "u"]]
    vowels = [i for i in word if i in ["a", "i", "o", "e", "u"]]

    print(f"Vowels : {vowels} \nConsonants : {consonants} \nUpper : {upper} \nLower : {lower}")

# Find the largest/smallest number in a list/tuple
# List : Lists are used to store multiple values in one variable. The elements of a list can be modified
# Tuple : Same as list but the elements are NOT modifiable

def main_2():

    data = [int(input("Enter number: ")) for _i in range(5)]
    print(f"Minimum Value : {min(data)} \nMaximum Value : {max(data)}")

# Input a list/tuple of elements, search for a given element in the list/tuple.

def main_3():

    data = [int(input("Enter number: ")) for _i in range(5)]
    print("Data received successfully")

    search = int(input("Enter the element you want to search for: "))

    print(f"Element found at index {data.index(search)}" if search in data else "Element not found")

# Input a list of numbers and find the smallest and largest number from the list.

def main_4():

    data = [int(input("Enter number: ")) for _i in range(5)]
    print(f"Max is {max(data)} \nMin is {min(data)}")

