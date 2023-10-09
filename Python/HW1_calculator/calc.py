#  This function is used to get a numeric input from the user.
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Input is not a valid number. Please try again.")

# This function performs the calculation based on the operation chosen by the user, taking 3 arguments.


def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Cannot divide by 0")
            return None


# Loop will continue to run until the user chooses to exit by entering '5' for the operation.
while True:
    # Prompting user to enter numbers.
    num1 = get_numeric_input("Enter the first number: ")
    num2 = get_numeric_input("Enter the second number: ")
# Operation choice.
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    operation = input("Enter choice (1/2/3/4/5): ")
# The line where program checks the given value of "5" and exit program.
    if operation == '5':
        break
# This checks if the user has entered a valid operation. If they have, it calls the calculate function to perform the calculation and print the result. If the result is None (which can only happen if the user tries to divide by zero), it doesn't print anything.If the user has not entered a valid operation, it prints an error message and the loop starts over, prompting the user for two numbers and an operation again.
    if operation in ('1', '2', '3', '4'):
        result = calculate(num1, num2, operation)
        if result is not None:
            print(f"The result is: {result:.4f}")
    else:
        print("Invalid choice, please try again and choose correct operation from list")
