# game_logic.py

import random  # Import random module for computer choice

# Import shared data
from data import choices, user_score, computer_score

# Function to get computer choice 🤖
def get_computer_choice():
    return random.choice(choices)  # Randomly pick from list


# Function to decide winner 🏆
def decide_winner(user, computer):
    global user_score, computer_score  # Access global scores

    print(f"🧑 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")

    if user == computer:
        print("🤝 It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        
        print("🎉 You win!")
        user_score += 1  # Increase user score

    else:
        print("💻 Computer wins!")
        computer_score += 1  # Increase computer score


# Function to display score 📊
def show_score():
    print("\n📊 Score Board")
    print("You:", user_score)
    print("Computer:", computer_score)