#rock paper scissor game
import random

variables = ["rock", "paper", "scissors"]
computer_choice = random.choice(variables)
player_choice = 0

def Game():
    player_choice = input("Which move are you going to do? : ")
    try:
        if str(computer_choice).lower() == str(player_choice).lower():
            print(f"Computer : {computer_choice}")
            print(f"You : {player_choice}")
            print("Draw!")
        elif str(computer_choice).lower() == "rock" and str(player_choice).lower() == "scissors":
            print(f"Computer : {computer_choice}")
            print(f"You : {player_choice}")
            print("Computer WINS!")
        elif str(computer_choice).lower() == "paper" and str(player_choice).lower() == "scissors":
            print(f"Computer : {computer_choice}")
            print(f"You : {player_choice}")
            print("You WIN!")
        elif str(computer_choice).lower() == "scissors" and str(player_choice).lower() == "rock":
            print(f"Computer : {computer_choice}")
            print(f"You : {player_choice}")
            print("You WIN!")
        elif str(computer_choice).lower() == "rock" and str(player_choice).lower() == "paper":
            print(f"Computer : {computer_choice}")
            print(f"You : {player_choice}")
            print("You WIN!")
        else:
            print("Invalid Input : You need to input Rock, Paper or Scissors!")
            Game()
    except Exception:
        print("You need to input Rock, Paper or Scissors!")
        Game()

Game()

play_again = input("Rematch? (yes/no) : ").lower()
if play_again == "yes":
    Game()
else:
    exit()
