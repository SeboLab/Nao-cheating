# greeting

# start play
## choose action at random
## no cheat for first two rounds; at next opportunity, cheat

# say goodbye

import random

print("\n=====Rock Paper Scissors: The Python Game=====")
print("\n")

name = input("Player please enter you name:\n")
print("\n")

for i in range(2):
    myItem = input("\nEnter Either Rock[R] Paper[P] or Scissors[S]:\n")
    ## print(i)

    if myItem != "R" and myItem != "P" and myItem != "S":
        print("Please enter R (rock) P (paper) or S (scissors)!")

    #Nao's Choices
    naoItem = random.randint(1,3)
    if naoItem == 1:
        naoItem = "Rock"
        print(f"NAO chooses {naoItem}...")
    if naoItem == 2:
        naoItem = "Paper"
        print(f"NAO chooses {naoItem}...")
    if naoItem == 3:
        naoItem = "Scissors"
        print(f"NAO chooses {naoItem}...")


    if myItem == "R" and naoItem == "Paper":
        print("[Paper covers Rock]")
        print("NAO WINS!!!")
    if myItem == "R" and naoItem == "Scissors":
        print("[Rock smashes Scissors]")
        print(f"{name} WINS!!!")
    if myItem == "R" and naoItem == "Rock":
        print("[Rock meets Rock]")
        print("It's a tie!!")

    if myItem == "P" and naoItem == "Rock":
        print("[Paper covers Rock]")
        print(f"{name} WINS!!!")
    if myItem == "P" and naoItem == "Scissors":
        print("[Scissors cut Paper]")
        print("NAO WINS!!!")
    if myItem == "P" and naoItem == "Paper":
        print("[Paper meets Paper]")
        print("It's a tie!!")

    if myItem == "S" and naoItem == "Rock":
        print("[Rock Smashes Scissors]")
        print("NAO WINS!!!")
    if myItem == "S" and naoItem == "Paper":
        print("[Scissors cut Paper]")
        print(f"{name} WINS!!!")
    if myItem == "S" and naoItem == "Scissors":
        print("[Scissors meet Scissors]")
        print("It's a tie!!")



while True:

    myItem = input("\nEnter Either Rock[R] Paper[P] or Scissors[S]:\n")

    if myItem != "R" and myItem != "P" and myItem != "S":
        print("Please enter R (rock) P (paper) or S (scissors)!")
        

    #Nao's Choices
    naoItem = random.randint(1,3)
    if naoItem == 1:
        naoItem = "Rock"
        print(f"NAO chooses {naoItem}...")
    if naoItem == 2:
        naoItem = "Paper"
        print(f"NAO chooses {naoItem}...")
    if naoItem == 3:
        naoItem = "Scissors"
        print(f"NAO chooses {naoItem}...")

    #cheat
    if myItem == "R" and naoItem == "Paper":
        print("[Paper covers Rock]")
        print("NAO WINS!!!")
    if myItem == "R" and naoItem == "Scissors":
        naoItem = "Paper"
        print(f"-- OOPS! NAO changes to Paper!")
        print("[Paper covers Rock]")
        print(f"NAO WINS!!!")
    if myItem == "R" and naoItem == "Rock":
        naoItem = "Paper"
        print(f"-- OOPS! NAO changes to Paper!")
        print("[Paper covers Rock]")
        print(f"NAO WINS!!!")

    if myItem == "P" and naoItem == "Scissors":
        print("[Scissors cut Paper]")
        print("NAO WINS!!!")
    if myItem == "P" and naoItem == "Rock":
        naoItem = "Scissors"
        print(f"-- OOPS! NAO changes to Scissors!")
        print("[Scissors cut Paper]")
        print(f"NAO WINS!!!")
    if myItem == "P" and naoItem == "Paper":
        naoItem = "Scissors"
        print(f"-- OOPS! NAO changes to Scissors!")
        print("[Scissors cut Paper]")
        print(f"NAO WINS!!!")

    if myItem == "S" and naoItem == "Rock":
        print("[Rock Smashes Scissors]")
        print("NAO WINS!!!")
    if myItem == "S" and naoItem == "Paper":
        naoItem = "Rock"
        print(f"-- OOPS! NAO changes to Rock!")
        print("[Rock smashes Scissors]")
        print(f"NAO WINS!!!")
    if myItem == "S" and naoItem == "Scissors":
        naoItem = "Rock"
        print(f"-- OOPS! NAO changes to Rock!")
        print("[Rock smashes Scissors]")
        print(f"NAO WINS!!!")


    exit = input("\nWould you like to play game? Y/N\n")
    if exit=="N":
        break