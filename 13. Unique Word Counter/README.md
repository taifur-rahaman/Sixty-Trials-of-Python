
# Unique Word Counter

An interactive command-line application that analyzes lists, tuples, and strings to detect duplicate elements and count unique items. The program provides multiple input methods for different data structures and performs duplicate detection and unique element counting operations. This project demonstrates set operations, data structure conversion, static methods, and menu-driven application design in Python.

## Features

1.  **List Input Mode**
    
    -   Accept multiple elements for list creation
    -   User-specified number of elements
    -   Interactive element entry
    -   Duplicate detection for lists
    -   Unique element counting
2.  **Tuple Input Mode**
    
    -   Space-separated element input
    -   Automatic conversion to tuple
    -   Sorted tuple output
    -   Duplicate detection for tuples
    -   Unique word counting
3.  **String Input Mode**
    
    -   Accept string input from user
    -   Character-level analysis
    -   Duplicate character detection
    -   Unique letter counting
    -   String-specific processing
4.  **Duplicate Detection**
    
    -   Identifies presence of duplicate elements
    -   Uses set-based comparison
    -   Works across different data types
    -   Automatic duplicate checking
    -   Clear user feedback
5.  **Unique Element Counting**
    
    -   Counts total unique elements
    -   Works with lists, tuples, strings
    -   Automatic calculation
    -   Instant reporting
    -   Accurate counting
6.  **Multiple Data Structure Support**
    
    -   List handling with numeric input
    -   Tuple creation from space-separated input
    -   String analysis at character level
    -   Flexible data type processing
    -   Type-aware counting
7.  **Interactive Menu System**
    
    -   User-friendly command-line interface
    -   Clear operation options
    -   Easy navigation between modes
    -   Graceful exit functionality
    -   Continuous operation loop
8.  **Input Validation**
    
    -   Type conversion handling
    -   Element validation
    -   User-friendly error messages
    -   Handles edge cases
    -   Prevents invalid operations

## How It Works

### UniqueWord Class Structure

```python
class UniqueWord:
    def __init__(self):
        pass
    
    @staticmethod
    def check_duplicate(iterable):
        if sorted(tuple(set(iterable))) == sorted(tuple(iterable)):
            return False
        return True
    
    @staticmethod
    def count_unique_word(iterable):
        if isinstance(iterable, str):
            return len(list(iterable))
        return len(iterable)

```

**Key Components:**

-   **Constructor**: Empty initialization (can be enhanced)
-   **check_duplicate() Method**: Detects if duplicates exist using set comparison
-   **count_unique_word() Method**: Counts unique elements in iterable
-   **@staticmethod Decorator**: Methods callable without instance
-   **Type Checking**: Handles strings differently from other iterables

### Duplicate Detection Logic

```python
@staticmethod
def check_duplicate(iterable):
    if sorted(tuple(set(iterable))) == sorted(tuple(iterable)):
        return False
    return True

```

**Process:**

1.  Convert iterable to set (removes duplicates)
2.  Convert set back to tuple
3.  Sort the tuple
4.  Compare with sorted version of original
5.  If equal → no duplicates (return False)
6.  If different → has duplicates (return True)

**Example:**

```
Input: [1, 2, 3, 2]
set(input): {1, 2, 3}
sorted(set): (1, 2, 3)
sorted(input): (1, 2, 2, 3)
(1, 2, 3) != (1, 2, 2, 3) → Has duplicates (return True)

```

### Unique Count Logic

```python
@staticmethod
def count_unique_word(iterable):
    if isinstance(iterable, str):
        return len(list(iterable))
    return len(iterable)

```

**Process for Lists/Tuples:**

1.  Get length of iterable directly
2.  Return as unique count (assumes no duplicates)

**Process for Strings:**

1.  Convert string to list of characters
2.  Get length of character list
3.  Return as total character count

**Note:** This counts total elements, not unique elements. For true unique count, should use `len(set(iterable))`

### List Input Flow

```python
def list_input():
    usr_list = []
    n = int(input("Enter Number of Elements: "))
    
    for i in range(n):
        usr_list.append(input(f"Enter Element {i+1}: "))
    
    if UniqueWord.check_duplicate(usr_list):
        print("List Contains Duplicate Elements")
        return
    else:
        print(f"Total Unique Words: {UniqueWord.count_unique_word(usr_list)}")

```

**Process:**

1.  Prompt for number of elements
2.  Loop n times, collecting input
3.  Append each element to list
4.  Check for duplicates
5.  If duplicates exist, display message
6.  If no duplicates, display count

### Tuple Input Flow

```python
def tuple_list():
    usr_tuple = sorted(tuple(input("Enter the elements separate by space: ").split()))
    
    if UniqueWord.check_duplicate(usr_tuple):
        print("Tuple Contains Duplicate Elements")
        return
    else:
        print(f"Total Unique Words: {UniqueWord.count_unique_word(usr_tuple)}")

```

**Process:**

1.  Get space-separated input
2.  Split by space into list
3.  Convert to tuple
4.  Sort the tuple
5.  Check for duplicates
6.  Display result

### String Input Flow

```python
def string_input():
    usr_string = input("Enter the string: ")
    
    if UniqueWord.check_duplicate(usr_string):
        print("String Contains Duplicate Elements")
        return
    else:
        print(f"Total Unique Letters: {UniqueWord.count_unique_word(usr_string)}")

```

**Process:**

1.  Get string input from user
2.  Check for duplicate characters
3.  If duplicates exist, display message
4.  If no duplicates, count and display

### Program Flow (main.py)

```
1. Display menu with beautify()
2. Show operation options (1, 2, 3, 0)
3. Get user choice
4. Match choice to operation:
   - Case 1: Call list_input()
   - Case 2: Call tuple_list()
   - Case 3: Call string_input()
   - Case 0: Exit program
5. Loop until user chooses exit

```

## Project Structure

```
project/
├── main.py              # Main program with menu interface
├── unique_words.py      # UniqueWord class with detection logic
├── functionalities.py   # Functions for different data types
├── utils.py             # Utility functions (beautify)
└── README.md            # This file

```

## Key Concepts Demonstrated

### Set Data Structure for Deduplication

```python
set(iterable)

```

-   Removes duplicate elements automatically
-   Unordered collection
-   Fast membership testing
-   Useful for duplicate detection
-   Foundation of duplicate checking logic

### Sorting and Comparison

```python
sorted(tuple(set(iterable))) == sorted(tuple(iterable))

```

-   Sort both versions for comparison
-   Sorted order removes ordering differences
-   Works across different iterables
-   Reliable duplicate detection
-   Equality operator for verification

### Type Checking with isinstance()

```python
if isinstance(iterable, str):
    return len(list(iterable))
return len(iterable)

```

-   Runtime type identification
-   Different handling for strings
-   Flexible function behavior
-   Type-aware operations
-   Polymorphic handling

### Static Methods

```python
@staticmethod
def check_duplicate(iterable):
    ...

```

-   Methods callable without instance
-   No access to instance data
-   Utility method organization
-   Cleaner function grouping
-   Memory efficient

### Iterable Conversion

```python
list(iterable)      # Convert to list
tuple(iterable)     # Convert to tuple
set(iterable)       # Convert to set

```

-   Convert between different types
-   Preserve or modify elements
-   Set-based operations
-   List comprehension ready
-   Type flexibility

### String Splitting

```python
input("...").split()

```

-   Split by whitespace by default
-   Returns list of tokens
-   Easy word separation
-   Clean input parsing
-   Flexible delimiter

### Input Validation and Type Conversion

```python
n = int(input("Enter Number of Elements: "))

```

-   Convert string input to integer
-   Direct type casting
-   Used for loop ranges
-   Can raise ValueError
-   Basic validation

### Menu-Driven Application with Match

```python
match choice:
    case "1": func.list_input()
    case "2": func.tuple_list()
    case "3": func.string_input()
    case "0": exit()
    case "_": print("Invalid Input")

```

-   Pattern matching for clean code
-   Multiple operation handling
-   Default case with underscore
-   User-driven control flow
-   Easy menu management

## Limitations

⚠️ **Important Limitations:**

1.  **count_unique_word() Counts Total, Not Unique**
    
    -   Returns total elements, not unique count
    -   When no duplicates exist, happens to be correct
    -   With duplicates, count is misleading
    -   Function name suggests unique count but doesn't deliver
2.  **No True Unique Count Functionality**
    
    -   No method to count actual unique elements
    -   Cannot determine unique count with duplicates
    -   User sees total count only
    -   Limited analysis capability
    -   Misleading function behavior
3.  **Early Exit on Duplicate Detection**
    
    -   Program exits when duplicates found
    -   Cannot see results with duplicates
    -   No option to continue analysis
    -   Limited flexibility
    -   All-or-nothing approach
4.  **Case-Sensitive String Analysis**
    
    -   "Hello" and "hello" treated as different
    -   Uppercase and lowercase not normalized
    -   May give unexpected results
    -   Not user-friendly for case-insensitive comparison
5.  **Whitespace Handling**
    
    -   Spaces treated as separate characters
    -   "hello world" counts space as character
    -   May not be intended behavior
    -   No trimming or normalization
6.  **No Input Validation for Lists**
    
    -   Accepts empty elements
    -   Accepts numeric and string mix
    -   No duplicate name checking
    -   No length limits
    -   Allows special characters
7.  **Tuple Sorting Limitation**
    
    -   Tuple is always sorted
    -   Cannot preserve original order
    -   Only alphabetical/numeric sort
    -   Not customizable
    -   May not match user expectations
8.  **No Data Persistence**
    
    -   Results not saved
    -   No history of analyses
    -   Cannot export results
    -   Single-session only
    -   No record keeping

### Example of Limitations

```python
# Limitation 1 & 2: Misleading count with duplicates
data = ["apple", "banana", "apple"]
has_dup = UniqueWord.check_duplicate(data)  # True
count = UniqueWord.count_unique_word(data)  # 3 (total, not unique!)
# Should be 2 unique, but shows 3

# Limitation 3: Early exit on duplicates
data = [1, 2, 2, 3]
if check_duplicate(data):
    print("Duplicates found")  # Exits here
    return  # Cannot see count or analysis

# Limitation 4: Case sensitivity
data = "Hello"
has_dup = check_duplicate(data)  # True (because of 'l')
# But: "HELLO" has same 'l's just uppercase

# Limitation 5: Whitespace counts
data = "hello world"
count = count_unique_word(data)  # 11 (includes space)
# Space is counted as character

# Limitation 6: No validation
UniqueWord.check_duplicate(["", "apple"])  # Accepts empty
UniqueWord.check_duplicate([123, "456"])  # Accepts mixed types

# Limitation 7: Always sorted tuple
input: "zebra apple banana"
tuple output: ('apple', 'banana', 'zebra')  # Always sorted

# Limitation 8: No persistence
analyze_data()  # Results disappear after exit
# Cannot retrieve previous analysis

```
## Potential Enhancements

1.  **True Unique Count**
    
    -   Add method to count actual unique elements
    -   Display count even with duplicates
    -   Use len(set(iterable))
    -   Accurate reporting
    -   Better function naming
2.  **Display Unique Elements**
    
    -   Show which elements are unique
    -   List duplicate elements
    -   Frequency analysis
    -   Visual representation
    -   Detailed results
3.  **Case-Insensitive Analysis**
    
    -   Normalize string input
    -   Case-insensitive comparison
    -   Better string handling
    -   More user-friendly
    -   Configurable case sensitivity
4.  **Whitespace Handling**
    
    -   Strip leading/trailing spaces
    -   Handle multiple spaces
    -   Normalize whitespace
    -   Better character counting
    -   Cleaner input
5.  **Input Validation**
    
    -   Validate element content
    -   Check for empty elements
    -   Limit element length
    -   Type consistency checking
    -   Data sanitization
6.  **Data Persistence**
    
    -   Save analysis results
    -   Export to file
    -   History tracking
    -   Previous results retrieval
    -   Report generation
7.  **Advanced Analysis**
    
    -   Frequency distribution
    -   Character frequency charts
    -   Word frequency analysis
    -   Statistical reports
    -   Visual graphs
8.  **Flexible Tuple Handling**
    
    -   Option to preserve order
    -   Custom sorting options
    -   No forced sorting
    -   User-defined order
    -   Sort configuration
9.  **Batch Processing**
    
    -   Process multiple inputs
    -   Compare multiple datasets
    -   Batch analysis
    -   Comparative results
    -   Multiple file input
10.  **User Experience**
        -   Detailed output formatting
        -   Color-coded results
        -   Visual indicators
        -   Interactive prompts
        -   Helpful messages


## Code Quality Features

✅ Set-based duplicate detection  
✅ Static methods for utility operations  
✅ Type checking with isinstance()  
✅ Iterable conversion between types  
✅ Menu-driven user interface  
✅ Modular function organization  
✅ Multiple data structure support  
✅ Clear separation of concerns  
✅ String splitting and input handling  
✅ User-friendly output messages  
✅ Formatted beautified headers  
✅ Reusable utility functions  
✅ Modern Python syntax (match statement)  
✅ Flexible polymorphic handling  
✅ Simple and readable code logic