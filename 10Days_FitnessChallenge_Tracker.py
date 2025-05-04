#10-Day Fitness Challenge Tracker
#Tracks daily steps and 7-minute workouts to calculate fitness points
#Based on Book Club Award and Step Tracker Programs

def fitness_challenge():
    total_points = 0  #Total points earned during the challenge

    print("Welcome to the 10-Day Fitness Challenge!")
    print("Each day, you'll enter your steps and if you completed a 7-minute workout.")
    print("You earn 1 point for 10,000+ steps and 2 points for doing the workout.\n")

    #Repeat for 10 days
    for day in range(1, 11):
        print(f"--- Day {day} ---")

        #Ask user for step count
        while True:
            try:
                steps = int(input("Enter your step count: "))
                if steps < 0:
                    print("Please enter a non-negative number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        #Ask user if they completed the workout
        while True:
            workout = input("Did you complete a 7-minute workout? (yes/no): ").strip().lower()
            if workout in ["yes", "no"]:
                break
            else:
                print("Please enter 'yes' or 'no'.")

        #Calculate points for the day
        points_today = 0
        if steps >= 10000:
            points_today += 1  #1 point for 10k+ steps
        if workout == "yes":
            points_today += 2  #2 points for workout

        total_points += points_today  # Add to total
        print(f"Points earned today: {points_today}\n")

    #Final summary
    print("====== Challenge Complete ======")
    print(f"Total points earned: {total_points}")

    #Check if user earned reward
    if total_points >= 25:
        print("Congratulations! You earned a free workout session!")
    else:
        print(f"You were {25 - total_points} points away from earning a free workout session. Keep going!")

#Run the program
fitness_challenge()
