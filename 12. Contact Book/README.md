
# Contact Book

An interactive command-line contact management application that allows users to add, view, delete, update, and search contacts. The application features advanced phone number validation using regular expressions for Bangladesh phone numbers, persistent storage with file I/O, and a user-friendly menu-driven interface. This project demonstrates object-oriented programming, regular expressions, file handling, dictionary operations, and error handling in Python.

## Features

1.  **Add Contact**
    
    -   Input contact name and phone number
    -   Validate phone numbers using regex pattern
    -   Bangladesh phone number format support (+88)
    -   Prevent invalid phone numbers from being saved
    -   Auto-save to persistent storage
2.  **View All Contacts**
    
    -   Display complete contact list
    -   Formatted contact information
    -   Centered output with separators
    -   Shows name and phone for each contact
    -   Empty list handling
3.  **Search Contact**
    
    -   Find contact by name
    -   Display name and phone number
    -   Quick lookup functionality
    -   User-friendly not found messages
    -   Case-sensitive search
4.  **Delete Contact**
    
    -   Remove contact by name
    -   Update file to reflect deletion
    -   Confirmation message on success
    -   Handles missing contacts gracefully
    -   File synchronization
5.  **Update Contact**
    
    -   Modify existing contact information
    -   Change phone number with validation
    -   Preserves other contacts in file
    -   Confirmation message on update
    -   Data persistence
6.  **Phone Number Validation**
    
    -   Bangladesh phone format validation
    -   Regular expression pattern matching
    -   Supports +880-9 prefix format
    -   Validates 8 additional digits
    -   Rejects invalid formats
7.  **Persistent Storage**
    
    -   Automatic file creation on first run
    -   Data survives application restart
    -   CSV-like format storage
    -   Synchronization with dictionary
    -   File-based backup
8.  **Error Handling**
    
    -   Try-except blocks for operations
    -   ValueError for invalid phone numbers
    -   KeyError for missing contacts
    -   FileNotFoundError handling
    -   User-friendly error messages

## How It Works

### Contact Class Structure

```python
class Contact:
    def __init__(self, user_name="John Doe", user_phone="+8801234567890"):
        self._usr_name = user_name
        self._usr_phone = self._phone_validity(user_phone)
        self._save_on_file()
    
    @staticmethod
    def _phone_validity(user_phone):
        pattern = r"^\+8801?[3,4,5,6,7,8,9]{1}[\d]{8}$"
        if re.match(pattern, user_phone):
            return user_phone
        else:
            raise ValueError("Invalid Phone Number")
    
    def _save_on_file(self):
        with open(FILE_NAME, "a") as file:
            file.write(f"{self._usr_name},{self._usr_phone}\n")

```

**Key Components:**

-   **Constructor**: Initializes contact with name and validated phone
-   **_phone_validity() Method**: Validates Bangladesh phone format using regex
-   **Static Method**: Phone validation without instance creation
-   **_save_on_file() Method**: Persists valid contact to file
-   **Pattern Variable**: Regex pattern for phone validation

### Phone Number Validation Pattern

```regex
^\+8801?[3,4,5,6,7,8,9]{1}[\d]{8}$

```

**Pattern Breakdown:**

-   `^` — Start of string
-   `\+880` — Required prefix (+880)
-   `1?` — Optional "1" digit
-   `[3,4,5,6,7,8,9]{1}` — One digit from allowed providers
-   `[\d]{8}` — Exactly 8 more digits (0-9)
-   `$` — End of string

**Valid Examples:**

-   `+8801912345678` (14 digits with 1)

**Invalid Examples:**

-   `01912345678` (Missing +880)
-   `+88021234567` (Invalid provider digit 2)
-   `+880191234567` (Only 7 additional digits)

### Add Contact Flow

```python
def add_contact():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone Number: ")
    return name, phone

# In main.py
case "1":
    name, phone = func.add_contact()
    try:
        Contact(name, phone)  # Validates and saves
    except ValueError as e:
        print(e)  # Invalid phone message
    else:
        contacts[name] = phone  # Add to dictionary

```

**Process:**

1.  Get name and phone from user
2.  Create Contact instance
3.  Contact validates phone format
4.  If invalid, raises ValueError
5.  Exception caught and displayed
6.  If valid, contact saves to file
7.  Entry added to contacts dictionary

### Storage Format

```
John,+8801912345678
Alice,+8801987654321
Bob,+880965432109
```

**Format:**

-   Comma-separated values (CSV)
-   One contact per line
-   Name, Phone format
-   Simple and parseable

### File Operations Overview

```python
def store_from_file():
    contacts = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        with open(FILE_NAME, "w") as file:
            pass
    else:
        return contacts

```

**Process:**

1.  Try to open and read existing file
2.  Parse each line as name, phone pair
3.  Add to dictionary
4.  If file missing, create empty file
5.  Return populated dictionary

### Dictionary-Based Contact Management

```python
contacts = {
    "John": "+8801912345678",
    "Alice": "+8801987654321",
    "Bob": "+880965432109"
}

```

**Operations:**

-   Add: `contacts[name] = phone`
-   View: `contacts.items()`
-   Search: `contacts[name]`
-   Delete: `del contacts[name]`
-   Update: `contacts[name] = new_phone`

### Program Flow (main.py)

```
1. Load contacts from file
2. Display menu with beautify()
3. Get user choice (1-5, 0)
4. Match choice to operation:
   - Case 1: Add new contact with validation
   - Case 2: Display all contacts
   - Case 3: Delete by name
   - Case 4: Update contact
   - Case 5: Search by name
   - Case 0: Exit program
5. Loop until user chooses exit
6. Save operations sync with file

```

## Project Structure

```
project/
├── main.py              # Main program with menu interface
├── contact.py           # Contact class with validation
├── functionalities.py   # Utility functions for CRUD
├── contact.txt          # File created automatically
└── README.md            # This file

```

## Key Concepts Demonstrated

### Regular Expressions (Regex)

```python
import re

pattern = r"^\+8801?[3,4,5,6,7,8,9]{1}[\d]{8}$"
if re.match(pattern, user_phone):
    return user_phone
else:
    raise ValueError("Invalid Phone Number")

```

-   Pattern matching for complex validation
-   Re.match() for start-of-string matching
-   Character classes and quantifiers
-   Phone format validation
-   String validation without manual checks

### Static Methods

```python
@staticmethod
def _phone_validity(user_phone):
    pattern = r"^\+8801?[3,4,5,6,7,8,9]{1}[\d]{8}$"
    if re.match(pattern, user_phone):
        return user_phone
    else:
        raise ValueError("Invalid Phone Number")

```

-   Methods that don't access instance data
-   Callable without instance creation
-   Utility method organization
-   Logical grouping of related functions
-   Memory efficient

### Dictionary Operations

```python
contacts = {}
contacts[name] = phone           # Add/Update
del contacts[name]               # Delete
phone = contacts[name]           # Access
for name, phone in contacts.items():  # Iterate

```

-   Key-value pair storage
-   Fast lookup by name
-   Flexible dynamic storage
-   In-memory data structure
-   Easy iteration

### Exception Handling with Try-Except-Else

```python
try:
    Contact(name, phone)
except ValueError as e:
    print(e)
else:
    contacts[name] = phone

```

-   Try block for risky operations
-   Except for specific exception handling
-   Else for success path execution
-   Exception message display
-   Graceful error recovery

### Custom Exception Raising

```python
if not re.match(pattern, user_phone):
    raise ValueError("Invalid Phone Number")

```

-   User-defined exception raising
-   Input validation enforcement
-   Custom error messages
-   Application-level checks
-   Clear error communication

### File I/O with Synchronization

```python
# Read from file to dictionary
with open(FILE_NAME, "r") as file:
    for line in file:
        name, phone = line.strip().split(",")
        contacts[name] = phone

# Write back to file
with open(FILE_NAME, "w") as file:
    for line in lines:
        if name not in line:
            file.write(line)

```

-   File-dictionary synchronization
-   Read-modify-write pattern
-   CSV parsing and generation
-   Data persistence
-   File corruption prevention

### String Formatting and Centering

```python
print(f"Name: {name}".center(40))
print(f"Phone: {phone}".center(40))

```

-   F-strings for interpolation
-   .center() for alignment
-   Formatted output
-   Visual organization
-   Readable display

### Menu-Driven Application with Match

```python
match choice:
    case "1": func.add_contact()
    case "2": func.show_contact(contacts)
    case "5": func.search_contact(contacts)
    case "0": exit()
    case _: print("Invalid Choice")

```

-   Pattern matching for clean code
-   Multiple operation handling
-   User-driven control flow
-   Default case handling
-   Easy menu management

## Limitations

⚠️ **Important Limitations:**

1.  **Bangladesh-Only Phone Format**
    
    -   Only validates Bangladesh (+880) numbers
    -   Cannot add international numbers
    -   No support for other countries
    -   Hardcoded pattern for specific format
2.  **Case-Sensitive Search**
    
    -   Search only works with exact name match
    -   "John" and "john" are different
    -   Cannot search by partial name
    -   Not user-friendly for inconsistent naming
3.  **No Duplicate Name Prevention**
    
    -   Same name can be added multiple times
    -   Latest entry overwrites previous
    -   No warning for duplicates
    -   Leads to data loss
4.  **No Data Validation for Names**
    
    -   Accepts empty names
    -   Accepts numeric-only names
    -   No length limits
    -   Special characters allowed
5.  **File Synchronization Issues**
    
    -   Delete and update read entire file
    -   Performance issues with large contacts
    -   Potential data corruption
    -   Not atomic operations
6.  **No Backup or Recovery**
    
    -   File corruption loses all data
    -   Delete operation is permanent
    -   No version history
    -   No undo functionality
7.  **Limited Search Capabilities**
    
    -   Cannot search by phone number
    -   Cannot filter contacts
    -   Cannot sort contacts
    -   Only exact name match
8.  **Memory-Efficiency Issues**
    
    -   All contacts loaded in memory
    -   Inefficient with thousands of contacts
    -   No pagination or lazy loading
    -   Single file with entire dataset

### Example of Limitations

```python
# Limitation 1: Only Bangladesh format
Contact("John", "+11234567890")  # International - Invalid
Contact("John", "+441234567890")  # UK - Invalid

# Limitation 2: Case-sensitive search
contacts = {"John Smith": "+8801912345678"}
search_contact(contacts)  # Search for "john smith" - Not Found

# Limitation 3: Duplicate names
contacts["John"] = "+8801111111111"  # First entry
contacts["John"] = "+8801222222222"  # Overwrites first
# First number is lost

# Limitation 4: No name validation
Contact("", "+8801912345678")  # Empty name accepted
Contact("12345", "+8801912345678")  # Numeric name accepted

# Limitation 5: File sync inefficiency
# Delete operation:
# 1. Read entire file
# 2. Write back all lines except deleted
# Slow with large files

# Limitation 6: No recovery
delete_contact(contacts)  # Permanently removes contact
# Cannot undo or recover

# Limitation 7: Limited search
# Can only find by exact name
# Cannot search by phone

# Limitation 8: Memory loaded
# 10,000 contacts = memory usage
# No lazy loading or pagination

```

## Potential Enhancements

1.  **Flexible Phone Validation**
    
    -   Support multiple countries
    -   International format support
    -   Custom validation patterns
    -   Variable format acceptance
    -   Phone type detection (mobile, landline)
2.  **Enhanced Search**
    
    -   Case-insensitive search
    -   Partial name matching
    -   Search by phone number
    -   Filter by first letter
    -   Advanced query syntax
3.  **Duplicate Prevention**
    
    -   Check for existing contacts
    -   Warn before overwriting
    -   Merge duplicate entries
    -   Unique name enforcement
    -   Conflict resolution
4.  **Data Validation**
    
    -   Validate names (non-empty, no numbers)
    -   Maximum name length
    -   Phone number formatting
    -   Trim whitespace
    -   Sanitize special characters
5.  **Database Integration**
    
    -   Use SQLite instead of text file
    -   Atomic transactions
    -   Better performance
    -   Scalability
    -   Indexed searches
6.  **Export/Import**
    
    -   Export to CSV
    -   Export to JSON
    -   Import from file
    -   Backup functionality
    -   Data portability
7.  **Advanced Features**
    
    -   Contact groups/categories
    -   Email address storage
    -   Address information
    -   Notes and reminders
    -   Call history
8.  **User Experience**
    
    -   GUI interface
    -   Contact photos
    -   Favorite contacts
    -   Recent contacts
    -   Auto-complete names
9.  **Data Management**
    
    -   Sort by name or phone
    -   Pagination for large lists
    -   Statistics (total contacts)
    -   Bulk operations
    -   Contact deduplication
10. **Security**
    -   Password protection
    -   Data encryption
    -   Backup encryption
    -   Access control
    -   Audit logging

## Code Quality Features

✅ Regular expression validation  
✅ Custom exception raising with messages  
✅ Static methods for utility functions  
✅ Try-except-else error handling  
✅ Dictionary-based data storage  
✅ File I/O with context managers  
✅ CSV format for easy parsing  
✅ Menu-driven user interface  
✅ Modular function organization  
✅ Persistent data storage  
✅ Input validation at entry point  
✅ Formatted output with centering  
✅ Clear separation of concerns  
✅ Descriptive variable naming  
✅ User-friendly error messages  
✅ Reusable utility functions  
✅ Object-oriented design  
✅ Modern Python syntax (match statement)