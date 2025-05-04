#Snow Day Tracker
#Asks the user to enter the number of snow days for each month across a number of years
#Calculates the total and average snow days
#Finds which month and year had the most snow.
#Based on Average Rainfall Assignment

#Global variables
total_snow = 0  #total snow days across all years
total_months = 0  #total number of months entered
years = 0  #number of years to track

max_snow = -1  #highest number of snow days in any single month
max_month = ""  #name of the snowiest month
max_year = 0  #year the snowiest month happened

#List of months in a year
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']

#Ask user how many years to track
def get_years():
    global years
    years = int(input("Enter the number of years to track snow days: "))

#Collect snow day data for each month of each year
def collect_snow_data():
    global total_snow, total_months, max_snow, max_month, max_year

    #Each year
    for year in range(1, years + 1):
        print(f"\nFor Year {year}:")
        yearly_total = 0  # keep track of snow days for the current year

        #Each month
        for month in range(12):
            while True:
                try:
                    #Ask the user for the number of snow days
                    snow = float(input(f"Enter snow days for {month_names[month]}: "))

                    #Validate input: must be between 0 and 31
                    if snow < 0 or snow > 31:
                        print("Please enter a number between 0 and 31.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            #Add the valid input to totals
            yearly_total += snow
            total_snow += snow
            total_months += 1

            #Check if this is the snowiest month so far
            if snow > max_snow:
                max_snow = snow
                max_month = month_names[month]
                max_year = year

        #Summary for the year
        print(f"Total snow days for Year {year}: {yearly_total}")
        print(f"Average snow days per month in Year {year}: {yearly_total / 12:.2f}")


#Display the final summary after all data is collected
def display_results():
    if total_months > 0:
        average_snow = total_snow / total_months

        print("\n====== FINAL SUMMARY ======")
        print(f"Total years tracked: {years}")
        print(f"Total months recorded: {total_months}")
        print(f"Total snow days: {total_snow}")
        print(f"Average snow days per month: {average_snow:.2f}")
        print(f"Snowiest month: {max_month}, Year {max_year} ({max_snow} snow days)")
    else:
        print("No data to display.")


#Run the program in order
def main():
    get_years()
    collect_snow_data()
    display_results()

# Start the program
main()

