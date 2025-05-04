#Budget Analysis Program
#Monthly Breakdown

#Collect expenses from a list of items under a given category
def get_expense_input(category, items):
    print(f"\nEnter your {category} expenses:")
    expenses = {}
    for item in items:
        while True:
            try:
                #Ask user for expense value and store it in a dictionary
                amount = float(input(f" {item}: $"))
                expenses[item] = amount
                break
            except ValueError:
                print("Please enter a valid number.")
    return expenses

#Run the whole program
def main():
    print("==== Monthly Budget Tracker ====")
    #Ask user for total monthly income
    try:
        income = float(input("Enter your total monthly income: $"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    #Lists of predefined expense categories
    needs_items = ["Rent", "Car", "Utilities", "Groceries", "Other (Needs)"]
    wants_items = ["Dining Out", "Entertainment", "Trips", "Other (Wants)"]

    #Get input from user for each category
    needs = get_expense_input("Needs", needs_items)
    wants = get_expense_input("Wants", wants_items)

    #Calculate the totals
    total_needs = sum(needs.values())
    total_wants = sum(wants.values())
    total_expenses = total_needs + total_wants
    balance = income - total_expenses

    #Display summary
    print("\n===== Budget Summary =====")
    print(f"Total Income:    ${income:.2f}")
    print(f"Total Needs:     ${total_needs:.2f}")
    print(f"Total Wants:     ${total_wants:.2f}")
    print(f"Total Expenses:  ${total_expenses:.2f}")

    #Show budget result
    if balance > 0:
        print(f"You are under budget. Remaining: ${balance:.2f}")
    elif balance < 0:
        print(f"You are over budget by: ${-balance:.2f}")
    else:
        print("Your budget is perfectly balanced!")

#Run the program
if __name__ == "__main__":
    main()
