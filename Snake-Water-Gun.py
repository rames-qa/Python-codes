import random
print("\n Game Logic (Result Matrix)\n")
print("User \\ Computer\tSnake (s)\tWater (w)\tGun (g)")
print("Snake (s)\t\tTie (0)\t\tWin (1)\t\tLose (-1)")
print("Water (w)\t\tLose (-1)\tTie (0)\t\tWin (1)")
print("Gun (g)\t\t\tWin (1)\t\tLose (-1)\tTie (0)\n")
options = ["s", "w", "g"]
comp = random.choice(options)
user = input("Snake (s), Water (w), Gun (g)\nEnter (s/w/g)= ").lower()
if user not in options:
    print("Invalid input!")
else:
    print(f"\nComputer: {comp}\nYou: {user}")
    if comp == user:
        print("It's a tie!")
    elif (user == "s" and comp == "w") or \
         (user == "w" and comp == "g") or \
         (user == "g" and comp == "s"):
        print("You win!")
    else:
        print("You lose!")