def check_quit(user_input: str) -> str:
    """
    Check if the user want to quit the calculator
    
    user_input: Message displaying to the user
    type user_input: str
    return: The value enter by the user
    rtype: str
    """
    if user_input.lower().strip() in ['q', 'quit']:
        exit()
    else:
        return user_input

def get_valid_number(prompt_message: str) -> float:
    """
    Check if the user input is a valid number and return this value converting
    in float
    
    prompt_message: Message displaying to the user
    type prompt_message: str
    return: The value enter by the user converted in float
    rtype: float
    """
    while True:
        user_input = input(prompt_message)
        check_quit(user_input) # Check if the user want to quit
        try:
            user_prompt = float(user_input)
            break
        except (ValueError, TypeError):
            print("Sorry the value isn't valid.. Please enter a number.")
            continue
    return user_prompt

def get_valid_operation(prompt_message: str) -> str:
    """
    Check if the user input is a valid operation and return it
    
    prompt_message: Message displaying to the user
    type prompt_message: str
    return: The valid operation
    rtype: str
    """
    while True:
        operation = input(prompt_message)
        check_quit(operation) # Check if the user want to quit
        if operation not in ["+", "-", "*", "/"]:
            print("Please, enter a valid operation..")
            continue
        else:
            break
    return operation