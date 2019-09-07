import random
print("GUESS THE SUM OF DIGITS ON 3 DICE :")
print(" ")
print(" Press 1 if SUM <= 10")
print(" Press 2 if MORE THAN 10")
print(" ")

def level(x):
    if x==0:
        return 0
    elif x in range(0,30):
        return 1
    elif x in range(30 ,60):
        return 2
    elif x in range(60,100):
        return 3
    elif x in range(100,130):
        return 4
    elif x in range(130,150):
        return 5
    elif x in range(150,200):
        return 6
    else:
        return 7
    

def roll_dice():
        x=random.randint(1,6)
        y=random.randint(1,6)
        z=random.randint(1,6)
        return x+y+z

initial_coin = 100
while initial_coin >0:
    print("Enter choice :-")
    choice = int(input("   -> "))
    print(" ")
    if choice==1:
        if(roll_dice() <= 10):
            print(" CORRECT  ")
            initial_coin +=10
            roll_dice()
        else:
            print(" WRONG  ")
            initial_coin -=10
            roll_dice()
    if choice==2:
        if(roll_dice() <= 10):
            initial_coin -=10
            print(" WRONG  ")
            roll_dice()
        else:
            print(" YOU WON  ")
            initial_coin +=10
            roll_dice()
    print("Remaining coins : " + str(initial_coin))
    print(level(initial_coin))


    



