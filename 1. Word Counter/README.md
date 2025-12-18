# Word Counter

A Python program that analyzes text strings by counting words, vowels, and consonants using object-oriented programming. Features a menu-driven interface for repeated analysis of the same input string.

## Features

1. **Word Count Analysis**
   - Counts total number of words in the input string.
   - Uses whitespace-based word splitting.
   - Handles multiple spaces correctly.

2. **Vowel Count Analysis**
   - Counts all vowels (a, e, i, o, u) in the string.
   - Case-insensitive counting (handles both upper and lowercase).
   - Ignores non-alphabetic characters.

3. **Consonant Count Analysis**
   - Counts all consonants in the string.
   - Calculated as: Total letters - Vowels.
   - Automatically excludes spaces and special characters.

4. **Case-Insensitive Processing**
   - Input normalized to lowercase using `.casefold()`.
   - Ensures consistent counting regardless of input case.
   - More robust than `.lower()` for international characters.

5. **Menu-Driven Interface**
   - Interactive console menu for repeated operations.
   - Analyze same string multiple ways without re-entry.
   - Clean exit option with goodbye message.

6. **Encapsulation**
   - Private helper method for internal letter counting.
   - String stored as private attribute.
   - Clean separation of concerns.

## How It Works

### Processor Class Structure

```python
class Processor:
    def __init__(self, string): 
        self._string = string  # Private attribute
    
    def count_words(self):
        return len(self._string.split())
    
    def count_vowels(self):
        # Counts 'a', 'e', 'i', 'o', 'u'
    
    def _count_letters(self):
        # Private method - counts total letters
    
    def count_consonants(self):
        # Consonants = Total Letters - Vowels
```

**Key Components:**
- **Private Attribute**: `_string` stores the input text
- **Public Methods**: `count_words()`, `count_vowels()`, `count_consonants()`
- **Private Helper**: `_count_letters()` for internal calculations
- **Single Responsibility**: Each method has one clear purpose

### Counting Algorithms

**Word Counting:**
```python
def count_words(self):
    return len(self._string.split())
# "Hello World" → ["Hello", "World"] → 2
```

**Vowel Counting:**
```python
def count_vowels(self):
    count = 0
    for char in self._string:
        if char.isalpha() and char in "aeiou":
            count += 1
    return count
# "Hello" → checks: h(no), e(yes), l(no), l(no), o(yes) → 2
```

**Letter Counting (Private Method):**
```python
def _count_letters(self):
    count = 0
    combine_string = ("").join(self._string.split())  # Remove spaces
    for char in combine_string:
        if char.isalpha():
            count += 1
    return count
# "Hello World!" → "HelloWorld!" → 10 letters
```

**Consonant Counting:**
```python
def count_consonants(self):
    return self._count_letters() - self.count_vowels()
# "Hello" → 5 letters - 2 vowels = 3 consonants
```

### Input Processing

```python
string = input("Enter a String: ").casefold()
process = Processor(string)
```
- Input converted to lowercase with `.casefold()`
- Processor object created with normalized string
- Object reused for all subsequent operations

### Error Handling
```
Enter your Choice: 5
Invalid Input. Please Try Again.

Enter your Choice: abc
Invalid Input. Please Try Again.
```

## Project Structure

```
project/
├── main.py              # Main program with menu interface
└── processor.py         # Processor class definition
```

## Key Concepts Demonstrated

### Private Attributes and Methods
```python
self._string              # Private attribute (by convention)
def _count_letters(self): # Private method (by convention)
```
- Leading underscore indicates internal use
- Not enforced by Python but signals intent
- Good practice for encapsulation

### Case-Insensitive String Processing
```python
string = input().casefold()
```
- `.casefold()` is more aggressive than `.lower()`
- Handles international characters better
- Example: German 'ß' → 'ss'

### Method Composition
```python
def count_consonants(self):
    return self._count_letters() - self.count_vowels()
```
- Builds complex functionality from simple methods
- Promotes code reuse
- Makes logic easier to understand and test

### String Manipulation Techniques
```python
self._string.split()           # Split by whitespace
("").join(list)                # Join without separator
char.isalpha()                 # Check if alphabetic
char in "aeiou"                # Membership test
```

### Match-Case for Menu Control
```python
match choice:
    case "1":
        # Word count
    case "0":
        exit()
    case _:
        # Invalid input
```

## Character Classification

### Vowels
- **Lowercase**: a, e, i, o, u
- **Uppercase**: Converted to lowercase by `.casefold()`
- **Count includes**: All vowel occurrences

### Consonants
- **Definition**: All alphabetic characters that are not vowels
- **Excludes**: Spaces, punctuation, numbers, special characters
- **Calculation**: Total letters - Total vowels

### Non-letters
- **Spaces**: Used for word separation, not counted as letters
- **Punctuation**: Ignored in letter/vowel/consonant counts
- **Numbers**: Ignored in all counts
- **Special Characters**: Ignored in all counts

## Notes

- **No External Libraries Required** - Uses only Python standard library features.
- **Python Version**: Match-case requires Python 3.10+ (can replace with if-elif for older versions).
- Input is processed once at startup and reused for all operations.
- Vowel checking is limited to standard English vowels (a, e, i, o, u).
- Word counting relies on whitespace - hyphenated words counted as one.
- The processor object maintains state throughout the session.
- Running `processor.py` directly shows a humorous error message.

## Behavior Details

### Word Counting
- **Method**: Split by any whitespace
- **Multiple Spaces**: Handled correctly (split ignores empty strings)
- **Leading/Trailing Spaces**: Automatically trimmed by split
- **Example**: `"  Hello   World  "` → 2 words

### Vowel Counting
- **Checks**: Both alphabetic AND vowel
- **Why**: Prevents counting non-letter characters
- **Example**: `"a1e2i3"` → counts only a, e, i (3 vowels)

### Consonant Counting
- **Two-Step Process**: 
  1. Remove all spaces to get continuous string
  2. Count alphabetic characters
  3. Subtract vowel count
- **Why Remove Spaces**: Prevents counting spaces as characters
- **Example**: `"Hello World"` → "HelloWorld" → 10 letters - 3 vowels = 7 consonants

## Potential Enhancements

### Additional Analysis Features
- Count specific letters or characters
- Find most/least common letter
- Calculate letter frequency distribution
- Count sentences (by punctuation)
- Average word length calculation
- Find longest/shortest word
- Count unique words
- Detect palindromes

### Input Flexibility
- Allow multiple string inputs per session
- Support file input for large texts
- Add string modification options (uppercase, reverse, etc.)
- Batch processing of multiple strings

### Output Improvements
- Display results as percentages
- Create visual bar charts in console
- Export results to file
- Generate summary reports
- Compare multiple texts

### Advanced Analysis
- Readability score calculation
- Language detection
- Sentiment analysis (basic)
- Keyword extraction
- Text complexity metrics

### Code Improvements
```python
# More Pythonic vowel counting
def count_vowels(self):
    return sum(1 for char in self._string if char in "aeiou")

# Alternative consonant counting
def count_consonants(self):
    return sum(1 for char in self._string if char.isalpha() and char not in "aeiou")
```

## Easter Egg

Try running `processor.py` directly to see a humorous message:
```bash
python processor.py
```
Output:
```
What the Hell are you doing? 
This is not the Main File.
Please run the main.py file.
```

This demonstrates the use of `if __name__ == "__main__":` to detect direct execution.

## Common Issues and Solutions

**Incorrect word count with punctuation:**
- Current behavior: "don't" counts as 1 word (correct)
- "hello-world" counts as 1 word (may want 2)
- Solution: Use regex for more sophisticated word splitting

**International characters:**
- Vowels limited to a, e, i, o, u
- Doesn't count á, é, í, ó, ú as vowels
- Solution: Expand vowel string or use Unicode categories

**Case sensitivity:**
- Handled by `.casefold()` at input
- If you want case-sensitive analysis, remove `.casefold()`

## Code Quality Features

✅ Object-oriented design with clear encapsulation  
✅ Private methods for internal logic  
✅ Single Responsibility Principle per method  
✅ DRY principle (consonants reuse other methods)  
✅ Case-insensitive processing  
✅ Clean separation of UI and logic  
✅ Menu-driven interface for usability  
✅ Humorous error handling in processor.py  
✅ Descriptive method names  
✅ Efficient string processing  

