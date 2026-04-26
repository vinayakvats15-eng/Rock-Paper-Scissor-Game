# utils.py

# Function to take user input safely 💡
def get_user_choice():
    choice = input("👉 Enter rock / paper / scissors: ").lower()  # Take input and convert to lowercase
    return choice  # Return user choice