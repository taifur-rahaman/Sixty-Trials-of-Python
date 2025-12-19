# Reverse Words

An interactive Python application that reverses strings in multiple ways. The program offers a menu-driven interface to reverse words or letters within a given string with proper text formatting.

## Features

1. **Interactive Menu System**
   - User-friendly command-line interface
   - Multiple operation options per session
   - Easy navigation between main menu and operations
   - Exit functionality with graceful shutdown

2. **Word Reversal**
   - Reverses the order of words in a string
   - Preserves individual word integrity
   - Example: "hello world python" becomes "python world hello"

3. **Letter Reversal**
   - Reverses the sequence of all characters in a string
   - Maintains spacing and special characters
   - Example: "hello" becomes "olleh"

4. **Case-Insensitive Input**
   - Converts input to lowercase for consistent processing
   - Automatically formats output to title case
   - Prevents case-related inconsistencies

5. **String Processing**
   - Handles multiple strings in a single session
   - Clean input/output formatting
   - Descriptive prompts and error messages

6. **Object-Oriented Design**
   - Encapsulated string operations in reusable class
   - Modular approach for code organization
   - Easy to extend with additional methods

## How It Works

### Reverse Class Structure

```python
class Reverse:
    def __init__(self):
        pass
    
    def reverse_words(self, string):
        return " ".join(reversed(string.split()))
    
    def reverse_letters(self, string):
        return "".join(reversed(string))
```

**Key Components:**
- **Constructor**: Initializes the Reverse object
- **reverse_words() Method**: Takes a string and reverses word order while preserving words
- **reverse_letters() Method**: Takes a string and reverses all characters sequentially
- **reversed() Function**: Built-in Python function that creates a reverse iterator

### Word Reversal Logic

```python
string.split()           # Split string into list of words
reversed(...)            # Reverse the list of words
" ".join(...)            # Join reversed words with spaces
```

**Process Flow:**
1. Input: `"hello world python"`
2. Split into words: `["hello", "world", "python"]`
3. Reverse list: `["python", "world", "hello"]`
4. Join with spaces: `"python world hello"`
5. Format to title case: `"Python World Hello"`

### Letter Reversal Logic

```python
reversed(string)         # Create reverse iterator of characters
"".join(...)             # Join all reversed characters
```

**Process Flow:**
1. Input: `"hello world"`
2. Reverse all characters: `dlrow olleh`
3. Format to title case: `Dlrow Olleh`

### Program Flow (main.py)

```
1. Display banner/title
2. Main menu loop:
   - Option 1: Get string input
   - Option 0: Exit program
3. Operations menu loop:
   - Option 1: Reverse words
   - Option 2: Reverse letters
   - Option 0: Return to main menu
```

## Project Structure

```
project/
├── main.py       # Main program with menu-driven interface
├── reverse.py    # Reverse class definition
└── README.md     # This file
```

## Key Concepts Demonstrated

### String Split and Join Operations
```python
string.split()           # Splits by whitespace, returns list
" ".join(reversed_list)  # Joins list elements with spaces
```
- `split()` separates string into tokens
- `join()` combines iterable elements into single string
- Foundation of word manipulation

### reversed() Built-in Function
```python
reversed(string)         # Creates reverse iterator
reversed(string.split()) # Reverses order of words
```
- Returns iterator (not list) for memory efficiency
- Works with any iterable (strings, lists, tuples)
- Lazy evaluation - doesn't create intermediate list

### String Methods: casefold() and title()
```python
input_string.casefold()  # Converts to lowercase (Unicode-aware)
output_string.title()    # Capitalizes first letter of each word
```
- `casefold()` more aggressive than `lower()`
- `title()` useful for proper formatting
- Standardizes input/output appearance

### Match Statement (Python 3.10+)
```python
match choice:
    case "1":
        # Execute code
    case "0":
        break
    case _:
        # Default case
```
- Structural pattern matching
- Cleaner than multiple if-elif statements
- Requires Python 3.10 or higher

### Menu-Driven Program Structure
```
while True:
    # Main menu
    while True:
        # Operations menu
```
- Nested loops for multi-level menus
- `break` statement to exit inner loop
- `exit()` to terminate program

### Object-Oriented Programming
```python
reverse = Reverse()
reverse.reverse_words(string)
```
- Encapsulation of related methods
- Reusable across multiple sessions
- Modular code organization


## Potential Enhancements

1. **Punctuation Handling**
   - Separate punctuation from words before reversal
   - Reattach punctuation to correct positions
   - Process punctuation separately from letters

2. **Input Validation**
   - Check for empty or whitespace-only strings
   - Validate menu choices with error handling
   - Set string length limits
   - Warn users about potential output readability

3. **Additional Operations**
   - Palindrome checker (is string same reversed?)
   - Word frequency counter
   - Character frequency analyzer
   - Anagram generator

4. **Advanced String Processing**
   - Reverse each word individually (keep word order)
   - Reverse sentences (keep word order, reverse sentences)
   - Selective reversal (reverse only vowels/consonants)
   - Reverse with custom delimiters

5. **Output Options**
   - Save results to file
   - Copy results to clipboard
   - Display statistics (character count, word count)
   - Show before/after comparison

6. **User Experience Improvements**
   - Input history/previous strings
   - Batch processing multiple strings
   - Save favorite operations
   - Undo/redo functionality
   - Case preservation options

7. **Performance Features**
   - Time complexity display
   - Benchmark different algorithms
   - Large string handling optimization
   - Unicode handling improvements

## Code Quality Features

✅ Menu-driven user interface  
✅ Clean separation of concerns (class vs main logic)  
✅ Reusable Reverse class  
✅ Clear variable naming conventions  
✅ Proper use of Python built-in functions  
✅ Efficient string manipulation with join/split  
✅ Graceful program exit handling  
✅ Input formatting with casefold() and title()  
✅ User-friendly prompts and messages  
✅ Modern Python syntax (match statement)  
✅ Modular program structure  
✅ Easy to extend with new operations