
# Word Frequency Counter

A Python program that analyzes text strings to count the frequency of each word. The application uses dictionary data structures to track word occurrences and displays the frequency count for each unique word in the input text. This project demonstrates dictionary operations, string manipulation, tuple conversion, and static method implementation in Python.

## Features

1.  **Word Frequency Analysis**
    
    -   Counts occurrences of each word in text
    -   Tracks frequency for all unique words
    -   Handles multiple word occurrences
    -   Dictionary-based counting
    -   Automatic frequency calculation
2.  **String Processing**
    
    -   Splits text into individual words
    -   Whitespace-based word separation
    -   Handles multiple spaces correctly
    -   Converts to tuple for processing
    -   Preserves word order for counting
3.  **Dictionary Output**
    
    -   Returns word-frequency pairs
    -   Key: word, Value: count
    -   Easy-to-read format
    -   Complete frequency mapping
    -   Direct dictionary display
4.  **Static Method Design**
    
    -   No instance creation required
    -   Class-based organization
    -   Callable without instantiation
    -   Utility function pattern
    -   Memory efficient
5.  **Simple Interface**
    
    -   Single method call for analysis
    -   String input parameter
    -   Automatic processing
    -   Immediate results
    -   No complex setup

## How It Works

### Count Class Structure

```python
class Count:
    def __init__(self):
        pass
    
    @staticmethod
    def count_words(string):
        count_dict = {}
        temp_string = tuple(string.split())
        for word in temp_string:
            count_dict[word] = temp_string.count(word)
        print(count_dict)

```

**Key Components:**

-   **Count Class**: Container for word counting functionality
-   **Empty Constructor**: No initialization needed
-   **count_words() Method**: Static method for frequency counting
-   **count_dict**: Dictionary to store word-frequency pairs
-   **temp_string**: Tuple conversion of split words
-   **Automatic Display**: Prints dictionary directly

### Word Frequency Algorithm

```python
@staticmethod
def count_words(string):
    count_dict = {}
    temp_string = tuple(string.split())
    for word in temp_string:
        count_dict[word] = temp_string.count(word)
    print(count_dict)

```

**Process:**

1.  Initialize empty dictionary
2.  Split string by whitespace
3.  Convert word list to tuple
4.  For each word in tuple:
    -   Count occurrences in tuple
    -   Store word as key, count as value
5.  Print resulting dictionary

**Example:**

```
Input: "Hello World How are you? Are you here?"
Split: ["Hello", "World", "How", "are", "you?", "Are", "you", "here?"]
Tuple: ("Hello", "World", "How", "are", "you?", "Are", "you", "here?")

Counting:
- "Hello" appears 1 time
- "World" appears 1 time
- "How" appears 1 time
- "are" appears 1 time
- "you?" appears 1 time
- "Are" appears 1 time
- "you" appears 1 time
- "here?" appears 1 time

Output: {'Hello': 1, 'World': 1, 'How': 1, 'are': 1, 'you?': 1, 'Are': 1, 'you': 1, 'here?': 1}

```

### String Splitting Process

```python
string.split()

```

**How it works:**

-   Splits by any whitespace (spaces, tabs, newlines)
-   Removes empty strings automatically
-   Returns list of words
-   Handles multiple consecutive spaces
-   Default behavior without arguments

**Examples:**

```python
"Hello World".split()           # ["Hello", "World"]
"  Hello   World  ".split()     # ["Hello", "World"]
"Hello\nWorld\tTest".split()    # ["Hello", "World", "Test"]

```

### Tuple Conversion

```python
temp_string = tuple(string.split())

```

**Why use tuple?**

-   Immutable sequence for counting
-   Prevents accidental modification
-   Works with .count() method
-   Memory efficient for read-only data
-   Clear intent of no modification

### Dictionary Building Loop

```python
for word in temp_string:
    count_dict[word] = temp_string.count(word)

```

**Process:**

1.  Iterate through each word in tuple
2.  Use tuple.count() to count occurrences
3.  Assign count to dictionary with word as key
4.  Overwrites if word already exists (same count anyway)
5.  Builds complete frequency map

**Note:** If word appears multiple times, dictionary entry is overwritten with same count value (no issue since count is same).

### Usage Example

```python
# Direct usage
Count.count_words("Hello World, How are you? Are you here to capture me? Are you insane?")

# Output:
# {'Hello': 1, 'World,': 1, 'How': 1, 'are': 1, 'you?': 3, 'Are': 2, 'you': 1, 'here': 1, 'to': 1, 'capture': 1, 'me?': 1, 'insane?': 1}

```

## Project Structure

```
project/
├── counter.py           # Count class with frequency logic
└── main.py              # Main program (currently empty)

```

## Key Concepts Demonstrated

### Dictionary Data Structure

```python
count_dict = {}
count_dict[word] = temp_string.count(word)

```

-   Key-value pair storage
-   Word as key, frequency as value
-   Dynamic dictionary building
-   Fast lookup and insertion
-   Automatic key uniqueness
-   Mutable mapping type

### Static Methods

```python
@staticmethod
def count_words(string):
    count_dict = {}
    # ...

```

-   Methods callable without instance
-   No access to instance data
-   Class-based organization
-   Utility function pattern
-   No self parameter needed
-   Memory efficient

### String Manipulation

```python
string.split()           # Split by whitespace
tuple(list)              # Convert list to tuple
temp_string.count(word)  # Count occurrences

```

-   split() for word extraction
-   Whitespace-based tokenization
-   Type conversion between collections
-   Built-in counting methods
-   String processing techniques

### Tuple Operations

```python
temp_string = tuple(string.split())
for word in temp_string:
    count = temp_string.count(word)

```

-   Immutable sequence type
-   Iteration support
-   count() method for frequency
-   Type conversion from list
-   Read-only data structure

### List Comprehension Alternative

```python
# Current approach
for word in temp_string:
    count_dict[word] = temp_string.count(word)

# Alternative (more Pythonic)
count_dict = {word: temp_string.count(word) for word in temp_string}

```

-   Dictionary comprehension
-   Single-line dictionary creation
-   Same functionality, cleaner syntax
-   More Pythonic approach

### Built-in count() Method

```python
temp_string.count(word)

```

-   Counts occurrences in sequence
-   Works on lists, tuples, strings
-   Returns integer count
-   Linear time complexity O(n)
-   Simple and readable

## Limitations

⚠️ **Important Limitations:**

1.  **Case-Sensitive Counting**
    
    -   "Hello" and "hello" counted separately
    -   "Are" and "are" treated as different words
    -   Not user-friendly for natural text
    -   Inflates unique word count
    -   Misleading frequency results
2.  **Punctuation Not Handled**
    
    -   "you?" and "you" counted separately
    -   "World," and "World" are different
    -   Punctuation attached to words
    -   No text normalization
    -   Inaccurate word counting
3.  **Inefficient Algorithm**
    
    -   Uses count() in loop: O(n²) complexity
    -   Counts same word multiple times
    -   Redundant counting operations
    -   Slow for large texts
    -   Better algorithms available
4.  **No Return Value**
    
    -   Only prints dictionary
    -   Cannot use result in code
    -   Not reusable
    -   No programmatic access
    -   Limited functionality
5.  **No Input Validation**
    
    -   Accepts empty strings
    -   No error handling
    -   Assumes valid string input
    -   May fail with None
    -   No type checking
6.  **Limited Output Format**
    
    -   Only dictionary print
    -   No sorted output
    -   No formatted display
    -   Not user-friendly
    -   Raw dictionary format
7.  **No Filtering Options**
    
    -   Cannot exclude common words (the, a, an)
    -   No minimum frequency filter
    -   Cannot filter by word length
    -   No stop word removal
    -   Includes all words
8.  **Main.py Empty**
    
    -   No user interface
    -   No interactive mode
    -   Only test code in counter.py
    -   No menu system
    -   Limited usability

### Example of Limitations

```python
# Limitation 1: Case sensitivity
Count.count_words("Hello hello HELLO")
# Output: {'Hello': 1, 'hello': 1, 'HELLO': 1}
# Should be: {'hello': 3} (if case-insensitive)

# Limitation 2: Punctuation
Count.count_words("Hello, hello. Hello!")
# Output: {'Hello,': 1, 'hello.': 1, 'Hello!': 1}
# Should be: {'hello': 3} (if punctuation removed)

# Limitation 3: Inefficiency
# For text with 1000 words:
# - Iterates 1000 times
# - Each iteration counts through 1000 words
# - Total: 1,000,000 operations
# Better approach: single pass with dictionary

# Limitation 4: No return
result = Count.count_words("test")  # Returns None
# Cannot use result for further processing

# Limitation 5: No validation
Count.count_words(None)  # AttributeError
Count.count_words("")    # Works but returns {}

# Limitation 6: Output format
Count.count_words("the cat sat on the mat")
# Output: {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
# Not sorted, not formatted nicely

# Limitation 7: No filtering
Count.count_words("the a an the a the")
# Output: {'the': 3, 'a': 2, 'an': 1}
# Common words not filtered

# Limitation 8: No interface
# main.py is empty - no way to run interactively

```

## Potential Enhancements

1.  **Case-Insensitive Counting**
    
    -   Convert all words to lowercase
    -   Use casefold() for better handling
    -   Normalize before counting
    -   More accurate frequency
    -   User-friendly results
2.  **Punctuation Removal**
    
    -   Strip punctuation from words
    -   Use string.punctuation
    -   Regular expressions for cleaning
    -   Normalize text before processing
    -   Accurate word identification
3.  **Efficient Algorithm**
    
    -   Single-pass counting
    -   Use dictionary directly
    -   O(n) time complexity
    -   No redundant counting
    -   Better performance
    
    ```python
    @staticmethod
    def count_words(string):
        count_dict = {}
        for word in string.split():
            count_dict[word] = count_dict.get(word, 0) + 1
        return count_dict
    ```
    
4.  **Return Dictionary**
    
    -   Return instead of print
    -   Allow programmatic use
    -   Reusable results
    -   Flexible output handling
    -   Better function design
5.  **Input Validation**
    
    -   Check for None
    -   Validate string type
    -   Handle empty strings
    -   Error messages
    -   Type hints
6.  **Formatted Output**
    
    -   Sort by frequency
    -   Sort alphabetically
    -   Pretty print format
    -   Top N words
    -   Visual representation
7.  **Stop Word Filtering**
    
    -   Remove common words
    -   Configurable stop word list
    -   Focus on meaningful words
    -   Better analysis
    -   Customizable filtering
8.  **Interactive Interface**
    
    -   Menu-driven program
    -   User input for text
    -   File input support
    -   Multiple analysis options
    -   Export results
9.  **Advanced Features**
    
    -   Word cloud generation
    -   Frequency charts
    -   N-gram analysis
    -   Sentiment analysis
    -   Statistical reports
10. **Collections.Counter Usage**
    
    -   Use built-in Counter class
    -   More efficient
    -   Additional methods
    -   Most common words
    -   Professional approach
    
    ```python
    from collections import Counter
    
    @staticmethod
    def count_words(string):
        return Counter(string.split())
    ```

## Better Implementation Example

```python
from collections import Counter
import string

class Count:
    @staticmethod
    def count_words(text, case_sensitive=False, remove_punctuation=True):
        """
        Count word frequency in text.
        
        Args:
            text: Input string to analyze
            case_sensitive: If False, converts to lowercase
            remove_punctuation: If True, removes punctuation
        
        Returns:
            Dictionary of word frequencies
        """
        if not text:
            return {}
        
        # Normalize case
        if not case_sensitive:
            text = text.lower()
        
        # Remove punctuation
        if remove_punctuation:
            text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Count words efficiently
        words = text.split()
        return dict(Counter(words))
    
    @staticmethod
    def display_results(word_freq, top_n=None, sort_by='frequency'):
        """Display word frequencies in formatted way."""
        if sort_by == 'frequency':
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        else:
            sorted_words = sorted(word_freq.items())
        
        if top_n:
            sorted_words = sorted_words[:top_n]
        
        print(f"{'Word':<20} {'Frequency':>10}")
        print("-" * 30)
        for word, count in sorted_words:
            print(f"{word:<20} {count:>10}")

```

## Usage Examples

```python
# Current implementation
Count.count_words("Hello World, How are you? Are you here?")
# Output: {'Hello': 1, 'World,': 1, 'How': 1, 'are': 1, 'you?': 2, 'Are': 1, 'you': 1, 'here?': 1}

# Better implementation
result = Count.count_words("Hello World, How are you? Are you here?", 
                          case_sensitive=False, 
                          remove_punctuation=True)
# Output: {'hello': 1, 'world': 1, 'how': 1, 'are': 2, 'you': 3, 'here': 1}

Count.display_results(result, sort_by='frequency')
# Output:
# Word                  Frequency
# ------------------------------
# you                           3
# are                           2
# hello                         1
# world                         1
# how                           1
# here                          1

```

## Code Quality Features

✅ Static method design  
✅ Dictionary-based counting  
✅ String manipulation techniques  
✅ Tuple conversion for immutability  
✅ Simple and readable code  
✅ Class-based organization  
✅ Built-in count() method usage  
✅ Direct dictionary building  
✅ No external dependencies  
✅ Demonstrates basic frequency analysis  

## Notes

-   **No External Libraries Required** - Uses only Python standard library features.
-   Algorithm has O(n²) time complexity due to repeated counting.
-   Case-sensitive by default - "Hello" and "hello" are different.
-   Punctuation attached to words affects counting accuracy.
-   main.py is currently empty - no interactive interface.
-   Best used as a learning example for dictionary operations.
-   Consider using collections.Counter for production code.
-   Running counter.py directly shows example output.