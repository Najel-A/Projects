import random
import math


def generateRandInt():
    randomNum = random.randint(1, 3)
    return randomNum


def getComputerChoice(randomNum):
    computerChoice = 0
    if randomNum == 1:
        computerChoice = "rock"
    elif randomNum == 2:
        computerChoice = "paper"
    elif randomNum == 3:
        computerChoice = "scissors"

    return computerChoice


def getUserChoice():
    user_choice = input("Please enter rock, paper or scissors: ")
    return user_choice.lower()


def determineWinner(user_choice, computerChoice):
    rockMessage = "Rock beats scissors!"
    paperMessage = "Paper beats rock!"
    scissorsMessage = "Scissors beats paper!"
    winner = "No winner!"
    message = ""

    if computerChoice == "rock" and user_choice == "scissors":
        winner = "Computer"
        message = rockMessage
    elif computerChoice == "scissors" and user_choice == "rock":
        winner = "You"
        message = rockMessage

    if computerChoice == "paper" and user_choice == "rock":
        winner = "Computer"
        message = paperMessage
    elif computerChoice == "rock" and user_choice == "paper":
        winner = "You"
        message = paperMessage

    if computerChoice == "scissors" and user_choice == "paper":
        winner = "Computer"
        message = scissorsMessage
    elif computerChoice == "paper" and user_choice == "scissors":
        winner = "You"
        message = scissorsMessage

    if computerChoice == "rock" and user_choice == "rock":
        winner = "No Contest"
        message = "Draw!"
    elif computerChoice == "paper" and user_choice == "paper":
        winner = "No Contest"
        message = "Draw!"
    elif computerChoice == "scissors" and user_choice == "scissors":
        winner = "No Contest"
        message = "Draw!"

    return winner, message


def startAgain():
    randomNum = generateRandInt()
    computerChoice = getComputerChoice(randomNum)
    userChoice = getUserChoice()
    print("The computer chose", computerChoice)
    winner, message = determineWinner(userChoice, computerChoice)

    if winner == "No Contest":
        print(winner + "!")
    elif winner != "no winner":
        print(winner, "won! (" + message + ")")

    return winner


def main():
    randomNum = generateRandInt()
    computerChoice = getComputerChoice(randomNum)
    userChoice = getUserChoice()
    while (userChoice != "rock") and (userChoice != "paper") and (userChoice != "scissors"):
        print("Invalid entry! Try again.")
        userChoice = getUserChoice()
    print("The computer chose", computerChoice)
    winner, message = determineWinner(userChoice, computerChoice)

    if winner == "No Contest":
        print(winner + "!")
    elif winner != "no winner":
        print(winner, "won! (" + message + ")")

    while winner == "no winner":
        winner = startAgain()


print('''Welcome to Rock, Paper, Scissors!
The rules are simple, type in either rock, paper, or scissors.
If you win, the program will display "You Won!", but if you lose it will display "Computer Won!"
In the event of a draw, you'll repeat the process and play until you win or lose.
Good Luck! Enjoy! Have Fun!
''')

main()
