import random
print("Hello! Would you like to play Rock, Paper, Scissors?")
while True:
    # The player chooses between rock, paper, scissors
    user_action = input("Enter a choice (rock, paper, scissors): ")

    # Computer chooses between rock, paper, scissors
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    # Text for player's and computer's action
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    # Determine the winner
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("That's not a valid play. Check your spelling!")
    #Ask to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            break
        elif play_again.lower() == "n":
            print("Thanks for playing")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
