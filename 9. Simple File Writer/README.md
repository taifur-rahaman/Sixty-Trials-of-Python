
# File Editor

A command-line file management application that provides an interactive interface for writing, reading, and deleting file contents. This project demonstrates file I/O operations, object-oriented programming, and menu-driven application design in Python.

## Features

1.  **Write to File**
    
    -   Append text content to a file
    -   Preserves existing content (append mode)
    -   Each input is written on a new line
    -   Automatic line break insertion
2.  **Read from File**
    
    -   Display complete file contents
    -   Shows all written data in sequential order
    -   Readable formatted output
    -   Retrieves entire file at once
3.  **Delete File Contents**
    
    -   Clear all data from the file
    -   Resets file to empty state
    -   Single operation with confirmation
    -   Useful for starting fresh
4.  **Interactive Menu System**
    
    -   User-friendly command-line interface
    -   Clear navigation options
    -   Menu-driven program flow
    -   Continuous operation until exit
5.  **File Management**
    
    -   Persistent storage using local text file
    -   Automatic file creation if not exists
    -   Safe file handling with context managers
    -   Centralized file name configuration
6.  **Utility Functions**
    
    -   Formatted title displays
    -   Centered text output
    -   Consistent visual formatting
    -   Reusable formatting utilities

## How It Works

### FileEditor Class Structure

```python
FILE_NAME = "file.txt"

class FileEditor:
    @staticmethod
    def write_file(string):
        with open(FILE_NAME, "a") as file:
            file.write(string + "\n")
    
    @staticmethod
    def read_file():
        with open(FILE_NAME, "r") as file:
            return file.read()
    
    @staticmethod
    def delete_content():
        with open(FILE_NAME, "w") as file:
            pass

```

**Key Components:**

-   **FILE_NAME Constant**: Centralized file path configuration
-   **write_file() Method**: Appends user input to file with newline
-   **read_file() Method**: Reads and returns complete file contents
-   **delete_content() Method**: Clears file by opening in write mode
-   **@staticmethod Decorator**: Methods don't require instance creation

### File Operation Modes

```python
open(FILE_NAME, "a")  # Append mode - adds to existing content
open(FILE_NAME, "r")  # Read mode - retrieves file contents
open(FILE_NAME, "w")  # Write mode - clears and overwrites file

```

**Mode Behaviors:**

-   **Append ("a")**: New content added at end, existing data preserved
-   **Read ("r")**: Opens file for reading, fails if file doesn't exist
-   **Write ("w")**: Opens file in write mode, truncates (clears) existing content

### Write Operation Flow

```python
def write_file(string):
    with open(FILE_NAME, "a") as file:
        file.write(string + "\n")

```

**Process:**

1.  User enters text input
2.  Open file in append mode
3.  Write input string to file
4.  Append newline character
5.  Automatically close file

### Read Operation Flow

```python
def read_file():
    with open(FILE_NAME, "r") as file:
        return file.read()

```

**Process:**

1.  Open file in read mode
2.  Read entire file content
3.  Return complete text
4.  Automatically close file

### Delete Operation Flow

```python
def delete_content():
    with open(FILE_NAME, "w") as file:
        pass

```

**Process:**

1.  Open file in write mode (truncates file)
2.  Close file immediately
3.  File is now empty

### Program Flow (main.py)

```
1. Display menu title with beautify()
2. Show operation options (1, 2, 3, 0)
3. Match user choice:
   - Case 1: Get input → write to file
   - Case 2: Read and display file
   - Case 3: Delete all contents
   - Case 0: Exit program
4. Loop until user exits

```
## Project Structure

```
project/
├── main.py           # Main program with menu interface
├── fileEditor.py     # FileEditor class with file operations
├── utils/
│   └── utils.py      # Utility functions for formatting
├── file.txt          # File created automatically
└── README.md         # This file

```

## Key Concepts Demonstrated

### Static Methods

```python
@staticmethod
def write_file(string):
    with open(FILE_NAME, "a") as file:
        file.write(string + "\n")

```

-   No `self` parameter required
-   Callable without instance creation
-   Class.method() syntax
-   Shared across all instances
-   Useful for utility methods

### Context Managers (with statement)

```python
with open(FILE_NAME, "a") as file:
    file.write(string + "\n")

```

-   Automatically handles file closing
-   Exception-safe file operations
-   Prevents resource leaks
-   Cleaner than try-finally blocks
-   Proper cleanup guaranteed

### File Modes

```python
"a" - Append mode      # Add to existing content
"r" - Read mode        # Read file contents
"w" - Write mode       # Overwrite/clear file

```

-   Different modes for different operations
-   "a" preserves data, "w" deletes it
-   Understanding modes is critical

### String Concatenation and Newlines

```python
file.write(string + "\n")

```

-   Concatenates user input with newline
-   Each write() adds one line
-   Newline separates entries
-   Improves readability

### Menu-Driven Application Design

```python
while True:
    # Display menu
    choice = input("Enter Your Choice: ")
    match choice:
        case "1": # operation 1
        case "2": # operation 2
        # ... more cases

```

-   Infinite loop with exit condition
-   Match statement for clean code
-   User-driven control flow
-   Continuous operation

### Module Organization

```python
from utils import utils
from fileEditor import FileEditor

```

-   Separate concerns into modules
-   Utility functions in dedicated module
-   Class-based operations in separate file
-   Main logic in main.py

## Limitations

⚠️ **Important Limitations:**

1.  **File Must Exist Before Reading**
    
    -   FileEditor doesn't create file automatically for read operations
    -   First read will fail if file doesn't exist
    -   Need write/delete operation first
2.  **No Error Handling**
    
    -   No try-except blocks for file operations
    -   Program crashes if file permission denied
    -   Missing file on read causes unhandled exception
    -   Invalid input not validated
3.  **All Content Deleted at Once**
    
    -   No selective deletion (by line or pattern)
    -   Delete removes everything permanently
    -   No undo functionality
    -   No confirmation prompt
4.  **Single File Only**
    
    -   Hardcoded file name (file.txt)
    -   Cannot manage multiple files
    -   No file selection option
    -   Cannot rename or move files
5.  **No Data Validation**
    
    -   Accepts any input including empty strings
    -   No character encoding handling
    -   No maximum file size limits
    -   Unicode characters may cause issues
6.  **No Persistence Reset on Program Start**
    
    -   Data persists between sessions
    -   Delete operation needed to start fresh
    -   No backup mechanism
```

## Configuration

### Changing File Name

Modify the `FILE_NAME` constant in `fileEditor.py`:

```python
# Default
FILE_NAME = "file.txt"

# Custom file name
FILE_NAME = "mydata.txt"

# Different file path
FILE_NAME = "data/notes.txt"

# Different extension
FILE_NAME = "content.log"

```


## Potential Enhancements

1.  **Error Handling**
    
    -   Try-except blocks for file operations
    -   File existence checking before read
    -   Permission error handling
    -   User-friendly error messages
    -   Graceful failure recovery
2.  **Data Validation**
    
    -   Check for empty input
    -   Validate user choices
    -   Character encoding support
    -   Maximum file size limits
    -   Input sanitization
3.  **Advanced File Operations**
    
    -   View file line by line with numbers
    -   Delete specific lines (by number or content)
    -   Search/find text in file
    -   Replace text functionality
    -   Append vs overwrite mode selection
4.  **Multiple File Management**
    
    -   List available files
    -   Create/select different files
    -   Copy between files
    -   Rename files
    -   File permissions/metadata
5.  **User Experience Improvements**
    
    -   Confirmation prompts for delete
    -   Show file statistics (line count, size)
    -   Line numbers in read output
    -   Search and highlight results
    -   Display mode (preview vs full)
6.  **Data Organization**
    
    -   Save with timestamps
    -   Organize entries by date
    -   Tag or categorize entries
    -   Sort entries
    -   Filter by criteria
7.  **Backup and Recovery**
    
    -   Create automatic backups
    -   Undo/redo functionality
    -   Version history
    -   Restore deleted content
    -   File recovery options
8.  **File Format Support**
    
    -   JSON file support
    -   CSV export/import
    -   Markdown formatting
    -   Rich text support
    -   Different encoding options

## Code Quality Features

✅ Modular design with separate files  
✅ Utility functions properly organized  
✅ Context managers for safe file handling  
✅ Static methods for utility operations  
✅ Menu-driven user interface  
✅ Centralized configuration (FILE_NAME constant)  
✅ Clean code with clear variable names  
✅ Persistent data storage  
✅ Reusable FileEditor class  
✅ Modern Python syntax (match statement)  
✅ Formatted output with beautify utility  
✅ Easy to extend and modify  
✅ Demonstrates OOP principles  
✅ Simple and intuitive user flow  
✅ Practical real-world application