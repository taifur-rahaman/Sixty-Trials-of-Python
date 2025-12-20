
# Grade Calculator

An interactive command-line application for managing student records and calculating grade statistics. The program allows users to add students with multiple subject scores and automatically computes highest score, lowest score, and average score for each student. This project demonstrates object-oriented programming, file I/O, data validation, and UUID generation in Python.

## Features

1.  **Add Student**
    
    -   Input student name interactively
    -   Enter multiple subject scores per student
    -   Automatic unique student ID generation using UUID
    -   Input validation for score ranges (0-100)
    -   Prevents negative and invalid scores
    -   Persistent storage to file
2.  **Score Management**
    
    -   Add multiple subjects per student
    -   Validate scores are between 0 and 100
    -   Calculate highest score automatically
    -   Calculate lowest score automatically
    -   Calculate average score automatically
3.  **Unique Student Identification**
    
    -   UUID (Universally Unique Identifier) generation
    -   Guaranteed unique ID for each student
    -   Prevents duplicate student conflicts
    -   Permanent ID assignment
4.  **View Students**
    
    -   Display all stored student records
    -   Show formatted student information
    -   Display calculated statistics
    -   Show student count and numbering
    -   Formatted output with beautified headers
5.  **Data Persistence**
    
    -   Automatic file saving after student creation
    -   CSV-like format for data storage
    -   Retrieval and display from persistent storage
    -   Data survives application restart
6.  **Score Validation**
    
    -   Rejects negative scores
    -   Rejects scores over 100
    -   Provides feedback on invalid input
    -   Prevents invalid data entry
    -   Continuous input until valid score entered
7.  **Statistics Calculation**
    
    -   Automatic maximum score calculation
    -   Automatic minimum score calculation
    -   Automatic average score calculation
    -   Real-time computation
    -   Comprehensive grade analysis
8.  **Interactive Menu System**
    
    -   User-friendly command-line interface
    -   Clear operation options
    -   Menu-driven continuous operation
    -   Graceful exit functionality

## How It Works

### Student Class Structure

```python
class Student:
    def __init__(self, student_name="John Doe"):
        self._student_name = student_name
        self._student_id_generator()
        self.std_scores = []
        self.scores()
        self.save_to_file()
    
    def _student_id_generator(self):
        self._student_id = str(uuid.uuid4())
    
    def scores(self):
        # Input and validate scores
    
    def __str__(self):
        # Display student information
    
    def save_to_file(self):
        # Save to persistent storage

```

**Key Components:**

-   **Constructor**: Initializes student with name, generates ID, collects scores
-   **_student_id_generator()**: Creates unique identifier using UUID
-   **std_scores List**: Stores all subject scores for calculations
-   **scores() Method**: Interactive input with validation
-   ****str**() Method**: Custom string representation with statistics
-   **save_to_file() Method**: Persists data to file in CSV format

### Student Creation Flow

```
1. User selects "Add Student"
2. Input student name
3. Create Student instance
4. Generate unique UUID
5. Initialize empty scores list
6. Prompt for number of subjects
7. For each subject:
   - Input score
   - Validate (0-100 range)
   - Add to scores list
8. Calculate statistics
9. Save to file

```

### Score Validation Logic

```python
def scores(self):
    sub_qty = input(f"Student: {self._student_name}, "
                    "\nEnter How many subjects scores you want to enter: ")
    for i in range(int(sub_qty)):
        score = float(input("Enter score: "))
        if score < 0:
            print("Score cannot be negative")
            continue
        elif score > 100:
            print("Score cannot be greater than 100")
            continue
        self.std_scores.append(score)

```

**Validation Process:**

1.  Prompt for number of subjects
2.  Loop for each subject
3.  Check if score is negative (< 0)
4.  Check if score exceeds maximum (> 100)
5.  Continue if invalid (skip invalid entry)
6.  Append if valid (add to scores)

### Statistics Calculation

```python
max(self.std_scores)                                    # Highest score
min(self.std_scores)                                    # Lowest score
sum(self.std_scores) / len(self.std_scores)             # Average score

```

**Calculations:**

-   **Highest**: Maximum value in scores list
-   **Lowest**: Minimum value in scores list
-   **Average**: Sum divided by count

### File Storage Format

```
Name, UUID, HighestScore, LowestScore, AverageScore
Alice Johnson, 550e8400-e29b-41d4-a716-446655440000, 95, 78, 87.5
Bob Smith, 6ba7b810-9dad-11d1-80b4-00c04fd430c8, 92, 65, 79.3

```

**CSV Format:**

-   Comma-separated values
-   One student per line
-   Fields: Name, ID, Highest, Lowest, Average
-   Easily readable and parseable

### Display Operation Flow

```python
def display_students():
    count = 0
    with open("students.txt", "r") as file:
        students = file.readlines()
    if not students:
        print("No Students Found")
        return
    for student in students:
        student = student.strip()
        count += 1
        student = student.split(", ")
        beautify(f"Student : {count}")
        print(formatted_student_info)

```

**Process:**

1.  Read all lines from file
2.  Check if file is empty
3.  For each student line:
    -   Strip whitespace
    -   Split by comma delimiter
    -   Display with formatting
    -   Increment counter

### Program Flow (main.py)

```
1. Display menu with beautify()
2. Show operation options (1, 2, 0)
3. Match user choice:
   - Case 1: Call add_student()
   - Case 2: Call display_students()
   - Case 0: Exit program
4. Loop until user chooses exit

```

## Project Structure

```
project/
├── main.py          # Main program with menu interface
├── students.py      # Student class with UUID and calculations
├── utils.py         # Utility functions (beautify, add, display)
├── students.txt     # File created automatically
└── README.md        # This file

```

## Key Concepts Demonstrated

### Object-Oriented Programming

```python
class Student:
    def __init__(self, student_name="John Doe"):
        self._student_name = student_name
        self._student_id_generator()

```

-   Class-based student representation
-   Encapsulation of student data
-   Constructor initialization
-   Method organization
-   Instance and private variables

### UUID Generation

```python
import uuid

def _student_id_generator(self):
    self._student_id = str(uuid.uuid4())

```

-   Universally unique identifier
-   Guarantees uniqueness across all systems
-   128-bit random identifier
-   String conversion for storage
-   Prevents ID conflicts

### List Operations and Statistics

```python
self.std_scores = []
self.std_scores.append(score)
max(self.std_scores)
min(self.std_scores)
sum(self.std_scores) / len(self.std_scores)

```

-   Dynamic list creation
-   Append for adding elements
-   Built-in functions for statistics
-   Mathematical calculations
-   List comprehension ready

### File I/O with Append Mode

```python
def save_to_file(self):
    with open(FILE_NAME, "a") as file:
        file.write(f"{self._student_name}, {self._student_id}...")

```

-   Append mode adds without overwriting
-   Context manager for safe handling
-   CSV-like data format
-   Persistent storage
-   Multiple entries support

### String Formatting and Custom **str**()

```python
def __str__(self):
    return (f"Student Name: {self._student_name},"
            f"\nStudent ID: {self._student_id},"
            f"\nHighest Score : {max(self.std_scores)}")

```

-   Custom string representation
-   F-strings for formatting
-   Automatic calculation display
-   Print-friendly output
-   Readable information presentation

### String Parsing and File Reading

```python
students = file.readlines()
student = student.strip()
student = student.split(", ")

```

-   readlines() for multiple lines
-   strip() to remove whitespace
-   split() to parse CSV data
-   Delimiter-based parsing
-   Data extraction

### Input Validation with Loops

```python
for i in range(int(sub_qty)):
    score = float(input("Enter score: "))
    if score < 0:
        continue
    elif score > 100:
        continue
    self.std_scores.append(score)

```

-   Loop-based input collection
-   Conditional validation
-   Continue statement to skip invalid
-   Range-based iteration
-   Type conversion

### Menu-Driven Application

```python
while True:
    match choice:
        case "1": utils.add_student()
        case "2": utils.display_students()
        case "0": exit()

```

-   Infinite loop with exit condition
-   Match statement for clean branching
-   Function-based operations
-   User-driven flow
-   Reusable utilities

## Potential Enhancements

1.  **Robust Error Handling**
    
    -   Try-except blocks in main menu
    -   File existence checking
    -   Graceful error recovery
    -   User-friendly error messages
    -   Input type validation
2.  **Student Data Management**
    
    -   Search/filter by name
    -   Search/filter by ID
    -   Update student scores
    -   Delete student records
    -   View specific student
3.  **Enhanced Score Management**
    
    -   Retry invalid score entry
    -   Show score entry confirmation
    -   Edit individual scores
    -   Score history tracking
    -   Subject-based score organization
4.  **Input Validation**
    
    -   Validate student names
    -   Check for duplicate names
    -   Limit name length
    -   Validate score quantity input
    -   Numeric input verification
5.  **Data Organization**
    
    -   Multiple classes/sections
    -   Filter by class
    -   Sort students by average
    -   Grade assignment (A, B, C, etc.)
    -   Student ranking
6.  **Statistics and Reporting**
    
    -   Class average calculation
    -   Highest/lowest student
    -   Grade distribution
    -   Performance reports
    -   Export to PDF/Excel
7.  **Backup and Recovery**
    
    -   Automatic backups
    -   Version history
    -   Data recovery options
    -   Restore previous state
    -   Archive old records
8.  **User Interface Improvements**
    
    -   Database instead of text file
    -   GUI interface
    -   Color-coded output
    -   Better formatting
    -   User authentication

## Code Quality Features

✅ UUID-based unique identification  
✅ Input validation for score ranges  
✅ Custom **str**() for readable output  
✅ File I/O with context managers  
✅ CSV-like data storage format  
✅ Automatic statistics calculation  
✅ Menu-driven user interface  
✅ Modular function organization  
✅ Persistent data storage  
✅ Object-oriented design  
✅ String formatting with f-strings  
✅ Reusable utility functions  
✅ Clear variable naming  
✅ Separated concerns (class, utils, main)  
✅ Practical real-world application  
✅ Educational code structure  
✅ Easy to extend and modify