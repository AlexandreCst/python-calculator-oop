# Python calculator OOP

## Description
A simple CLI calculator in Python based on POO principles. The script ask 
numbers and an operator among [+, -, *, /, **, %, !, sqrt] to make some 
scientific calculations.

## Features
- Class calculator with methods (addition, subtraction, multiplication, 
division, show history and clear history)
- Subclass scientific with methods (power, factorial, modulo and square root)
- Function_helper module with functions to check if the user want to quit the
script (check_quit()), 2 functions to check the validity of the user inputs 
(get_valid_number() and get_valid_operation()) and one function to handle
different error that occurs like ZeroDivisionError or ValueError (handle_error())
- Main script with basic and scientific arithmetic operations (addition, 
subtraction, multiplication, division)
- Input validation
- Calculation history (viewable on demand)
- Exit anytime with 'q' command
- Formatted output with 2 decimal places

## Installation
Clone the repository:
```bash
git clone https://github.com/AlexandreCst/python-calculator-oop.git
cd python-calculator-oop
```

No additional dependencies required (uses Python standard library only).

## How to Use
Run the program:
```bash
python main.py
```

Follow the prompts:
- Enter your first number
- Enter your second number
- Choose an operation (+, -, *, /)
- View result
- Type 'q' anytime to quit

## Requirements
- Python 3.9 or above

## License
MIT License

## Author
Alexandre COSTE