
# List Merger

A Python program that merges two lists, removes duplicate elements, and sorts the combined result intelligently. The application handles mixed data types (integers and strings) by sorting them separately and combining them in a logical order. This project demonstrates object-oriented programming, set operations, list manipulation, type checking, and static method implementation in Python.

## Features

1.  **Dual List Input**
    
    -   Accept two separate lists from user
    -   Space-separated input format
    -   Automatic list creation from input
    -   Flexible element entry
    -   Simple input interface
2.  **List Merging**
    
    -   Combines two lists into one
    -   Preserves all elements initially
    -   Automatic concatenation
    -   No manual element copying
    -   Efficient merging process
3.  **Duplicate Removal**
    
    -   Eliminates duplicate elements
    -   Uses set-based deduplication
    -   Preserves unique elements only
    -   Automatic duplicate detection
    -   Clean result output
4.  **Mixed-Type Sorting**
    
    -   Handles integers and strings together
    -   Separates by data type
    -   Sorts each type independently
    -   Integers first, then strings
    -   Intelligent type-aware sorting
5.  **Object-Oriented Design**
    
    -   ListMerger class encapsulation
    -   Instance-based list storage
    -   Static method utilities
    -   Clean separation of concerns
    -   Reusable class structure
6.  **Interactive Loop**
    
    -   Continuous operation mode
    -   User-controlled continuation
    -   Multiple merge operations
    -   Easy exit option
    -   Session-based workflow
7.  **Formatted Output**
    
    -   Beautified program header
    -   Clean result display
    -   User-friendly interface
    -   Professional presentation
    -   Clear visual separation

## How It Works

### ListMerger Class Structure

```python
class ListMerger:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
    
    @staticmethod
    def _remove_duplicates(user_list):
        return list(set(user_list))
    
    def marge_lists(self):
        return self._mixed_sort(self._remove_duplicates((self.list_1 + self.list_2)))
    
    @staticmethod
    def _mixed_sort(user_list):
        int_part = sorted(i for i in user_list if isinstance(i, int))
        str_part = sorted(i for i in user_list if isinstance(i, str))
        return int_part + str_part

```

**Key Components:**

-   **Constructor**: Stores two input lists as instance variables
-   **_remove_duplicates()**: Static method to eliminate duplicate elements
-   **marge_lists()**: Main method orchestrating merge, dedupe, and sort
-   **_mixed_sort()**: Static method for type-aware sorting
-   **Private Methods**: Underscore prefix indicates internal use
-   **Method Chaining**: Operations flow through multiple methods

### Duplicate Removal Algorithm

```python
@staticmethod
def _remove_duplicates(user_list):
    return list(set(user_list))

```

**Process:**

1.  Convert list to set (removes duplicates automatically)
2.  Convert set back to list
3.  Return deduplicated list
4.  Order may change (sets are unordered)
5.  Only unique elements remain

**Example:**

```
Input: [1, 2, 'a', 2, 'a', 3]
set(input): {1, 2, 3, 'a'}
list(set): [1, 2, 3, 'a']  # Order may vary

```

### Mixed-Type Sorting Algorithm

```python
@staticmethod
def _mixed_sort(user_list):
    int_part = sorted(i for i in user_list if isinstance(i, int))
    str_part = sorted(i for i in user_list if isinstance(i, str))
    return int_part + str_part

```

**Process:**

1.  **Separate by Type**:
    -   Filter integers using isinstance() check
    -   Filter strings using isinstance() check
    -   Create two separate lists
2.  **Sort Each Type**:
    -   Sort integers numerically
    -   Sort strings alphabetically
3.  **Combine Results**:
    -   Integers first
    -   Strings second
    -   Return concatenated list

**Example:**

```
Input: [5, 'z', 1, 'a', 3, 'b']

Filtering:
- int_part: [5, 1, 3]
- str_part: ['z', 'a', 'b']

Sorting:
- sorted(int_part): [1, 3, 5]
- sorted(str_part): ['a', 'b', 'z']

Result: [1, 3, 5, 'a', 'b', 'z']

```

### Main Merge Method

```python
def marge_lists(self):
    return self._mixed_sort(self._remove_duplicates((self.list_1 + self.list_2)))

```

**Process Flow:**

1.  **Concatenate**: `self.list_1 + self.list_2`
    -   Combines both lists
    -   Creates single merged list
2.  **Remove Duplicates**: `_remove_duplicates(...)`
    -   Eliminates duplicate elements
    -   Returns unique elements only
3.  **Sort**: `_mixed_sort(...)`
    -   Separates by type
    -   Sorts each type
    -   Combines in order
4.  **Return**: Final sorted, deduplicated list

**Complete Example:**

```
list_1 = [1, 2, 'a', 'z', 5]
list_2 = [4, 'A', 6, 7, 8]

Step 1 - Concatenate:
[1, 2, 'a', 'z', 5, 4, 'A', 6, 7, 8]

Step 2 - Remove Duplicates:
[1, 2, 'a', 'z', 5, 4, 'A', 6, 7, 8]  # No duplicates in this case

Step 3 - Mixed Sort:
int_part: [1, 2, 4, 5, 6, 7, 8]
str_part: ['A', 'a', 'z']

Final Result:
[1, 2, 4, 5, 6, 7, 8, 'A', 'a', 'z']

```

### User Input Processing

```python
while True:
    list_1 = input("Enter list 1: ").split()
    list_2 = input("Enter list 2: ").split()
    
    merger = ListMerger(list_1, list_2)
    print(merger.marge_lists())

    if input("Do you want to continue? (y/n): ") == "n":
        exit()

```

**Process:**

1.  Get space-separated input for list 1
2.  Split input into list elements
3.  Get space-separated input for list 2
4.  Split input into list elements
5.  Create ListMerger instance
6.  Call marge_lists() and print result
7.  Ask user to continue or exit
8.  Loop until user chooses to exit

**Note:** Input is always treated as strings since `.split()` returns string elements. For numeric sorting, elements would need to be converted to integers.

### Type Checking with isinstance()

```python
isinstance(i, int)   # Check if i is an integer
isinstance(i, str)   # Check if i is a string

```

**How it works:**

-   Runtime type identification
-   Returns True if object is of specified type
-   Returns False otherwise
-   Works with built-in and custom types
-   Essential for mixed-type handling

**Examples:**

```python
isinstance(5, int)        # True
isinstance("hello", str)  # True
isinstance(5, str)        # False
isinstance("5", int)      # False

```

## Project Structure

```
project/
├── main.py              # Main program with input loop
├── merger.py            # ListMerger class with merge logic
├── utils.py             # Utility functions (beautify)
└── README.md            # This file

```

## Key Concepts Demonstrated

### Set-Based Deduplication

```python
list(set(user_list))

```

-   Sets automatically remove duplicates
-   Unordered collection of unique elements
-   Fast membership testing
-   Efficient duplicate removal
-   Simple one-line deduplication
-   Type-agnostic operation

### List Concatenation

```python
self.list_1 + self.list_2

```

-   Combines two lists into one
-   Creates new list (doesn't modify originals)
-   Preserves order from both lists
-   Simple and readable syntax
-   Efficient operation
-   Works with any list types

### List Comprehension with Filtering

```python
sorted(i for i in user_list if isinstance(i, int))

```

-   Generator expression for filtering
-   Conditional element selection
-   Type-based filtering
-   Memory efficient
-   Readable and concise
-   Combined with sorting

### Static Methods

```python
@staticmethod
def _remove_duplicates(user_list):
    return list(set(user_list))

```

-   Methods callable without instance
-   No access to instance data (self)
-   Utility function organization
-   Class-based grouping
-   Memory efficient
-   Reusable across instances

### Object-Oriented Encapsulation

```python
class ListMerger:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

```

-   Data encapsulation in objects
-   Instance variables for state
-   Methods for behavior
-   Clean interface design
-   Reusable class structure
-   Separation of concerns

### Private Method Convention

```python
def _remove_duplicates(user_list):  # Leading underscore
def _mixed_sort(user_list):         # Indicates private/internal

```

-   Underscore prefix convention
-   Indicates internal use only
-   Not enforced by Python
-   Documentation through naming
-   Best practice for encapsulation
-   Clear API boundaries

### String Splitting

```python
input("Enter list 1: ").split()

```

-   Splits by whitespace by default
-   Returns list of strings
-   Handles multiple spaces
-   Easy input parsing
-   Removes leading/trailing spaces
-   Common input pattern

## Limitations

⚠️ **Important Limitations:**

1.  **All Input Treated as Strings**
    
    -   `.split()` returns string elements
    -   Numeric input becomes strings
    -   "1 2 3" becomes ['1', '2', '3'], not [1, 2, 3]
    -   Sorting works alphabetically, not numerically
    -   "10" comes before "2" in string sort
2.  **Incorrect Numeric Sorting**
    
    -   String sorting: ['1', '10', '2', '3']
    -   Expected numeric: [1, 2, 3, 10]
    -   Alphabetical order for numbers
    -   Misleading results for numeric data
    -   Type conversion needed
3.  **Type Detection Never Triggers for Integers**
    
    -   `isinstance(i, int)` always False for input
    -   All elements are strings from `.split()`
    -   int_part always empty
    -   Only str_part populated
    -   Mixed-type logic unused
4.  **No Input Validation**
    
    -   Accepts empty input
    -   No error handling
    -   Assumes valid input format
    -   No type checking
    -   Can crash on invalid input
5.  **Case-Sensitive String Sorting**
    
    -   'A' comes before 'a' in ASCII
    -   Uppercase and lowercase not normalized
    -   ['A', 'a', 'z'] sorted as ['A', 'a', 'z']
    -   May not match user expectations
    -   No case-insensitive option
6.  **No Duplicate Count Display**
    
    -   Doesn't show how many duplicates removed
    -   Silent deduplication
    -   No before/after comparison
    -   Limited user feedback
    -   No statistics
7.  **Set Order Not Preserved**
    
    -   Sets are unordered
    -   Original order lost during deduplication
    -   Unpredictable intermediate order
    -   Relies on final sort for order
    -   May affect debugging
8.  **Spelling Error in Method Name**
    
    -   `marge_lists()` instead of `merge_lists()`
    -   Typo in method name
    -   Inconsistent with standard terminology
    -   May confuse users
    -   Poor code quality

### Example of Limitations

```python
# Limitation 1 & 2: String sorting issue
Input: "10 2 5 1"
list_1 = ['10', '2', '5', '1']  # All strings!
sorted: ['1', '10', '2', '5']   # Alphabetical, not numeric
Expected: [1, 2, 5, 10]         # Numeric order

# Limitation 3: Type detection never works
list_1 = ['1', '2', '3']  # All strings from split()
isinstance('1', int)      # False (it's a string!)
int_part = []             # Always empty
str_part = ['1', '2', '3']  # All elements here

# Limitation 4: No validation
Input: ""  # Empty input
list_1 = []  # Empty list, no error
merger = ListMerger([], [])  # Accepts empty lists

# Limitation 5: Case sensitivity
Input: "apple Apple APPLE"
sorted: ['APPLE', 'Apple', 'apple']  # Uppercase first
Expected (case-insensitive): ['apple', 'apple', 'apple']

# Limitation 6: No duplicate feedback
list_1 = ['a', 'b', 'a']
list_2 = ['b', 'c']
Result: ['a', 'b', 'c']
# Doesn't tell user: removed 2 duplicates

# Limitation 7: Order lost
Input: ['z', 'a', 'm', 'a']
After set: {'z', 'a', 'm'}  # Order unpredictable
After list: ['a', 'm', 'z'] or ['z', 'm', 'a'] or other
After sort: ['a', 'm', 'z']  # Final order restored

# Limitation 8: Spelling error
merger.marge_lists()  # Should be merge_lists()

```

## Potential Enhancements

1.  **Numeric Input Support**
    
    -   Convert numeric strings to integers
    -   Type detection during input
    -   Proper numeric sorting
    -   Mixed type handling
    -   User-specified type conversion
    
    ```python
    def parse_input(input_str):
        elements = []
        for item in input_str.split():
            try:
                elements.append(int(item))
            except ValueError:
                elements.append(item)
        return elements
    ```
    
2.  **Input Validation**
    
    -   Check for empty input
    -   Validate element format
    -   Error messages for invalid input
    -   Type checking
    -   Graceful error handling
3.  **Case-Insensitive Sorting Option**
    
    -   Normalize string case
    -   User-configurable case handling
    -   Case-insensitive comparison
    -   Better string sorting
    -   More flexible sorting
4.  **Duplicate Statistics**
    
    -   Count duplicates removed
    -   Show before/after counts
    -   Display duplicate elements
    -   Detailed merge report
    -   User feedback
5.  **Fix Method Name**
    
    -   Rename `marge_lists()` to `merge_lists()`
    -   Correct spelling
    -   Professional naming
    -   Standard terminology
    -   Better code quality
6.  **Custom Sorting Options**
    
    -   Ascending/descending order
    -   Custom sort key
    -   Multiple sort criteria
    -   User-defined order
    -   Flexible sorting
7.  **Return Value Enhancement**
    
    -   Return dictionary with statistics
    -   Include original lists
    -   Duplicate count
    -   Merge metadata
    -   Comprehensive results
    
    ```python
    def merge_lists(self):
        merged = self.list_1 + self.list_2
        unique = self._remove_duplicates(merged)
        sorted_list = self._mixed_sort(unique)
        
        return {
            'result': sorted_list,
            'original_count': len(merged),
            'unique_count': len(unique),
            'duplicates_removed': len(merged) - len(unique)
        }
    ```
    
8.  **File Input Support**
    
    -   Read lists from files
    -   Multiple list processing
    -   Batch operations
    -   Export results
    -   Data persistence
9.  **Advanced Sorting**
    
    -   Natural sorting (1, 2, 10 instead of 1, 10, 2)
    -   Locale-aware sorting
    -   Custom comparators
    -   Multi-level sorting
    -   Sort by length, then alphabetically
10. **Visual Feedback**
    
    -   Show merge process steps
    -   Highlight duplicates
    -   Color-coded output
    -   Progress indicators
    -   Interactive display

## Code Quality Features

✅ Object-oriented design  
✅ Set-based deduplication  
✅ Type-aware sorting  
✅ Static method utilities  
✅ List comprehension with filtering  
✅ Method chaining  
✅ Private method convention  
✅ Instance variable encapsulation  
✅ Interactive user interface  
✅ Continuous operation loop  
✅ Clean code organization  
✅ Modular function design  
✅ Reusable class structure  
✅ Simple and readable logic  
✅ No external dependencies  

## Notes

-   **Input Type Issue** - Current implementation treats all input as strings due to `.split()`, making the integer sorting logic ineffective.
-   **Spelling Error** - Method name `marge_lists()` should be `merge_lists()`.
-   Set-based deduplication is efficient but doesn't preserve original order.
-   Mixed-type sorting separates integers and strings for logical ordering.
-   Static methods allow utility functions without instance creation.
-   Private method naming (underscore prefix) indicates internal use.
-   Interactive loop allows multiple merge operations in one session.
-   Best used as a learning example for OOP and list operations.
-   Consider type conversion for proper numeric handling in production code.
-   Running merger.py directly shows example output with proper integer types.