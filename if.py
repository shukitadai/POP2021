import random

choices = ["Rock","Paper","Scissors"]


playerChoice = ""
playerScore = 0

computerChoice = ""
computerScore = 0

print("Let's play rock, paper, scissors!")
for x in range(1,4):
    computerChoice = choices[random.randint(0,2)]
    print("\n")
    playerChoice = input("Enter [R], [P], or [S] \n")
    #use if to see who won the match
    if playerChoice == "R" and computerChoice == "Scissors":
        playerScore += 1

    if playerChoice == "R" and computerChoice == "Paper":
        computerScore += 1
        
    if playerChoice == "R" and computerChoice == "Rock":
        playerScore += 0

    if playerChoice == "P" and computerChoice == "Rock":
        playerScore += 1

    if playerChoice == "P" and computerChoice == "Paper":
        playerScore += 0

    if playerChoice == "P" and computerChoice == "Scissors":
        computerScore += 1

    if playerChoice == "S" and computerChoice == "Rock":
        computerScore += 1

    if playerChoice == "S" and computerChoice == "Paper":
        playerScore += 1
        
