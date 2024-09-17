# DS.v3.1.2.5
# Calculator Module

# Calculator Package

The `Calculator` package provides a simple calculator class with basic arithmetic operations, memory functionality, and additional capabilities like taking roots. This package is designed for easy integration into Python projects where basic arithmetic operations are needed.

# Features

- Addition: Add a number to the current memory.
- Subtraction: Subtract a number from the current memory.
- Multiplication: Multiply the current memory by a number.
- Division: Divide the current memory by a number (with error handling for division by zero).
- Nth Root: Take the nth root of the current memory.
- Memory Reset: Reset the memory to zero.

# Installation

To install the `calculator.py` package, you can simply download the file or clone the repository to your local machine:

```bash
git clone <repository-url>
```

Alternatively, if the package is available on PyPI, you can install it using pip:

```bash
pip install calculator
```

# Usage

To use the `Calculator` class, you need to import the class from the `calculator.py` file and then create an instance of the class. Here’s an example of how to use each method:

1. Importing the Calculator

```python
from calculator import Calculator
```

2. Creating an Instance

```python
calc = Calculator()
```

3. Performing Operations

- Addition

    ```python
    result = calc.add(10)
    print(result)  # Output will be 10
    ```

- Subtraction

    ```python
    result = calc.subtract(3)
    print(result)  # Output will be 7
    ```

- Multiplication

    ```python
    result = calc.multiply(2)
    print(result)  # Output will be 14
    ```

- Division

    ```python
    result = calc.divide(7)
    print(result)  # Output will be 2.0
    ```

    Note: If you try to divide by zero, the method will raise a `ValueError`:

    ```python
    calc.divide(0)  # Raises ValueError: Cannot divide by zero.
    ```

- Nth Root

    ```python
    result = calc.take_root(2)
    print(result)  # Output will be the square root of the current memory value.
    ```

    Note: The method will raise a `ValueError` if the root degree is less than 1:

    ```python
    calc.take_root(0)  # Raises ValueError: Root degree must be >= 1.
    ```

- Resetting Memory

    ```python
    calc.reset_memory()
    print(calc.memory)  # Output will be 0
    ```

# Example Workflow

Here is a complete example that demonstrates the typical workflow using the `Calculator` class:

```python
from calculator import Calculator

calc = Calculator()  # Create an instance of Calculator
calc.add(15)         # Add 15 to memory
calc.subtract(5)     # Subtract 5 from memory
calc.multiply(3)     # Multiply memory by 3
calc.divide(2)       # Divide memory by 2
calc.take_root(3)    # Take the cube root of memory
calc.reset_memory()  # Reset memory to 0
```