print("Calculator Menu:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

# Take user input for option
option = int(input("Choose an option: "))

result = 0

# Check if the chosen option is valid (1, 2, 3, or 4)
if option in [1, 2, 3, 4]:
    # Take user input for two numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Perform the selected operation based on the chosen option
    if option == 1:
        result = num1 + num2
        operation = "Addition"
    elif option == 2:
        result = num1 - num2
        operation = "Subtraction"
    elif option == 3:
        result = num1 * num2
        operation = "Multiplication"
    elif option == 4:
        if num2 != 0:
            result = num1 / num2
            operation = "Division"
        else:
            print("Error: Cannot divide by zero!")
            exit(1)  # Exit the program if division by zero is attempted
    
    # Display the result of the operation
    print(f"The result of {operation} is {result}")
else:
    # Display error message for invalid option
    print("Invalid option entered. Please choose a valid option (1-4).")









