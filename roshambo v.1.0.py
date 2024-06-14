import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = str(input("Enter rock, paper, or scissors (q to quit): "))
    if user_choice == "q":
        print("Thanks for playing and see you soon!")
        quit()

    if user_choice not in options:
        print("Invalid input, please enter from the choices of 'rock', 'paper', or 'scissors'.")
        continue

    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    print(f"Computer choice: {computer_choice}")

    if user_choice == "rock" and computer_choice == "scissors":
        print("User wins!")
        user_wins = user_wins + 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("User wins!")
        user_wins = user_wins + 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("User wins!")
        user_wins = user_wins + 1
    elif user_choice == "scissors" and computer_choice == "scissors":
        print("It's a tie!")
        user_wins = user_wins + 1
    elif user_choice == "rock" and computer_choice == "rock":
        print("It's a tie!")
        user_wins = user_wins + 1
    elif user_choice == "paper" and computer_choice == "paper":
        print("It's a tie!")
        user_wins = user_wins + 1
    else:
        print("Computer wins!")