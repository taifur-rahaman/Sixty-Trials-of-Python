# Shopping List Manager

A Python program that manages a persistent shopping list with add, remove, and view functionality. Items are stored in a text file (`list.txt`) for persistence across sessions, with case-insensitive storage and title-case display.

## Features

1. **Persistent Storage**
   - Items saved to `list.txt` file.
   - Data persists between program runs.
   - Automatic file creation if not found.

2. **Add Items**
   - Add items to shopping list one at a time.
   - Items stored in lowercase for consistency.
   - Immediate file write for data safety.

3. **Remove Items**
   - Delete specific items from the list.
   - Case-insensitive item matching.
   - Prevents deletion of non-existent items.

4. **View List**
   - Display all items in the shopping list.
   - Items shown in Title Case for readability.
   - Clean, bulleted list format.

5. **Case Normalization**
   - Input converted to lowercase for storage.
   - Display formatted in Title Case.
   - Case-insensitive item searching.

6. **Menu-Driven Interface**
   - Clear, numbered menu options.
   - Visual separators for better UX.
   - Input validation with error messages.

## How It Works

### File Structure

**list.txt format:**
```
milk
bread
eggs
cheese
```
- One item per line
- Stored in lowercase
- No special formatting

### Program Flow

```
Start Program
    ↓
Load list.txt (or create if missing)
    ↓
Display Menu
    ↓
User Choice → [Add | Remove | View | Exit]
    ↓
Perform Action → Update list.txt
    ↓
Loop back to Menu
```

### Core Functions

**File Operations:**
```python
def file_add(item):
    # Append item to file
    with open("list.txt", "a") as file:
        file.write(f"{item}\n")

def file_read():
    # Read all items from file
    with open("list.txt", "r") as file:
        return file.read().splitlines()

def file_delete_item():
    # Remove specific item from file
    # Reads all items, removes target, rewrites file
```

**User Interface Functions:**
```python
def add_item():
    # Get input, save to file, return item
    item = input("Enter the name of the item to add: ")
    file_add(item.casefold())
    return item

def display():
    # Read items and display in Title Case
    items = file_read()
    for item in items:
        print(f"- {item.title()}")
```

### Case Handling Strategy

**Storage (lowercase):**
```python
item.casefold()  # "MILK" → "milk"
```

**Display (Title Case):**
```python
item.title()  # "milk" → "Milk"
```

**Searching (lowercase):**
```python
item.casefold()  # "MiLk" → "milk"
```

### File Initialization

```python
try:
    with open("list.txt", "r") as file:
        # Load existing items
except FileNotFoundError:
    with open("list.txt", "w"):
        pass  # Create empty file
```

### Menu Options

```
========================================
SHOPPING LIST
========================================
1. Add Item
2. Remove Item
3. View List
0. Exit
========================================
```

## Project Structure

```
project/
├── main.py              # Main program with menu interface
├── list_manager.py      # Shopping list management functions
└── list.txt             # Persistent storage (auto-created)
```

## Key Concepts Demonstrated

### File I/O Operations

**Append Mode (a):**
```python
with open("list.txt", "a") as file:
    file.write(f"{item}\n")
```
- Adds to end of file without overwriting
- Creates file if doesn't exist

**Read Mode (r):**
```python
with open("list.txt", "r") as file:
    return file.read().splitlines()
```
- Reads file content
- `.splitlines()` removes newline characters

**Write Mode (w):**
```python
with open("list.txt", "w") as file:
    for item in items:
        file.write(item)
```
- Overwrites entire file
- Used for deletion operations

### Context Managers (with statement)
```python
with open("list.txt", "r") as file:
    data = file.read()
# File automatically closed here
```
- Ensures file is properly closed
- Exception-safe file handling
- Best practice for file operations

### Case Normalization

**casefold() vs lower():**
```python
"MILK".lower()      # "milk"
"MILK".casefold()   # "milk"
"ß".lower()         # "ß"
"ß".casefold()      # "ss"  (more aggressive)
```
- `.casefold()` better for case-insensitive comparisons
- Handles international characters better

**title() for Display:**
```python
"milk and eggs".title()  # "Milk And Eggs"
```
- Capitalizes first letter of each word
- Good for user-facing display

### Exception Handling Pattern
```python
try:
    # Attempt file operation
except FileNotFoundError:
    # Create file if missing
```

### List Manipulation
```python
items.remove(item)  # Remove first occurrence
items.append(item)  # Add to end
```

## Data Flow

### Adding an Item
```
User Input: "MILK"
    ↓
casefold(): "milk"
    ↓
Append to list.txt: "milk\n"
    ↓
Confirm to user: "MILK has been successfully added"
```

### Displaying Items
```
Read list.txt: ["milk", "bread", "eggs"]
    ↓
Apply title(): ["Milk", "Bread", "Eggs"]
    ↓
Print with bullets: "- Milk"
```

### Removing an Item
```
Read all items from list.txt
    ↓
User input: "MILK"
    ↓
casefold(): "milk"
    ↓
Find in list: "milk\n"
    ↓
Remove from list
    ↓
Rewrite entire file without removed item
```

## Notes

- **No External Libraries Required** - Uses only Python standard library features.
- Items stored one per line in `list.txt`.
- Duplicate items are allowed (each stored separately).
- Case-insensitive matching prevents "Milk" and "milk" being treated as different.
- File is created automatically in the same directory as the script.
- Deletion rewrites entire file (not efficient for very large lists).
- No quantity tracking (items are present or absent only).

## Limitations

### Current Implementation

1. **No Quantity Tracking**
   - Can't specify "2 milk" or "3 eggs"
   - Each item is simply present or absent

2. **Duplicate Items**
   - Can add "milk" multiple times
   - Deletion only removes first occurrence

3. **No Categories**
   - All items in one flat list
   - No organization by aisle or type

4. **File Rewrite for Deletion**
   - Rewrites entire file when removing one item
   - Inefficient for large lists (hundreds of items)

5. **No Undo Functionality**
   - Changes are immediate and permanent
   - No way to recover accidentally deleted items

6. **Basic Error Handling**
   - ValueError raised but not caught in main.py
   - Could cause program crash on invalid deletion

## Real-World Applications

This type of program is the foundation for:
- Shopping list mobile apps
- Todo list applications
- Inventory management systems
- Recipe ingredient trackers
- Packing list generators
- Grocery delivery platforms
- Meal planning tools