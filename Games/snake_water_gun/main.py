import random

def get_winner(user_choice, computer_choice):
    """Determines the winner based on the game rules"""
    if user_choice == computer_choice:
        return "draw"
    
    winning_combinations = {
        "snake": "water",  # Snake drinks water → Snake wins
        "water": "gun",    # Water douses gun → Water wins
        "gun": "snake"     # Gun shoots snake → Gun wins
    }
    
    return "user" if winning_combinations[user_choice] == computer_choice else "computer"

def snake_gun_water_game():
    print("\n🔹 Welcome to the Snake, Gun, Water Game! 🔹\n")
    
    choices = ["snake", "gun", "water"]
    rounds = 5  # Best of 5
    user_score, computer_score = 0, 0

    for i in range(1, rounds + 1):
        print(f"\n🎲 Round {i} of {rounds}")
        
        # Take user input and validate it
        while True:
            user_choice = input("Choose (snake, gun, water): ").strip().lower()
            if user_choice in choices:
                break
            print("❌ Invalid choice! Please choose from snake, gun, or water.")

        # Computer's choice
        computer_choice = random.choice(choices)
        print(f"💻 Computer chose: {computer_choice}")

        # Determine the winner
        result = get_winner(user_choice, computer_choice)

        if result == "user":
            print("✅ You won this round!")
            user_score += 1
        elif result == "computer":
            print("❌ You lost this round!")
            computer_score += 1
        else:
            print("⚖ It's a draw!")

        print(f"📊 Current Score → You: {user_score} | Computer: {computer_score}")

    # Final Winner
    print("\n🔹 Game Over! 🔹")
    if user_score > computer_score:
        print("🏆 Congratulations! You won the game!")
    elif user_score < computer_score:
        print("💻 Computer wins! Better luck next time.")
    else:
        print("⚖ It's a tie!")

# Run the game
if __name__ == "__main__":
    snake_gun_water_game()
