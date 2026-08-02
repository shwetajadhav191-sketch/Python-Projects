import random

user_score = 0
computer_score = 0
max_tries = 5
tries = 0

while tries < max_tries:
    tries += 1
    user = int(input("""\nEnter your choice(1-3): 
    1.rock
    2.paper
    3.scissors\n"""))

    if user == 1:
        user = "rock"
    elif user == 2:
        user = "paper"
    elif user == 3:
        user = "scissors"
    else:
        print("invalid input!")

    computer = random.choice(['rock','paper','scissors'])

    print("you: ",user)
    print("computer: ",computer)

    if user == computer:
        print("Draw!")
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        user_score += 1
    else:
        computer_score += 1

    if user_score > computer_score:
        print("\nYOU WIN!\n")
        print("you: ",user_score)
        print("computer: ",computer_score)
    elif user_score < computer_score:
        print("\nYOU LOOSE\n")
        print("you: ",user_score)
        print("computer: ",computer_score)
    else:
        print("\nTie\n")
        print("you: ",user_score)
        print("computer: ",computer_score)
