from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date):
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Main flow
current = display_current_datetime()
calculate_future_date(current)
# This code displays the current date and time, then prompts the user to enter a number of days to add to the current date,
# calculating and displaying the future date based on that input. It handles invalid inputs gracefully  