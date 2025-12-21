# 🔮 Sixty Trials of Python : Novice to Master

## 📚 Topics Covered
- String Methods
- Regular Expression
- List Methods
- Tuple (Methods & Unpacking)
- Sets Methods
- Dictionary Methods
- Functions (Positional, Keyword, *args, **kwargs)
- Generator
- Exception Handling
- File Handling

---

## 🎓 Progression Path

- **Novice (1-10)**: 1-2 weeks, solve atleast 1-2 per day 
    - [ ] Planning
    - [ ] On-Going
    - [x] Completed
- **Beginner (11-20)**: 2 weeks, solve atleast 1 per day
    - [ ] Planning
    - [x] On-Going
    - [ ] Completed
- **Intermediate (21-32)**: 2-3 weeks, solve atleast 1 per day
    - [x] Planning
    - [ ] On-Going
    - [ ] Completed
- **Advanced (33-43)**: 2-3 weeks, solve atleast 1 per 1-2 days
    - [x] Planning
    - [ ] On-Going
    - [ ] Completed
- **Expert (44-52)**: 3-4 weeks, solve atleast 1 per 2 days
    - [x] Planning
    - [ ] On-Going
    - [ ] Completed
- **Master (53-60)**: 4-6 weeks, solve atleast 1 per 3-4 days
    - [x] Planning
    - [ ] On-Going
    - [ ] Completed


## 🌱 NOVICE LEVEL (Focus: Basics + String/List Methods)

### 1. **Word Counter**
- Input: A sentence
- Output: Count how many words, vowels, and consonants
- Topics: String methods (`.split()`, `.lower() / .casefold()`, `.join()`,`.isalpha()`, `len()`)

### 2. **Email Validator**
- Check if an email is valid (has @ and .)
- Topics: String methods (`.find()`, `.index()`, `in`)

### 3. **Shopping List Manager**
- Add items, remove items, show list
- Topics: List methods (`.append()`, `.remove()`, `.clear()`)

### 4. **Password Strength Checker**
- Check if password has uppercase, lowercase, numbers, special chars
- Topics: String methods (`.isupper()`, `.islower()`, `.isdigit()`)

### 5. **Name Formatter**
- Input: "john doe"
- Output: "John Doe"
- Topics: String methods (`.title()`, `.capitalize()`, `.strip()`)

### 6. **Duplicate Remover**
- Remove duplicates from a list
- Topics: Sets, list methods

### 7. **Reverse Words**
- Input: "Hello World"
- Output: "World Hello"
- Topics: String methods (`.split()`, `.join()`), list methods (`.reverse()`)

### 8. **Safe Division Calculator**
- Divide two numbers with exception handling for division by zero
- Topics: Exception handling (try/except), functions

### 9. **Simple File Writer**
- Create a text file and write some lines to it
- Topics: File handling (write mode)

### 10. **File Reader with Line Count**
- Read a file and count how many lines it has
- Topics: File handling (read mode), basic exception handling

---

## 🌿 BEGINNER LEVEL (Focus: Tuples, Sets, Dict + Functions + Basic Files)

### 11. **Grade Calculator**
- Function that takes student scores and returns average, highest, lowest
- Topics: Functions, tuple unpacking, list methods

### 12. **Contact Book**
- Store contacts in a dictionary {name: phone}
- Add, search, delete, update contacts
- Topics: Dictionary methods (`.get()`, `.update()`, `.pop()`)

### 13. **Unique Word Counter**
- Count unique words in a text
- Topics: Sets, dictionary methods, string methods

### 14. **Student Database**
- Store student info: {name: (age, grade, city)}
- Search by name, list all students
- Topics: Dictionary, tuple unpacking

### 15. **Word Frequency Counter**
- Count how many times each word appears in text
- Topics: Dictionary methods, string methods, `.setdefault()`

### 16. **List Merger**
- Function that merges two lists, removes duplicates, sorts them
- Topics: Functions, sets, list methods (`.sort()`, `.extend()`)

### 17. **Tuple Swapper**
- Function that swaps elements in a tuple: (a, b, c) → (c, b, a)
- Topics: Tuple unpacking, functions

### 18. **Todo List with File Persistence**
- Save todo items to a file, load them back on restart
- Topics: File handling (read/write), list methods, exception handling

### 19. **Safe File Reader**
- Read a file and handle FileNotFoundError gracefully
- Topics: File handling, exception handling (try/except)

### 20. **Append to Log File**
- Append new entries to existing log file without overwriting
- Topics: File handling (append mode), string methods

---

## 🌳 INTERMEDIATE LEVEL (Focus: *args, **kwargs, RegEx + Advanced Files)

### 21. **Flexible Calculator**
- `calculate(operation, *numbers)` - add, multiply, etc. any number of values
- Topics: *args, functions

### 22. **Config Manager**
- Function that accepts any keyword arguments and stores as config
- `set_config(theme='dark', lang='en', font_size=12)`
- Topics: **kwargs, dictionary methods

### 23. **Phone Number Validator**
- Validate different phone formats: (123) 456-7890, 123-456-7890, etc.
- Topics: Regular expressions

### 24. **Email Extractor**
- Extract all emails from a text
- Topics: Regular expressions (`.findall()`)

### 25. **Logging Function**
- `log(level, *messages, **details)` 
- Example: `log('ERROR', 'Failed', 'Retry', user='john', time='10:30')`
- Topics: *args, **kwargs, string methods

### 26. **Text Cleaner with RegEx**
- Remove special characters, extra spaces, format text using regex
- Topics: Regular expressions (`.sub()`, `.match()`)

### 27. **URL Parser**
- Extract protocol, domain, path from URL using regex
- Topics: Regular expressions, tuple unpacking

### 28. **Flexible Greeter**
- `greet(*names, greeting='Hello', sep=', ')`
- Should handle any number of names
- Topics: *args, **kwargs, string methods (`.join()`)

### 29. **CSV Writer**
- Write list of dictionaries to CSV file manually (don't use csv module)
- Topics: File handling, string methods (`.join()`), exception handling

### 30. **File Statistics Analyzer**
- Read file and show: lines, words, chars, average word length
- Handle multiple exception types (FileNotFoundError, PermissionError)
- Topics: File handling, exception handling (multiple except blocks)

### 31. **Safe Input Validator**
- Get user input with validation, retry on error
- `get_input(prompt, validator_func, max_retries=3)`
- Topics: Exception handling, functions, while loops

### 32. **Multiple Exception Handler**
- Create a function that demonstrates handling ValueError, TypeError, KeyError
- Topics: Exception handling (multiple except blocks)

---

## 🌲 ADVANCED LEVEL (Focus: Generators + File Streams + Complex Exceptions)

### 33. **File Line Reader Generator**
- Read large file line by line using generator
- Topics: Generators, `yield`, file handling

### 34. **Fibonacci Generator**
- Generate infinite Fibonacci sequence
- Topics: Generators, `yield`

### 35. **Prime Number Generator**
- Generate prime numbers up to N using generator
- Topics: Generators, functions

### 36. **Data Pipeline with Generators**
- Create generator chain: numbers → square → only evens → format
- Topics: Generator chaining, `yield`

### 37. **CSV Parser Generator**
- Parse CSV file line by line, yield dictionary for each row
- Topics: Generators, dictionaries, string methods, file handling

### 38. **Batch Processor**
- Process items in batches using generator
- `batch([1,2,3,4,5,6], size=2)` → yields `[1,2], [3,4], [5,6]`
- Topics: Generators, list slicing

### 39. **File Backup System**
- Backup file with timestamp, handle errors
- Use try/except/else/finally properly
- Topics: File handling, exception handling (all blocks), string methods

### 40. **Multi-File Reader Generator**
- Read from multiple files sequentially using generator
- Yield one line at a time from all files
- Handle missing files gracefully
- Topics: Generators, file handling, exception handling

### 41. **Custom Exception Classes**
- Create custom exceptions: InvalidAgeError, NegativeValueError
- Use them in age validator function
- Topics: Exception handling (custom exceptions, raise)

### 42. **Context Manager File Handler**
- Demonstrate proper use of `with` statement for file operations
- Show difference between with and without context manager
- Topics: File handling (context manager), exception handling

### 43. **Log File Search Generator**
- Search for pattern in log file, yield matching lines with line numbers
- Topics: Regular expressions, generators, file handling

---

## 🏔️ EXPERT LEVEL (Focus: Complex Combinations + Error Recovery)

### 44. **Command Line Parser**
- Parse commands: `--name John --age 25 --hobbies reading gaming`
- Topics: *args, **kwargs, string methods, dictionaries

### 45. **Data Validator Framework**
- Create validation system: `validate(data, *validators, **options)`
- Each validator is a function that raises exception on failure
- Topics: *args, **kwargs, functions, exception handling

### 46. **Smart Dictionary Merger**
- Merge multiple dicts with conflict resolution
- `merge_dicts(*dicts, strategy='override', on_conflict=None)`
- Topics: *args, **kwargs, dictionary methods

### 47. **Transaction Logger**
- Log transactions to file with timestamps
- Implement rollback on errors
- Topics: File handling (append), exception handling, functions

### 48. **Fault-Tolerant File Processor**
- Process file even if some lines are corrupted
- Log errors to separate error file, continue processing
- Topics: File handling, exception handling, generators

### 49. **Retry Decorator**
- Create decorator that retries function on exception
- `@retry(times=3, exceptions=(ValueError, TypeError))`
- Topics: Functions, exception handling, *args, **kwargs

### 50. **Configuration File Parser**
- Parse INI-like config files into nested dictionaries
- Handle syntax errors gracefully
- Topics: File handling, regex, dictionaries, exception handling, generators

### 51. **File Difference Checker**
- Compare two files line by line, report differences
- Handle files of different sizes
- Topics: File handling, generators, sets, exception handling

### 52. **Safe JSON-like Handler**
- Save/load dictionary to file in custom format
- If file corrupted, restore from backup
- Topics: File handling, exception handling (recovery), dictionaries

---

## 🎯 MASTER LEVEL (Real-World Projects)

### 53. **Mini Database System**
- In-memory database with CRUD operations
- Persist to file, handle corruption, automatic backups
- Support filtering and sorting
- Topics: All concepts combined

### 54. **Text-Based Adventure Game**
- Room navigation, inventory system, command parser
- Save/load game state to file
- Handle invalid commands gracefully
- Topics: Dictionaries, tuples, file handling, exception handling

### 55. **Report Generator**
- Generate formatted reports from data
- Support multiple formats (text, markdown, CSV)
- Handle missing data gracefully
- Topics: Generators, **kwargs, string methods, file handling

### 56. **Expression Evaluator**
- Parse and evaluate math expressions: "2 + 3 * 4"
- Handle division by zero, invalid syntax
- Topics: Regular expressions, functions, exception handling

### 57. **Data Aggregator Pipeline**
- Aggregate data from multiple sources
- `aggregate(*sources, by='sum', **filters)`
- Use generators for memory efficiency
- Topics: Generators, *args, **kwargs, dictionaries, file handling

### 58. **Log File Analyzer**
- Parse log files, extract errors/warnings
- Generate statistics and summary report
- Handle malformed log entries
- Topics: Regex, generators, dictionaries, file handling, exception handling

### 59. **Task Scheduler Simulator**
- Schedule tasks with priorities and dependencies
- Save schedule to file, load on restart
- Handle task failures and implement retries
- Topics: Dictionaries, tuples, sets, functions, file handling, exception handling

### 60. **Robust File Synchronizer**
- Sync files between two directories
- Handle permission errors, missing files
- Log all operations and errors
- Topics: File handling, exception handling, generators, all concepts

---


