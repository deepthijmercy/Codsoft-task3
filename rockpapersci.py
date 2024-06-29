
import random

def get_machinechoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_userchoice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice, please try again.")

def determine_winner(userchoice, machinechoice):
    if userchoice == machinechoice:
        return "tie"
    elif (userchoice == "rock" and machinechoice == "scissors") or \
         (userchoice == "scissors" and machinechoice == "paper") or \
         (userchoice == "paper" and machinechoice == "rock"):
        return "user wins"
    else:
        return "computer wins"

def display_result(userchoice, machinechoice, winner, user_score, computer_score):
    print(f"\nYou chose: {userchoice}")
    print(f"Computer chose: {machinechoice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1
    print(f"Current Score - You: {user_score} | Computer: {computer_score}")
    return user_score, computer_score

def play_again():
    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again in ['yes', 'no']:
            return again == 'yes'
        else:
            print("Invalid input, please try again.")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0
    
    while True:
        userchoice = get_userchoice()
        machinechoice = get_machinechoice()
        winner = determine_winner(userchoice, machinechoice)
        
        user_score, computer_score = display_result(userchoice, machinechoice, winner, user_score, computer_score)
        
        if not play_again():
            print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
