import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors:  ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        print("Match draw")
    elif user == 'r':
        if computer == 'p':
            print("Computer wrapper your rock with paper. Computer Wins.")
        elif computer == 's':
            print("You breaked the scissors, You win!")
    elif user == 'p':
        if computer == 'r':
            print("You wrapped rock with paper. You win!")
        elif computer == 's':
            print("Computer cutted your paper. Computer wins")
    elif user == "s":
        if computer == 'r':
            print("Computer breaks the scissors, computer wins.")
        elif computer == 'p':
            print("You cutted the paper. You win!")


play()
