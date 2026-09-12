#Create a basic rock papper scissors game  generate a functon which 
# repeatediately requests input from the user(either rock, paper, or scissors) 
# and 
# compares it to a randomly generated the opponent's choice.
# Then check who won and display the results after each round.
# The game should continue until the user decides to quit.

import random

def rock_paper_scissors():
	choices = ("rock", "paper", "scissors")
	print("Welcome to Rock, Paper, Scissors!")
	print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

	while True:
		user_choice = input("Your choice: ").strip().lower()

		if user_choice == "quit":
			print("Thanks for playing!")
			break
		if user_choice not in choices:
			print("Invalid choice. Please try again.")
			continue

		opponent_choice = random.choice(choices)
		print(f"Opponent chose: {opponent_choice}")

		if user_choice == opponent_choice:
			print("It's a tie!")
		elif (
			(user_choice == "rock" and opponent_choice == "scissors")
			or (user_choice == "paper" and opponent_choice == "rock")
			or (user_choice == "scissors" and opponent_choice == "paper")
		):
			print("You win!")
		else:
			print("You lose!")


if __name__ == "__main__":
	rock_paper_scissors()