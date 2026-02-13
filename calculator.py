"""This module contain the calculator class with basic operations like addition,
 subtraction, mulitplication and division."""

class Calculator:
    """This class represent a calculator with basic operations"""
    
    def __init__(self) -> None:
        """Initialize class attributes"""
        self.history = []

    def addition(self, a: float, b: float) -> float:
        """
        Addition of 2 terms a and b 
        
        Append the operation and result to the history.
        
        a: float
        b: float
        return type: float"""
        self.history.append(f"{a:.2f} + {b:.2f} = {a + b:.2f}")
        return a + b
    
    def subtraction(self, a: float, b: float) -> float:
        """
        Subtraction of 2 terms a and b

        Append the operation and result to the history.
        
        a: float
        b: float
        return type: float"""
        self.history.append(f"{a:.2f} - {b:.2f} = {a - b:.2f}")
        return a - b
    
    def multiplication(self, a: float, b: float) -> float:
        """
        Multiplication of 2 terms a and b

        Append the operation and result to the history.
        
        a: float
        b: float
        return type: float
        """
        self.history.append(f"{a:.2f} * {b:.2f} = {a * b:.2f}")
        return a * b
    
    def division(self, a: float, b: float):
        """
        Divsion of 2 terms a by b
        
        Append the operation and result to the history.

        a: float
        b: float
        return type: float
        """
        try:
            result = a / b
            self.history.append(f"{a:.2f} / {b:.2f} = {a / b:.2f}")
        except ZeroDivisionError:
            return Exception("Oops.. Division by 0!")
            
        return result
    
    def show_history(self):
        """
        Display the calculation history
        """
        if self.history == []:
            print("Ooh non history is empty.. Make an operation!")
        else:
            for operation in self.history:
                print(operation)

    
    def clear_history(self):
        """
        Clear the calculation history
        """
        self.history = []
