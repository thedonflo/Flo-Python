# print("Player, make your move:")
# print("Computer plays scissors")
# print("Please enter a valid move!")
#

import random
computer = ""
generate = random.randint(0, 2)
print(computer)
if generate == 0:
    computer = "rock"
elif generate == 1:
    computer = "paper"
else:
    computer = "scissors"

print("Rock...\nPaper...\nScissors...")

while True:
    player1 = input("Player, make your move: ").lower()
    if player1 == "rock" or player1 == "paper" or player1 == "scissors":
        break
    else:
        print("Enter a valid move!")
print("***NO CHEATING!\n\n" * 15)
print(f"Computer plays {computer}")

# while True:
#     computer = input("Computer, make your move: ").lower()
#     if computer == "rock" or computer == " paper" or computer == "scissors":
#         break
#     else:
#         print("Enter a valid move!")

if player1 == computer:
    print("It's a tie")
elif player1 == "rock":
    if computer == "paper":
        print("Computer Wins")
    else:
        print("Player 1 Wins")
elif player1 == "paper":
    if computer == "scissors":
        print("Computer Wins")
    else:
        print("Player 1 Wins")
elif player1 == "scissors":
    if computer == "rock":
        print("Computer Wins")
    else:
        print("Player 1 Wins")





