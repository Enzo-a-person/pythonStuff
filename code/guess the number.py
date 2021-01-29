import random 
n = random.randint(0,10) #creates a number between 0 or 10
x = int(input("try to guess my number :) : "))
if x > 10: #detects if the number is too big
    print ("the number is too big try again :\ ")
    exit()
    
if x < 0: #detects if the number is too small
    print ("the number is too small please try again :\ ")
    exit()

if x != n: #detects if you lost
    print ("you lost sorry try again :( ")
    exit()
    
if x == n : #detects if you win
    print ("you won yay :) ")
    exit()

