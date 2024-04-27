def add(x, y):  # Function to add two numbers
    return x + y  # Return the sum of x and y
def subtract(x, y):  # Function to subtract two numbers
    return x - y  # Return the difference of x and y

def multiply(x, y):  # Function to multiply two numbers
    return x * y  # Return the product of x and y

def divide(x, y):
    """
    Function to divide two numbers.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")  # Raise an error if y is zero
    return x / y

def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number")

            
def calculator():
    # Use a while loop to continuously prompt the user to enter arithmetic operations
    while True:
        # operator avaliable
        print("select operator:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. exit")

        # to get the aritmetic user want to use for the operation
        arithmetics_operation = input("enter the airthmetic you want to use: ")

        # to check if the user want to exit the operation
        if arithmetics_operation == '5':
            # end the program
            break

        # Get the user's input for the first number
        try:
            num1 = float(input("enter the first number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Get the user's input for the second numbers
        try:
            num2 = float(input("enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Perform the selected arithmetic operation
        if arithmetics_operation == '1':  # Check if user selected addition
            result = add(num1, num2)  # Call the `add` function
        elif arithmetics_operation == '2':  # Check if user selected subtraction
            result = subtract(num1, num2)  # Call the `subtract` function
        elif arithmetics_operation == '3':  # Check if user selected multiplication
            result = multiply(num1, num2)  # Call the `multiply` function
        elif arithmetics_operation == '4':  # Check if user selected division
            result = divide(num1, num2)  # Call the `divide` function
        else:
            # Display an error message if the user's input is invalid
            print("Invalid input")

        # Display the result of the arithmetic operation
        print("result: {:.2f}".format(result))

 # Call the `calculator` function
calculator()