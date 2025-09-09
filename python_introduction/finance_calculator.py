<<<<<<< HEAD
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
=======
# finance_calculator.py

# Prompt user for financial details
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest
>>>>>>> 76e5a87c9e3718dac40135ae10fbb8bff0659b47
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

<<<<<<< HEAD
=======
# Display results
>>>>>>> 76e5a87c9e3718dac40135ae10fbb8bff0659b47
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
