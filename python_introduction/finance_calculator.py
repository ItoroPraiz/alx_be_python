"""
This script calculates the monthly savings based on user input for income and expenses.
1. User Input for Financial Details:
2. Calculate Monthly Savings
3. Project Annual Savings:
"""


#Prompt the user for their monthly income: “Enter your monthly income:
monthly_income = float(input("Enter your monthly income: "))

#Ask for their total monthly expenses: “Enter your total monthly expenses:
total_expenses = float(input("Enter your total monthly expenses: "))

#Calculate the monthly savings by subtracting monthly expenses from the monthly income.
monthly_savings = monthly_income - total_expenses
#Assume a simple annual interest rate of 5%.
annual_interest_rate = 0.05

'''Calculate the projected savings after one year, 
incorporating the interest. Use the simplified formula 
for annual savings projection: '''
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

#Display the user’s monthly savings.
#Display the projected annual savings after including interest.
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings after interest is: ${projected_savings:.2f}") 