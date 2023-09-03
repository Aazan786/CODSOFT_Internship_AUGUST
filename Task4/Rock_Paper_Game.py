import random

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in ["rock", "paper", "scissors"]:
                return user_choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def display_result(self, user_choice, computer_choice, result):
        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")
        print(result)
        print(f"User Score: {self.user_score}, Computer Score: {self.computer_score}\n")

    def play_game(self):
        print("Welcome to Rock-Paper-Scissors Game!")
        rounds = int(input("Enter the number of rounds to play: "))
        
        for _ in range(rounds):
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(user_choice, computer_choice)
            self.display_result(user_choice, computer_choice, result)

        print("Game Over!")

def main():
    game = RockPaperScissors()
    game.play_game()

if __name__ == "__main__":
    main()
