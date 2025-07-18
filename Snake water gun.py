import random

'''
1 for snake 
-1 for water 
0 for gun
'''
youdict = {"s": 1, "w": -1, "g": 0}
computer = random.choice([1, -1, 0])
youinput = input("Enter your choice s for snake w for water and g for gun: ")
you = youdict.get(youinput)

if you is None:
    print("Invalid Input!")
elif you == computer:
    print("It's a Draw!")
else:
    if(computer == 1 and you == 0) or (computer == -1 and you == 1) or (computer == 0 and you == -1):
        print("You Win!")
    else:
        print("You Lose")
