#This program simulates a game of Even and Odds between two players.
#Each round, both players throw a random number from 1 to 10.
#If the sum is even, Player 1 wins. If it's odd, Player 2 wins.
#Based on the structure of the Rock, Paper, Scissors game

import random

#Simulate a number choice between 1 and 10
def throw_number():
    """Simulates a number throw between 1 and 10"""
    return random.randint(1, 10)


#Play a single round of Even and Odds
def play_round(player1_number, player2_number):
    """ Determines the winner of an Even and Odds round based on sum    """
    total = player1_number + player2_number
    result = 'even' if total % 2 == 0 else 'odd'

    print(f"Player 1 throws {player1_number}, Player 2 throws {player2_number}. Total is {total} ({result}).")

    if result == 'even':
        print("Player 1 wins the round (Even wins).")
        return 'Player 1'
    else:
        print("Player 2 wins the round (Odd wins).")
        return 'Player 2'


#Main function
def main():
    player1_score = 0
    player2_score = 0

    #Ask the user for the number of rounds
    rounds = int(input("How many rounds do you want to play? "))

    for _ in range(rounds):
        player1_number = throw_number()
        player2_number = throw_number()

        winner = play_round(player1_number, player2_number)

        if winner == 'Player 1':
            player1_score += 1
        else:
            player2_score += 1

    #Print the final results
    print(f"\nFinal Score: Player 1 wins {player1_score} round(s). Player 2 wins {player2_score} round(s).")
    if player1_score > player2_score:
        print("Overall Winner: Player 1!")
    elif player2_score > player1_score:
        print("Overall Winner: Player 2!")
    else:
        print("The game ends in a tie!")

#Run the function
if __name__ == "__main__":
    main()

