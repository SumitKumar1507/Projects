# Write a program to compute hcf of two numbers

def main(x:int, y:int):

    smaller = x if x < y else y
    hcf = [i if x % i == 0 and y % i == 0 else None for i in range(1, smaller+1)]
    
    print(f"HCF is {hcf[-1]}" if hcf[-1] != None else f"HCF is 1")

def main_2(x, y):
    
    if x < y:
        smaller = x
    else: 
        smaller = y

    for i in range(1, smaller+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    print(f"HCF is {hcf}")

if __name__ == "__main__":
    main(43, 53)
    main_2(43, 53)