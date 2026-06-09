# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Arithmetic Calculator
# DATE WRITTEN: 8/26/2020
# UPDATED:      2026 — removed unused toFixed(), added input validation,
#                      added division-by-zero guard, updated to snake_case,
#                      using right-aligned ">29s" format for clean output
#
# PURPOSE: Perform basic arithmetic calculations (add, subtract, multiply,
#          divide) on two numbers entered by the user and display the
#          results in a formatted right-aligned output.
#
# Declare Variables (place in alpha order)
# Initialize variables used to store calculations (ensure accuracy of results)
difference = 0.0
divide = 0.0
multiply = 0.0
total = 0.0

# ============================================================
# INPUT OPERATIONS — collect two numbers from the user

# Loop until valid numeric input for number 1
while True:
    try:
        print("Enter the first number or value [numbers and decimals only].")
        num1 = float(input())
        break  # Valid input received
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Loop until valid numeric input for number 2
while True:
    try:
        print("Enter the second number [numbers and decimals only].")
        num2 = float(input())
        break  # Valid input received
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# ============================================================
# Perform calculations — add, subtract, multiply, divide
total      = num1 + num2   # Addition
difference = num1 - num2   # Subtraction
multiply   = num1 * num2   # Multiplication

# Guard against division by zero before dividing
if num2 == 0:
    divide = None   # Cannot divide by zero
else:
    divide = num1 / num2   # Division

# ============================================================
# OUTPUT OPERATIONS — display results in right-aligned format

print("=========================================================")
print(format("Number 1 = ",              ">29s") + format(num1,       ",.2f"))
print(format("Number 2 = ",              ">29s") + format(num2,       ",.2f"))
print(format("Sum of the numbers = ",    ">29s") + format(total,      ",.2f"))
print("================================================================")
print(format("Difference of the Numbers = ", ">29s") + format(difference, ",.2f"))
print("================================================================")
print(format("Multiplying two values = ",    ">29s") + format(multiply,   ",.2f"))
print("================================================================")

# Display division result or division-by-zero message
if divide is None:
    print(format("Dividing the two numbers = ", ">29s") + "Cannot divide by zero")
else:
    print(format("Dividing the two numbers = ", ">29s") + format(divide, ",.2f"))
print("================================================================")

# END PROGRAM
