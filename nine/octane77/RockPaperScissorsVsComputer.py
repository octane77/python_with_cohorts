import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)

Player1Score = 0
ComputerScore = 0

print("Rock, Paper, Scissors")
print("The rules are simple, Rock breaks Scissors, Paper wraps Rock, Scissors cuts Paper")
print("We're going 10 rounds")

for i in range(10):

    user_1 = str(input("Ready, Player 1? Rock, Paper, Scissors?: "))
    print("Computer: {}".format(computer))
    if user_1 == "Rock" and computer == "Scissors":
        Player1Score += 1
        print("Player 1 Wins this round")
    elif user_1 == "Scissors" and computer == "Paper":
        Player1Score += 1
        print("Player 1 Wins this round")
    elif user_1 == "Paper" and computer == "Rock":
        Player1Score += 1
        print("Player 1 Wins this round")

    else:
        ComputerScore += 1
        print("Computer Wins this round")

