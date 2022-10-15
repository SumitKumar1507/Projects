# What are nested loops??
# A nested loop is a loop inside the body of the outer loop. The inner or outer loop can be any type, such as a while loop or for loop.

def main():

    for i in range(1, 5): # this loop will run from 1 to 4, changing it's value per iteration
        
        print(i)
        for j in range(1, 4): # this loop will run from 1 to 3, chaning it's value P.I.
            print(j)
    
    # As soon as we execute the program, the first loop gets executed and runs the print function inside it. In first iteration, the value of i will be 1. But there's an another for loop inside the existing loop. The second for loop will execute it's function until unless the condition becomes false. As soon as the condition becomes false, it will exit out of the current loop and the parent loop will be execute again n times (n = defined tries).

    # So the output is:
    # 1, 1, 2, 3, 2, 1, 2, 3, 3, 1, 2, 3, 4, 1 , 2 ,3

if __name__ == "__main__":
    main()