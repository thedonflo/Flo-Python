print("Rock...\nPaper...\nScissors...")

while True:
    player1 = input("Player 1, make your move: ").lower()
    if player1 == "rock" or player1 == " paper" or player1 == "scissors":
        break
    else:
        print("Enter a valid move!")
print("***NO CHEATING!\n\n" * 15)

while True:
    player2 = input("Player 2, make your move: ").lower()
    if player2 == "rock" or player2 == " paper" or player2 == "scissors":
        break
    else:
        print("Enter a valid move!")

if player1 == player2:
    print("It's a tie")
elif player1 == "rock":
    if player2 == "paper":
        print("Player 2 Wins")
    else:
        print("Player 1 Wins")
elif player1 == "paper":
    if player2 == "scissors":
        print("Player 2 Wins")
    else:
        print("Player 1 Wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player 2 Wins")
    else:
        print("Player 1 Wins")



