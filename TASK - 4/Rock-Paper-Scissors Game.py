"""
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
Game Logic: Determine the winner based on the user's choice and the computer's choice.
 Rock beats scissors, scissors beat paper, and paper beats rock.
 Display Result: Show the user's choice and the computer's choice.
 Display the result, whether the user wins, loses, or it's a tie.
 Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and feedback
 """
 
import random
import datetime
import os

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    choice = input("Enter your choice (1 = rock, 2 = paper, 3 = scissors): ")
    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice. Please enter 1 for rock, 2 for paper, or 3 for scissors: ")
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    return choices[choice]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def play_game():
    user_score = 0
    computer_score = 0
    game_results = []
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1
        
        game_results.append(f"You: {user_choice}, Computer: {computer_choice}, Result: {result}")
        print(f"Score -> You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            break

    # Save game results to a text file
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y and %H-%M-%S")
    folder_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder_path, f"RPS game {timestamp}.txt")
    with open(filename, 'w') as file:
        file.write("\n".join(game_results))
        file.write(f"\nFinal Score -> You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
