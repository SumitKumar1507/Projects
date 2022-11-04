# Alphabetical Order

data = []
wd = input("Enter word in upper case").upper()

[data.append(i) for i in wd]

data.sort()

print(f"Alphabetical order is {data}")
