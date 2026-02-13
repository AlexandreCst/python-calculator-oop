"""
Script that give to the user the possibility of make basic operations untill it
decide to quit. He has the possibility to display his history of each operation
done.
"""

from calculator import Calculator
from functions_helper import check_quit, get_valid_number, get_valid_operation


if __name__ == "__main__":
    print("Give me two numbers, and I'll applicate operations on them")
    print("Enter 'q' at anytime to quit.\n")

    calculation = Calculator() # Create a calculator
    while True:
        # Check if the inputs is valid for numbers (int or float)
        first_number = get_valid_number("Enter a number: ")
        second_number = get_valid_number("Enter a second number: ")

        # Check if the operation is valid (+, -, *, /)
        operation = get_valid_operation(
            "\nWhat operation (+, -, *, /) do you want to do? "
            )
        
        # Make the appropriate operation demand by the user
        if operation == "+":
            add = calculation.addition(first_number, second_number)
            print(f"\nResult: {add:.2f}")
        
        elif operation == "-":
            sub = calculation.subtraction(first_number, second_number)
            print(f"\nResult: {sub:.2f}")
        
        elif operation == "*":
            mul = calculation.multiplication(first_number, second_number)
            print(f"\nResult: {mul:.2f}")

        else:
            div = calculation.division(first_number, second_number)
            if isinstance(div, object): # If it's an error (division by zero)
                print(f"\n{div}") # Display error message
            else: # If it's a number (division valid)
                print(f"\nResult: {div:.2f}")
        

        # Ask if the user wishes to display its history
        user_history = input("\nDo you want to show your history? (y/n)")

        # Check if the user want to quit
        user_quit = check_quit(user_history)

        # Display the history
        if user_history.lower().strip() in ['y', 'yes']:
            calculation.show_history()

