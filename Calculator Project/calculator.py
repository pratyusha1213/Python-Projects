# calculator.py

class Calculator:
    def __init__(self):
        """
        Initialize the Calculator with memory set to 0.
        """
        self.memory = 0

    def add(self, value):
        """
        Add the given value to the current memory.

        :param value: The number to be added.
        :return: The result after addition.
        """
        self.memory += value
        return self.memory

    def subtract(self, value):
        """
        Subtract the given value from the current memory.

        :param value: The number to be subtracted.
        :return: The result after subtraction.
        """
        self.memory -= value
        return self.memory

    def multiply(self, value):
        """
        Multiply the current memory by the given value.

        :param value: The number to multiply by.
        :return: The result after multiplication.
        """
        self.memory *= value
        return self.memory

    def divide(self, value):
        """
        Divide the current memory by the given value.

        :param value: The number to divide by.
        :return: The result after division.
        :raises ValueError: If division by zero is attempted.
        """
        if value == 0:
            raise ValueError("Cannot divide by zero.")
        self.memory /= value
        return self.memory

    def take_root(self, n):
        """
        Take the nth root of the current memory.

        :param n: The degree of the root.
        :return: The result after taking the root.
        :raises ValueError: If n is less than 1.
        """
        if n < 1:
            raise ValueError("Root degree must be >= 1.")
        self.memory **= (1/n)
        return self.memory

    def reset_memory(self):
        """
        Reset the memory to 0.
        """
        self.memory = 0
