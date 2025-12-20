
# File Reader with Line Count

An interactive command-line application for managing text files with advanced features including line counting, writing, reading, and file clearing. This project demonstrates file I/O operations, input validation, error handling, and object-oriented programming in Python.

## Features

1.  **Write to File**
    
    -   Add multiple lines to a file sequentially
    -   Input validation prevents empty entries
    -   Automatic newline insertion after each entry
    -   Appends to existing content
2.  **Read from File**
    
    -   Display complete file contents
    -   Shows all stored data in proper format
    -   Readable sequential output
    -   Preserves line structure and formatting
3.  **Count Lines**
    
    -   Counts total number of lines in file
    -   Provides instant line count statistics
    -   Useful for file monitoring
    -   Real-time count on demand
4.  **Clear File**
    
    -   Remove all content from file
    -   Single operation file reset
    -   Confirmation message on completion
    -   Prepares file for fresh start
5.  **Input Validation**
    
    -   Prevents empty string submission
    -   Validates user input before processing
    -   Raises ValueError for invalid input
    -   User-friendly error messages
6.  **Error Handling**
    
    -   Try-except blocks for all file operations
    -   Handles FileNotFoundError gracefully
    -   Handles FileExistsError exceptions
    -   Proper exception propagation
7.  **Interactive Menu System**
    
    -   User-friendly command-line interface
    -   Clear operation options
    -   Menu-driven continuous operation
    -   Easy navigation and exit

## How It Works

### LineCount Class Structure

```python
FILE_NAME = "file.txt"

class LineCount:
    @staticmethod
    def write_lines():
        try:
            with open(FILE_NAME, "a") as file:
                file.write(functionalities.usr_input())
        except FileExistsError as e:
            raise e
    
    @staticmethod
    def read_lines():
        try:
            with open(FILE_NAME, "r") as file:
                return file.read()
        except FileNotFoundError as e:
            raise e
    
    @staticmethod
    def count_lines():
        try:
            with open(FILE_NAME, "r") as file:
                return len(file.readlines())
        except FileNotFoundError as e:
            raise e
    
    @staticmethod
    def clear_file():
        try:
            with open(FILE_NAME, "w") as file:
                file.write("")
                print("File has been Cleared")
        except FileNotFoundError as e:
            raise e

```

**Key Components:**

-   **FILE_NAME Constant**: Centralized file path configuration
-   **write_lines() Method**: Appends validated user input to file
-   **read_lines() Method**: Retrieves and returns complete file content
-   **count_lines() Method**: Counts total lines using readlines()
-   **clear_file() Method**: Clears all file content and displays confirmation
-   **@staticmethod Decorator**: Methods callable without instance creation
-   **Try-except Blocks**: Exception handling for file operations

### Input Validation Logic

```python
def usr_input():
    lines = input("Enter your Input: ")
    if lines == "":
        raise ValueError("Input cannot be empty")
    return lines + "\n"

```

**Validation Process:**

1.  Prompt user for input
2.  Check if input is empty string
3.  Raise ValueError if empty
4.  Add newline character if valid
5.  Return validated input

### Write Operation Flow

```python
def write_lines():
    try:
        with open(FILE_NAME, "a") as file:
            file.write(functionalities.usr_input())
    except FileExistsError as e:
        raise e

```

**Process:**

1.  Try to open file in append mode
2.  Call validated usr_input() function
3.  Write input with newline to file
4.  File automatically closes
5.  Catch and propagate FileExistsError if occurs

### Read Operation Flow

```python
def read_lines():
    try:
        with open(FILE_NAME, "r") as file:
            return file.read()
    except FileNotFoundError as e:
        raise e

```

**Process:**

1.  Try to open file in read mode
2.  Read entire file content
3.  Return complete text
4.  Catch FileNotFoundError if file missing

### Line Count Operation Flow

```python
def count_lines():
    try:
        with open(FILE_NAME, "r") as file:
            return len(file.readlines())
    except FileNotFoundError as e:
        raise e

```

**Process:**

1.  Open file in read mode
2.  Use readlines() to get list of all lines
3.  Return length of line list
4.  Handle missing file exception

### Clear Operation Flow

```python
def clear_file():
    try:
        with open(FILE_NAME, "w") as file:
            file.write("")
            print("File has been Cleared")
    except FileNotFoundError as e:
        raise e

```

**Process:**

1.  Open file in write mode (truncates file)
2.  Write empty string to ensure clarity
3.  Display confirmation message
4.  Handle exceptions

### Program Flow (main.py)

```
1. Display menu with beautify()
2. Show operation options (1, 2, 3, 4, 0)
3. Get user choice input
4. Match choice to operation:
   - Case 1: Write validated input to file
   - Case 2: Read and display file contents
   - Case 3: Count and display line count
   - Case 4: Clear file and show confirmation
   - Case 0: Exit program gracefully
5. Loop until user chooses exit

```

## Project Structure

```
project/
├── main.py              # Main program with menu interface
├── line_count.py        # LineCount class with file operations
├── functionalities.py   # Utility functions and validation
├── file.txt             # File created automatically
└── README.md            # This file

```

## Key Concepts Demonstrated

### Static Methods

```python
@staticmethod
def write_lines():
    with open(FILE_NAME, "a") as file:
        file.write(functionalities.usr_input())

```

-   Methods don't require instance creation
-   Called via ClassName.method()
-   Shared utility functions
-   No access to instance data
-   Useful for stateless operations

### Try-Except Exception Handling

```python
try:
    with open(FILE_NAME, "r") as file:
        return file.read()
except FileNotFoundError as e:
    raise e

```

-   Catches specific exceptions
-   Graceful error handling
-   Preserves exception information
-   Allows error propagation
-   Better than program crash

### Custom Exceptions (ValueError)

```python
if lines == "":
    raise ValueError("Input cannot be empty")

```

-   User-defined exception raising
-   Input validation enforcement
-   Clear error messages
-   Prevents invalid data entry
-   Application-level checks

### File Operations with Different Modes

```python
"a" - Append mode    # Add lines
"r" - Read mode      # Read content
"w" - Write mode     # Clear/overwrite

```

-   Different modes for different operations
-   Append preserves data
-   Read retrieves data
-   Write truncates file

### readlines() vs read()

```python
file.readlines()  # Returns list of lines
file.read()       # Returns complete string

```

-   readlines() useful for line operations
-   read() useful for complete content
-   readlines() facilitates line counting
-   Different use cases

### Module Organization

```python
import functionalities
from line_count import LineCount

```

-   Separate concerns into modules
-   Utility functions in dedicated module
-   Class operations in separate file
-   Main logic in main.py
-   Clean imports

### Menu-Driven Application with Match

```python
match choice:
    case "1": LineCount.write_lines()
    case "2": print(LineCount.read_lines())
    case "3": print(f"Number of lines: {LineCount.count_lines()}")
    case "0": exit()
    case _: print("Invalid Input")

```

-   Modern Python pattern matching
-   Clean syntax vs if-elif-else
-   Default case with underscore
-   User-driven control flow

## Limitations

⚠️ **Important Limitations:**

1.  **File Creation on First Run**
    
    -   Operations fail if file doesn't exist initially
    -   First read/count fails before any write
    -   Clear fails if file never created
    -   No automatic file creation
2.  **No Line Number Tracking**
    
    -   Cannot reference or delete specific lines
    -   Cannot insert at specific line position
    -   Cannot modify individual lines
    -   Cannot retrieve line by number
3.  **Limited Input Validation**
    
    -   Only checks for empty strings
    -   Doesn't limit line length
    -   Accepts duplicate content
    -   No special character filtering
4.  **Single File Only**
    
    -   Hardcoded file name
    -   Cannot switch between files
    -   No file management options
    -   No multiple file support
5.  **No Backup or Recovery**
    
    -   Clear operation is permanent
    -   No undo functionality
    -   No version history
    -   Data loss on accidental clear
6.  **Exception Propagation**
    
    -   Exceptions raised but not caught in main
    -   Program crashes on FileNotFoundError
    -   No user-friendly error messages in menu
    -   Better error handling needed
7.  **No Character Encoding Specification**
    
    -   Uses default system encoding
    -   May fail with special characters
    -   Unicode issues possible
    -   No UTF-8 guarantee

## Potential Enhancements

1.  **Robust Error Handling**
    
    -   Catch exceptions in main.py
    -   Display user-friendly error messages
    -   Provide recovery options
    -   Log errors to file
    -   Continue program after error
2.  **File Management**
    
    -   Create file if doesn't exist
    -   Check file existence before operations
    -   List available files
    -   Switch between files
    -   File metadata display
3.  **Advanced Line Operations**
    
    -   View specific line by number
    -   Delete specific line(s)
    -   Insert line at position
    -   Modify/edit specific line
    -   Search for lines containing text
4.  **Input Enhancement**
    
    -   Limit maximum line length
    -   Prevent duplicate lines
    -   Accept multi-line input
    -   Timestamp each entry
    -   User/author tracking
5.  **Output Options**
    
    -   Display line numbers
    -   Show file statistics (lines, characters, words)
    -   Format output differently
    -   Export to different formats
    -   Color-coded output
6.  **Data Persistence**
    
    -   Automatic backup creation
    -   Version history tracking
    -   Undo/redo functionality
    -   Save snapshots
    -   Recovery options
7.  **Multiple File Support**
    
    -   Create/select different files
    -   Copy/move between files
    -   Merge files
    -   Compare files
    -   File organization
8.  **Advanced Features**
    
    -   Sort lines
    -   Remove duplicates
    -   Filter by pattern
    -   Search and replace
    -   Analytics dashboard

## Code Quality Features

✅ Input validation with custom exceptions  
✅ Comprehensive error handling with try-except  
✅ Modular design with separate files  
✅ Utility functions properly organized  
✅ Static methods for stateless operations  
✅ Context managers for safe file handling  
✅ Menu-driven user interface  
✅ Clear separation of concerns  
✅ Descriptive variable and function names  
✅ Centralized file name configuration  
✅ Formatted output with beautify utility  
✅ Reusable LineCount class  
✅ Modern Python syntax (match statement)  
✅ Exception propagation for error tracking  
✅ Interactive user-friendly application  
✅ Practical real-world file management features