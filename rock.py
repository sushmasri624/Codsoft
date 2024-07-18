import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0
    play_again = True

    print("Welcome to Rock-Paper-Scissors!")

    while play_again:
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"\nScores -> You: {user_score}, Computer: {computer_score}")
        
        play_again_input = input("\nDo you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'
    
    print("\nThank you for playing Rock-Paper-Scissors!")

if __name__ == "__main__":
    main()
