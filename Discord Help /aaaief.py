
import time
import random
end = 0
score = 1
n = random.randint(1 , 20)
totaltime = 0
num = [x for x in range(1, 10+1)]
n = random.randint(1, len(num))
num.pop(n)
def question(q , o1 , o2 , o3 , o4 , ans):
    global score
    global end
    print("Question no:" , score)
    time.sleep(1)
    print(q)
    time.sleep(.5)
    print("A)" , o1)
    time.sleep(.5)
    print("B)" , o2)
    time.sleep(.5)
    print("C)" , o3)
    time.sleep(.5)
    print("D)" , o4)
    time.sleep(.5)
    print("You have ten seconds to answer.")
    starttime = round(time.time())
    userans = input("")
    endtime = round(time.time())
    totaltime = endtime-starttime
    if totaltime > 10:
        print("Time is up! Your score is" , score-1)
        end = 1
    elif userans == ans:
        print("Thats correct!")
        score += 1
        n = random.randint(1 , len(num))
        num.pop(n)
    else:
        print("Thats the wrong answer! Your score is" , score-1)
        end = 1
		
while True:
    if end != 1:
        time.sleep(1)
        if n == 1:
            question("What is the country with the biggest size?" , "Canada" , "USA" , "Russia" , "China" , "C")
        elif n == 2:
            question("What is the country with the most population?" , "India" , "China" , "USA" , "Nigeria" , "B")
        elif n == 3:
            question("What is the country with the smallest size?" , "Vatican City" , "San Marino" , "Malta" , "Monaco" , "A")
        elif n == 4:
            question("What is the country with the most obesity rate?" , "USA" , "Vanuatu" , "Germany" , "Nauru" , "D")
        elif n == 5:
            question("What is the country with the most nukes?" , "China" , "USA" , "India" , "Russia" , "D")
        elif n == 6:
            question("What is the country with the least population desinsty?" , "Canada" , "Mongolia" , "Australia" , "Iceland" , "B")
        elif n == 7:
            question("What is the country with the most Islands?" , "Sweden" , "Canada" , "Norway" , "Australia" , "A")
        elif n == 8:
            question("What is the country with the most population desinsty?" , "China" , "Bangladesh" , "Monaco" , "Sri Lanka" , "C")
        elif n == 9:
            question("What is the country with the most total military personel?" , "USA" , "China" , "Vietnam" , "North Korea" , "C")
        elif n == 10:
            question("What is the country with the coumty with the most GDP?" , "Luxembourg" , "Qatar" , "Saudi Arabia" , "Liechestein" , "B")