import random
'''
1 for rock
-1 for paper
0 for sciessor
'''
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
yourdict = {"r" : 1, "p": -1, "s": 0}
reversedict = {1: "Rock", -1: "Paper", 0: "Sciessor"}

you = yourdict[youstr]

print(f"Your choice {reversedict[you]}\nComputer choice {reversedict[computer]}")

if(computer == you):
    print("It's Draw!")
else:
    if(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Lose!")
    elif(computer == -1 and you == 1):
        print("You Won!")
    elif(computer == -1 and you == 0):
        print("You Won!")
    elif(computer == 0 and you == -1):
        print("You Lose!")
    elif(computer == 0 and you == 1):
        print("You Won!")
    else:
        print("Something gonna wrong!")
    
