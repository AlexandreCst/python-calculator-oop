from calculator import Calculator

def check_quit(user_input):
    if user_input.lower().strip() in ['q', 'quit']:
        exit()
    else:
        return user_input

def get_valid_number(prompt_message):
    while True:
        user_input = input(prompt_message)
        check_quit(user_input)
        try:
            user_prompt = float(user_input)
            break
        except (ValueError, TypeError):
            print("Sorry the value isn't valid.. Please enter a number.")
            continue
    return user_prompt

def get_valid_operation(prompt_message):
    while True:
        operation = input(prompt_message)
        check_quit(operation)
        if operation not in ["+", "-", "*", "/"]:
            print("Please, enter a valid operation..")
            continue
        else:
            break
    return operation

if __name__ == "__main__":
    print("Give me two numbers, and I'll applicate operations on them")
    print("Enter 'q' at anytime to quit.\n")
    calculation = Calculator()
    while True:
        first_number = get_valid_number("Enter a number: ")
        second_number = get_valid_number("Enter a second number: ")
        operation = get_valid_operation(
            "What operation (+, -, *, /) do you want to do? "
            )
        
        if operation == "+":
            print(calculation.addition(first_number, second_number))
        
        elif operation == "-":
            print(calculation.subtraction(first_number, second_number))
        
        elif operation == "*":
            print(calculation.multiplication(first_number, second_number))

        else:
            print(calculation.division(first_number, second_number))
        

        user_history = input("Do you want to show your history? (y/n)")
        user_quit = check_quit(user_history)

        if user_history.lower().strip() in ['y', 'yes']:
            calculation.show_history()

