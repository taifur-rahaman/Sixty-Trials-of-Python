
# Safe Division Calculator

A Python-based command-line calculator application that supports multiple arithmetic operations with robust error handling and a user-friendly menu interface. The application can perform calculations on multiple numbers simultaneously using object-oriented design principles.

## Features

1.  **Multiple Arithmetic Operations**
    
    -   Addition of multiple numbers
    -   Subtraction with sequential operations
    -   Multiplication of multiple numbers
    -   Division with sequential operations
    -   Support for any number of operands
2.  **Menu-Driven Interface**
    
    -   Interactive command-line menu
    -   Clear operation selection
    -   Formatted output presentation
    -   Easy navigation and graceful exit
3.  **Comprehensive Error Handling**
    
    -   Division by zero protection
    -   Quantity validation (non-zero, non-negative)
    -   Minimum operand requirement (at least 2 numbers)
    -   Informative error messages
    -   Exception handling for multiple error types
4.  **Input Validation**
    
    -   Validates number of operands
    -   Converts string input to float
    -   Checks for negative or zero quantities
    -   Prevents division by zero
    -   Continuous error recovery
5.  **Modular Architecture**
    
    -   Separated concerns (operations, utilities, main logic)
    -   Reusable Operation class with static methods
    -   Utility functions for common tasks
    -   Easy to extend with new operations
6.  **Formatted Output**
    
    -   Decorative header formatting
    -   Centered operation titles
    -   Clear result display
    -   Professional presentation

## How It Works

### Operation Class Structure (calculator.py)

```python
class Operation:
    @staticmethod
    def addition(*args):
        return sum(args)
    
    @staticmethod
    def subtraction(*args):
        result = args[0]
        for arg in args[1:]:
            result -= arg
        return result
    
    @staticmethod
    def multiplication(*args):
        result = 1
        for arg in args:
            result *= arg
        return result
    
    @staticmethod
    def division(*args):
        result = args[0]
        for arg in args[1:]:
            result /= arg
        return result
```

**Key Components:**

-   **Static Methods**: No instance needed; methods are class-level
-   **Variadic Arguments (*args)**: Accept any number of operands
-   **Input Validation**: Check for minimum 2 operands
-   **Error Throwing**: Raise exceptions for invalid operations
-   **Sequential Processing**: Process operands left-to-right for subtraction/division

### Addition Logic

```python
addition(5, 10, 15)
# Returns: 5 + 10 + 15 = 30
# Uses sum() function for all operands
```

### Subtraction Logic

```python
subtraction(50, 10, 5)
# Returns: 50 - 10 - 5 = 35
# Starts with first number, subtracts remaining sequentially
```

### Multiplication Logic

```python
multiplication(2, 3, 4)
# Returns: 2 * 3 * 4 = 24
# Multiplies all operands sequentially (starts with 1)
```

### Division Logic

```python
division(100, 2, 5)
# Returns: 100 / 2 / 5 = 10
# Divides sequentially left to right
# Includes zero-check for all divisors
```

### Utility Functions (utils.py)

**beautify() Function:**

```python
def beautify(string):
    print("="*40)
    print(string.center(40))
    print("="*40)
```

-   Creates decorative headers
-   Centers text with padding
-   Improves visual presentation

**usr_input() Function:**

```python
def usr_input():
    numbers = []
    qty = input("Enter how many number you want to enter: ")
    # Validate quantity
    for i in range(int(qty)):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(float(num))
    return numbers
```

-   Collects user input
-   Validates quantity (non-zero, non-negative)
-   Converts to float for precision
-   Returns list of numbers

**exception_handler() Function:**

```python
def exception_handler(string):
    # Try to get user input
    try:
        numbers = usr_input()
    except ValueError as e:
        print(f"Value Error: {e}")
    else:
        # Dynamically call operation method
        result = getattr(Operation, string)(*numbers)
    # Handle specific exceptions
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return "ERROR"
    return result
```

-   Handles all exception types
-   Uses getattr() for dynamic method calling
-   Provides informative error messages
-   Returns "ERROR" on failure

### Program Flow (main.py)

```
1. Display calculator menu
2. Validate user choice (1-4, 0)
3. Call exception_handler with operation name
4. exception_handler collects input and validates
5. Dynamically call Operation method
6. Display formatted result
7. Loop until user exits (0)
```

## Project Structure

```
project/
├── main.py          # Main program with menu-driven interface
├── calculator.py    # Operation class with arithmetic methods
├── utils.py         # Utility functions for formatting and handling
└── README.md        # This file

```

## Key Concepts Demonstrated

### Static Methods

```python
@staticmethod
def addition(*args):
    return sum(args)

```

-   Belong to class, not instance
-   Called without instantiation: `Operation.addition()`
-   No access to instance/class attributes (except other static methods)
-   Useful for utility operations

### Variadic Arguments (*args)

```python
def addition(*args):
    # args is a tuple of all passed arguments
    return sum(args)

```

-   Accept any number of positional arguments
-   args becomes a tuple containing all arguments
-   Allows flexible function calls: `add(1, 2, 3, 4, 5)`
-   Ideal for operations with multiple operands

### Dynamic Method Calling with getattr()

```python
result = getattr(Operation, string)(*numbers)
# Equivalent to: Operation.addition(*numbers) if string = "addition"

```

-   Gets method by string name
-   Converts string input to method call
-   Enables flexible operation selection
-   Single line handles all operations

### Exception Handling with try-except-else

```python
try:
    numbers = usr_input()
except ValueError as e:
    print(f"Value Error: {e}")
else:
    result = getattr(Operation, string)(*numbers)
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

```

-   Catches specific exception types
-   `else` block executes only if no exception
-   Multiple except blocks for different errors
-   Allows graceful error recovery

### String Formatting with f-strings

```python
print(f"Enter number {i+1}: ")
print(f"Result: {utils.exception_handler('addition')}")

```

-   Embed variables directly in strings
-   More readable than % or .format()
-   Supports expressions within {}
-   Modern Python syntax

### Match Statement (Python 3.10+)

```python
match choice:
    case "1":
        # Operation 1
    case "0":
        exit()
    case _:
        # Default case

```

-   Structural pattern matching
-   Cleaner than if-elif-else chains
-   `_` as wildcard/default case
-   Requires Python 3.10+

## Limitations

⚠️ **Important Limitations:**

1.  **Limited Operation Set**
    
    -   Only four basic operations available
    -   No support for exponentiation, modulo, square root, etc.
    -   Would require adding new methods
2.  **Float Precision Issues**
    
    -   Division results in floating-point numbers
    -   Rounding errors may occur with certain divisions
    -   Example: `0.1 + 0.2 = 0.30000000000000004`
3.  **No Operation History**
    
    -   Previous calculations are not saved
    -   Cannot recall or modify past operations
    -   Each operation is independent
4.  **No Parentheses Support**
    
    -   Cannot group operations with parentheses
    -   All operations performed left-to-right
    -   No order of operations (PEMDAS) support
5.  **Single Input Validation Pass**
    
    -   Validates quantity but not individual number formats
    -   May crash if non-numeric input provided
    -   User must enter valid numbers
6.  **No Expression Parsing**
    
    -   Cannot evaluate mathematical expressions
    -   Must manually enter each number
    -   No support for equations like "2+3*4"


## Potential Enhancements

1.  **Additional Operations**
    
    -   Power/exponentiation: 2^5
    -   Modulo/remainder: 10 % 3
    -   Square root: √16
    -   Percentage calculations
    -   Average/mean of numbers
2.  **Operation History**
    
    -   Track previous calculations
    -   Display calculation history
    -   Ability to recall and modify past operations
    -   Export history to file
3.  **Advanced Calculations**
    
    -   Scientific functions (sin, cos, log, etc.)
    -   Trigonometric operations
    -   Statistical functions (mean, median, standard deviation)
    -   Matrix operations
4.  **Expression Evaluation**
    
    -   Parse mathematical expressions from string
    -   Support parentheses and order of operations (PEMDAS)
    -   Allow expressions like "2 + 3 * 4 - 5 / 2"
    -   Use external library like `eval()` or `sympy`
5.  **Data Persistence**
    
    -   Save calculations to file
    -   Load previous sessions
    -   Export results to CSV/PDF
    -   Generate calculation reports
6.  **Improved User Interface**
    
    -   GUI with buttons and display
    -   Color-coded output for operations
    -   Input validation with retry prompts
    -   Visual error highlighting
    -   Progress indicators for complex calculations
7.  **Performance Features**
    
    -   Keyboard shortcuts for operations
    -   Command-line arguments for direct calculation
    -   Batch calculation mode
    -   Undo/redo functionality
    -   Settings/preferences menu
8.  **Error Handling Improvements**
    
    -   Handle non-numeric input gracefully
    -   Suggest corrections for invalid input
    -   Provide helpful error messages
    -   Log errors to file
    -   Recovery suggestions

## Code Quality Features

✅ Static methods for utility operations  
✅ Variadic arguments for flexible input  
✅ Dynamic method calling with getattr()  
✅ Comprehensive exception handling  
✅ Multiple exception types caught separately  
✅ Input validation at each step  
✅ Modular code organization across files  
✅ Separated concerns (operations, utilities, UI)  
✅ Formatted output with beautify()  
✅ Reusable utility functions  
✅ Clear variable naming conventions  
✅ Informative error messages  
✅ Graceful error recovery  
✅ Menu-driven user interface  
✅ Modern Python syntax (match statement, f-strings)