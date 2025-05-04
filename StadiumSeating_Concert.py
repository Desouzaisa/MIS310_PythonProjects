#Stadium Seating - Hozier Concert in New Britain, CT
#Based on the Stadium Seating Program

def calculate_income():
    #Ticket prices
    PRICE_A = 220
    PRICE_B = 160
    PRICE_C = 125

    #Seat limits
    MAX_A = 80
    MAX_B = 100
    MAX_C = 120

    #Input with validation
    while True:
        class_a = int(input("How many Class A tickets were sold? "))
        if 0 <= class_a <= MAX_A:
            break
        print(f"Please enter a value between 0 and {MAX_A}.")

    while True:
        class_b = int(input("How many Class B tickets were sold? "))
        if 0 <= class_b <= MAX_B:
            break
        print(f"Please enter a value between 0 and {MAX_B}.")

    while True:
        class_c = int(input("How many Class C tickets were sold? "))
        if 0 <= class_c <= MAX_C:
            break
        print(f"Please enter a value between 0 and {MAX_C}.")

    #Calculate income per class
    income_a = class_a * PRICE_A
    income_b = class_b * PRICE_B
    income_c = class_c * PRICE_C
    total_income = income_a + income_b + income_c

    #Summary of total income
    print("\n------ Ticket Sales Summary ------")
    print(f"Class A tickets sold: {class_a} =  ${income_a:,.2f}")
    print(f"Class B tickets sold: {class_b} =  ${income_b:,.2f}")
    print(f"Class C tickets sold: {class_c} = ${income_c:,.2f}")
    print("----------------------------------")
    print(f"Total income generated:   ${total_income:,.2f}")

#Run the program
calculate_income()
