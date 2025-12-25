
# Tuple Swapper

A Python program that allows users to swap elements within a tuple by specifying index positions. The application demonstrates tuple immutability by converting tuples to lists for modification, performing the swap operation, and converting back to tuples. This project showcases tuple unpacking, index-based element swapping, exception handling, and interactive user input in Python.

## Features

1.  **Index Display**
    
    -   Shows all tuple elements with their indices
    -   Zero-based index numbering
    -   Clear index-value pairing
    -   Uses enumerate() for iteration
    -   Formatted output display
2.  **Element Swapping**
    
    -   Swap any two elements by index
    -   User-specified index positions
    -   Tuple immutability handling
    -   Temporary list conversion
    -   Returns new swapped tuple
3.  **Multiple Swap Operations**
    
    -   Perform consecutive swaps
    -   Build on previous swap results
    -   Interactive swap continuation
    -   Cumulative swap effects
    -   Session-based modifications
4.  **Exception Handling**
    
    -   IndexError for invalid indices
    -   ValueError for non-numeric input
    -   Graceful error recovery
    -   User-friendly error messages
    -   Continuous operation after errors
5.  **Interactive Interface**
    
    -   Space-separated tuple input
    -   Index-based element selection
    -   User-controlled swap flow
    -   Multiple tuple processing
    -   Easy exit options
6.  **Object-Oriented Design**
    
    -   Swapper class encapsulation
    -   Static method utilities
    -   Clean separation of concerns
    -   Reusable class structure
    -   Professional code organization
7.  **Formatted Output**
    
    -   Beautified program header
    -   Section separators
    -   Clear result display
    -   Professional presentation
    -   Visual feedback

## How It Works

### Swapper Class Structure

```python
class Swapper:
    def __init__(self):
        pass
    
    @staticmethod
    def show_index(tuple_):
        for index, value in enumerate(tuple_):
            print(f"{index}: {value}")
    
    @staticmethod
    def swap(tuple_, index_1, index_2):
        tuple_ = list(tuple_)
        tuple_[index_1], tuple_[index_2] = tuple_[index_2], tuple_[index_1]
        return tuple(tuple_)

```

**Key Components:**

-   **Swapper Class**: Container for tuple manipulation functionality
-   **Empty Constructor**: No initialization needed
-   **show_index()**: Static method to display indexed elements
-   **swap()**: Static method to swap elements by index
-   **Tuple-List Conversion**: Handles tuple immutability
-   **Index-Based Access**: Direct element manipulation

### Index Display Algorithm

```python
@staticmethod
def show_index(tuple_):
    for index, value in enumerate(tuple_):
        print(f"{index}: {value}")

```

**Process:**

1.  Use enumerate() to get index-value pairs
2.  Iterate through tuple elements
3.  Print each index with its corresponding value
4.  Zero-based indexing (starts at 0)
5.  Formatted string output

**Example:**

```
Input: (4, 2, 3, 'a', 5)

Output:
0: 4
1: 2
2: 3
3: a
4: 5

```

### Enumerate Function

```python
enumerate(tuple_)

```

**How it works:**

-   Returns an enumerate object
-   Produces (index, value) pairs
-   Index starts at 0 by default
-   Can specify custom start value
-   Memory efficient iteration

**Example:**

```python
tuple_ = ('a', 'b', 'c')
for index, value in enumerate(tuple_):
    print(index, value)

# Output:
# 0 a
# 1 b
# 2 c

# Custom start
for index, value in enumerate(tuple_, start=1):
    print(index, value)

# Output:
# 1 a
# 2 b
# 3 c

```

### Swap Algorithm

```python
@staticmethod
def swap(tuple_, index_1, index_2):
    tuple_ = list(tuple_)
    tuple_[index_1], tuple_[index_2] = tuple_[index_2], tuple_[index_1]
    return tuple(tuple_)

```

**Process:**

1.  **Convert to List**: `tuple_ = list(tuple_)`
    -   Tuples are immutable
    -   Lists allow element modification
    -   Creates mutable copy
2.  **Swap Elements**: `tuple_[index_1], tuple_[index_2] = tuple_[index_2], tuple_[index_1]`
    -   Simultaneous assignment (tuple unpacking)
    -   No temporary variable needed
    -   Pythonic swap syntax
3.  **Convert Back**: `return tuple(tuple_)`
    -   Restore tuple type
    -   Return new immutable tuple
    -   Original tuple unchanged

**Example:**

```
Input: (4, 2, 3, 'a', 5), index_1=0, index_2=3

Step 1 - Convert to list:
[4, 2, 3, 'a', 5]

Step 2 - Swap elements at index 0 and 3:
Before: [4, 2, 3, 'a', 5]
After:  ['a', 2, 3, 4, 5]

Step 3 - Convert back to tuple:
('a', 2, 3, 4, 5)

```

### Tuple Unpacking Swap

```python
tuple_[index_1], tuple_[index_2] = tuple_[index_2], tuple_[index_1]

```

**How it works:**

1.  Right side creates temporary tuple: `(tuple_[index_2], tuple_[index_1])`
2.  Left side unpacks values to variables
3.  Assignment happens simultaneously
4.  No explicit temporary variable needed
5.  Atomic operation in Python

**Traditional vs Pythonic:**

```python
# Traditional approach (with temp variable)
temp = tuple_[index_1]
tuple_[index_1] = tuple_[index_2]
tuple_[index_2] = temp

# Pythonic approach (tuple unpacking)
tuple_[index_1], tuple_[index_2] = tuple_[index_2], tuple_[index_1]

```

### Main Program Flow

```python
while True:
    tuple_ = tuple(input("Enter tuple elements separated by space: ").split())
    Swapper.show_index(tuple_)
    swap_tuple_ = tuple_
    while True:
        try:
            index_1 = int(input("Which element to Swap: "))
            index_2 = int(input("With which element to Swap: "))
            swap_tuple_ = Swapper.swap(tuple_, index_1, index_2)
            beautify("Swapped Tuple")
            Swapper.show_index(swap_tuple_)
        except IndexError:
            print("Invalid index")
        except ValueError:
            print("Invalid input")
        else:
            tuple_ = swap_tuple_
            if input("Do you want to swap again? (y/n): ") == "n":
                break
    if input("Do you want to try again? (y/n): ") == "n":
        break

```

**Process:**

1.  **Outer Loop**: Multiple tuple processing sessions
2.  **Input Tuple**: Space-separated elements
3.  **Display Indices**: Show current tuple state
4.  **Inner Loop**: Multiple swap operations on same tuple
5.  **Get Indices**: User specifies swap positions
6.  **Perform Swap**: Execute swap operation
7.  **Exception Handling**: Catch invalid indices and input
8.  **Update Tuple**: Apply successful swap
9.  **Continue/Exit**: User controls flow

### Exception Handling

```python
try:
    index_1 = int(input("Which element to Swap: "))
    index_2 = int(input("With which element to Swap: "))
    swap_tuple_ = Swapper.swap(tuple_, index_1, index_2)
except IndexError:
    print("Invalid index")
except ValueError:
    print("Invalid input")
else:
    tuple_ = swap_tuple_

```

**Error Types:**

1.  **IndexError**:
    -   Index out of range
    -   Negative index too large
    -   Accessing non-existent position
    -   Example: index 5 in tuple of length 3
2.  **ValueError**:
    -   Non-numeric input
    -   Cannot convert to int
    -   Invalid format
    -   Example: "abc" instead of number

**Else Clause:**

-   Executes only if no exception occurs
-   Updates tuple with swap result
-   Ensures tuple only changes on success
-   Prevents partial updates on errors

## Project Structure

```
project/
├── main.py              # Main program with interactive loop
├── swapper.py           # Swapper class with swap logic
├── utils.py             # Utility functions (beautify)
└── README.md            # This file

```

## Key Concepts Demonstrated

### Tuple Immutability

```python
# Tuples cannot be modified directly
tuple_ = (1, 2, 3)
tuple_[0] = 5  # TypeError: 'tuple' object does not support item assignment

# Must convert to list first
list_ = list(tuple_)
list_[0] = 5
tuple_ = tuple(list_)  # (5, 2, 3)

```

-   Tuples are immutable sequences
-   Cannot change elements after creation
-   Must convert to list for modification
-   Convert back to tuple after changes
-   Ensures data integrity
-   Memory efficient for read-only data

### Enumerate Function

```python
for index, value in enumerate(tuple_):
    print(f"{index}: {value}")

```

-   Adds counter to iterable
-   Returns (index, value) pairs
-   Cleaner than manual indexing
-   Pythonic iteration pattern
-   Supports custom start value
-   Works with any iterable

### Tuple Unpacking

```python
a, b = b, a  # Swap without temp variable

```

-   Simultaneous assignment
-   Right side creates temporary tuple
-   Left side unpacks values
-   No explicit temporary variable
-   Atomic operation
-   Pythonic and elegant

### Static Methods

```python
@staticmethod
def swap(tuple_, index_1, index_2):
    # No access to self
    return modified_tuple

```

-   Methods callable without instance
-   No access to instance data
-   Class-based organization
-   Utility function pattern
-   Memory efficient
-   Reusable across contexts

### Exception Handling

```python
try:
    # Code that might raise exception
except IndexError:
    # Handle index errors
except ValueError:
    # Handle value errors
else:
    # Execute if no exception

```

-   Graceful error recovery
-   Multiple exception types
-   Specific error handling
-   Else clause for success path
-   User-friendly error messages
-   Continuous operation

### Type Conversion

```python
tuple_ = tuple(input().split())  # String to tuple
list_ = list(tuple_)              # Tuple to list
tuple_ = tuple(list_)             # List to tuple

```

-   Convert between collection types
-   Tuple ↔ List conversion
-   String splitting to list
-   Type flexibility
-   Data structure transformation

### F-String Formatting

```python
print(f"{index}: {value}")

```

-   Modern string formatting
-   Embedded expressions
-   Readable and concise
-   Runtime evaluation
-   Better than % or .format()

## Limitations

⚠️ **Important Limitations:**

1.  **All Input Treated as Strings**
    
    -   `.split()` returns string elements
    -   Numeric input becomes strings
    -   "1 2 3" becomes ('1', '2', '3'), not (1, 2, 3)
    -   Mixed types all become strings
    -   No automatic type detection
2.  **No Input Validation**
    
    -   Accepts empty input
    -   No minimum element check
    -   Assumes valid input format
    -   Can create empty tuples
    -   No element count validation
3.  **No Duplicate Index Check**
    
    -   Allows swapping same index (index_1 == index_2)
    -   Pointless operation
    -   No warning to user
    -   Wastes processing
    -   Should validate indices differ
4.  **No Negative Index Support**
    
    -   Python supports negative indexing
    -   -1 refers to last element
    -   Program doesn't explain this
    -   May confuse users
    -   Could enhance usability
5.  **Limited Error Messages**
    
    -   Generic "Invalid index" message
    -   Doesn't show valid range
    -   No specific guidance
    -   User must guess valid values
    -   Poor user experience
6.  **No Swap History**
    
    -   Cannot undo swaps
    -   No history tracking
    -   Cannot view previous states
    -   Permanent modifications
    -   No rollback feature
7.  **No Bulk Operations**
    
    -   Only swap two elements at a time
    -   No multiple simultaneous swaps
    -   No pattern-based swapping
    -   No reverse operation
    -   Limited functionality
8.  **Inefficient for Large Tuples**
    
    -   Full tuple-list-tuple conversion
    -   O(n) space complexity
    -   Creates complete copies
    -   Not optimized for large data
    -   Memory overhead

### Example of Limitations

```python
# Limitation 1: String input
Input: "1 2 3"
tuple_ = ('1', '2', '3')  # All strings, not integers
# Cannot perform numeric operations

# Limitation 2: No validation
Input: ""  # Empty input
tuple_ = ()  # Empty tuple, no error
# Program continues with empty tuple

# Limitation 3: Duplicate index
index_1 = 2
index_2 = 2
# Swaps element with itself (pointless)
# No warning given

# Limitation 4: Negative index
tuple_ = (1, 2, 3, 4, 5)
index_1 = -1  # Last element (valid in Python)
# May cause IndexError or unexpected behavior
# Not documented for users

# Limitation 5: Error messages
tuple_ = (1, 2, 3)
index_1 = 10  # Out of range
# Output: "Invalid index"
# Should say: "Invalid index. Valid range: 0-2"

# Limitation 6: No history
tuple_ = (1, 2, 3)
# Swap 0 and 2: (3, 2, 1)
# Swap 1 and 2: (3, 1, 2)
# Cannot undo to get back to (3, 2, 1)

# Limitation 7: No bulk operations
# Want to reverse tuple
# Must manually swap multiple times
# No single reverse command

# Limitation 8: Memory usage
tuple_ = tuple(range(1000000))  # Large tuple
# Converts entire tuple to list
# Swaps two elements
# Converts entire list back to tuple
# Inefficient for large data

```

## Potential Enhancements

1.  **Type-Aware Input**
    
    -   Detect numeric strings
    -   Convert to appropriate types
    -   Support mixed types
    -   Preserve original types
    -   Better data handling
    
    ```python
    def parse_input(input_str):
        elements = []
        for item in input_str.split():
            try:
                elements.append(int(item))
            except ValueError:
                try:
                    elements.append(float(item))
                except ValueError:
                    elements.append(item)
        return tuple(elements)
    ```
    
2.  **Input Validation**
    
    -   Check for empty input
    -   Minimum element requirement
    -   Valid index range checking
    -   Duplicate index detection
    -   Comprehensive validation
3.  **Enhanced Error Messages**
    
    -   Show valid index range
    -   Specific error guidance
    -   Helpful suggestions
    -   Better user feedback
    -   Educational messages
    
    ```python
    except IndexError:
        print(f"Invalid index. Valid range: 0-{len(tuple_)-1}")
    ```
    
4.  **Swap History**
    
    -   Track all swap operations
    -   Undo/redo functionality
    -   View history
    -   Rollback to previous state
    -   Complete audit trail
5.  **Bulk Operations**
    
    -   Reverse entire tuple
    -   Rotate elements
    -   Multiple simultaneous swaps
    -   Pattern-based operations
    -   Advanced manipulations
6.  **Negative Index Support**
    
    -   Document negative indexing
    -   Support -1 for last element
    -   Normalize indices
    -   User-friendly indexing
    -   Python-style indexing
7.  **Visual Feedback**
    
    -   Highlight swapped elements
    -   Show before/after comparison
    -   Color-coded output
    -   Animation effects
    -   Better visualization
8.  **Save/Load Functionality**
    
    -   Save tuples to file
    -   Load from file
    -   Export results
    -   Data persistence
    -   Session recovery
9.  **Advanced Swap Options**
    
    -   Swap by value (not just index)
    -   Conditional swapping
    -   Range-based swaps
    -   Custom swap patterns
    -   Flexible operations
10. **Performance Optimization**
    
    -   Lazy evaluation for large tuples
    -   Minimal copying
    -   Efficient algorithms
    -   Memory optimization
    -   Scalability improvements

## Code Quality Features

✅ Object-oriented design  
✅ Static method utilities  
✅ Exception handling  
✅ Tuple immutability handling  
✅ Enumerate usage  
✅ Tuple unpacking for swaps  
✅ Interactive user interface  
✅ Multiple operation support  
✅ Clean code organization  
✅ Type conversion techniques  
✅ F-string formatting  
✅ Error recovery  
✅ User-controlled flow  
✅ No external dependencies  
✅ Modular function design  

## Usage Example

```python
# Running the program
python main.py

# Example session:
========================================
             Tuple Swapper
========================================
Enter tuple elements separated by space: 2 4 5 1
0: 2
1: 4
2: 5
3: 1
Which element to Swap: 0
With which element to Swap: 3
========================================
             Swapped Tuple
========================================
0: 1
1: 4
2: 5
3: 2
Do you want to swap again? (y/n): y
Which element to Swap: 1
With which element to Swap: 3
========================================
             Swapped Tuple
========================================
0: 1
1: 2
2: 5
3: 4
Do you want to swap again? (y/n): n
Do you want to try again? (y/n): n

```

## Notes

-   **Tuple Immutability** - Tuples cannot be modified directly; must convert to list first.
-   **Enumerate Function** - Provides clean way to get index-value pairs during iteration.
-   **Tuple Unpacking** - Pythonic way to swap values without temporary variables.
-   **Exception Handling** - Gracefully handles invalid indices and input errors.
-   Input is treated as strings by default due to `.split()` method.
-   Static methods allow utility functions without instance creation.
-   Interactive loop enables multiple swap operations in one session.
-   Best used as a learning example for tuple operations and exception handling.
-   Running swapper.py directly shows example output with test data.
-   Consider adding type conversion for proper numeric handling in production code.
