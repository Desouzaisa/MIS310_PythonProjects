# This program is a dice game where two players roll dice over multiple rounds.
# The player with the highest total sum after all rounds wins.
# Based on a random numbers problem, similar to simulating real dice rolls.

import random

#Simulate rolling two dice and returning the sum
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

#Play one round and show the results
def play_round(round_number):
    print(f"\n--- Round {round_number} ---")
    p1 = roll_dice()
    p2 = roll_dice()
    print(f"Player 1 rolls a total of: {p1}")
    print(f"Player 2 rolls a total of: {p2}")
    return p1, p2

#Main function
def main():
    print("Ready for the Dice Sum Challenge?")

    #Ask for the number of rounds
    rounds = input("How many rounds do you want to play? ")
    while not rounds.isdigit() or int(rounds) <= 0:
        rounds = input("Please enter a valid number of rounds: ")
    rounds = int(rounds)

    #Initialize totals
    p1_total = 0
    p2_total = 0

    #Play the game
    for i in range(1, rounds + 1):
        p1, p2 = play_round(i)
        p1_total += p1
        p2_total += p2

    #Final results
    print("\n=== Final Results ===")
    print(f"Player 1's total score: {p1_total}")
    print(f"Player 2's total score: {p2_total}")

    if p1_total > p2_total:
        print("Winner: Player 1!")
    elif p2_total > p1_total:
        print("Winner: Player 2!")
    else:
        print("It's a tie!")

#Run the game
if __name__ == "__main__":
    main()
