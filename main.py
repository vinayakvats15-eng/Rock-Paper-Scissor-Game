# main.py

# Import functions
from utils import get_user_choice
from   operations import get_computer_choice, decide_winner, show_score

# Infinite loop to play game 🔁
while True:
    print("\n🎮 --- Rock Paper Scissors ---")
    print("1️⃣ Play")
    print("2️⃣ Show Score")
    print("3️⃣ Exit")

    choice = input("👉 Enter your choice: ")

    if choice == '1':
        user = get_user_choice()  # Get user choice
        computer = get_computer_choice()  # Get computer choice
        decide_winner(user, computer)  # Decide winner

    elif choice == '2':
        show_score()  # Show scoreboard

    elif choice == '3':
        print("👋 Thanks for playing!")
        break  # Exit loop

    else:
        print("⚠️ Invalid choice!")