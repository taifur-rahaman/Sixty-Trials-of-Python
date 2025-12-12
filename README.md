# ⚔️ Fifty Trials of Python - Novice to Master

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

## 🌱 NOVICE LEVEL (Focus: Basics + String/List Methods)

### 1. **Word Counter**
- Input: A sentence
- Output: Count how many words, vowels, and consonants
- Topics: String methods (`.split()`, `.lower()`, `.count()`)

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

### 9. **File Creator**
- Create a text file and write some text to it
- Topics: File handling (write mode)

---

## 🌿 BEGINNER LEVEL (Focus: Tuples, Sets, Dict + Functions + Files)

### 8. **Safe Division Calculator**
- Divide two numbers with exception handling for division by zero
- Topics: Exception handling (try/except), functions

### 9. **File Creator**
- Create a text file and write some text to it
- Topics: File handling (write mode)

### 10. **Grade Calculator**
- Function that takes student scores and returns average, highest, lowest
- Topics: Functions, tuple unpacking, list methods

### 12. **Contact Book**
- Store contacts in a dictionary {name: phone}
- Add, search, delete, update contacts
- Topics: Dictionary methods (`.get()`, `.update()`, `.pop()`)

### 13. **Todo List with File**
- Save todo items to a file, load them back
- Topics: File handling (read/write), list methods, exception handling

### 14. **Unique Word Counter**
- Count unique words in a text
- Topics: Sets, dictionary methods, string methods

### 16. **Student Database**
- Store student info: {name: (age, grade, city)}
- Search by name, list all students
- Topics: Dictionary, tuple unpacking

### 17. **Word Frequency Counter**
- Count how many times each word appears in text
- Topics: Dictionary methods, string methods, `.setdefault()`

### 18. **Merge Two Lists**
- Function that merges two lists, removes duplicates, sorts them
- Topics: Functions, sets, list methods (`.sort()`, `.extend()`)

### 19. **Tuple Swapper**
- Function that swaps elements in a tuple
- Topics: Tuple unpacking, functions

### 20. **Append to File**
- Append new entries to existing file without overwriting
- Topics: File handling (append mode)

---

## 🌳 INTERMEDIATE LEVEL (Focus: *args, **kwargs, RegEx + Advanced File/Exception)

### 15. **Flexible Calculator**
- `calculate(operation, *numbers)` - add, multiply, etc. any number of values
- Topics: *args, functions

### 16. **Safe Input Validator**
- Get user input with validation and custom error messages
- Retry on invalid input (use while + try/except)
- Topics: Exception handling, functions, string methods

### 17. **Config Manager**
- Function that accepts any keyword arguments and stores as config
- `set_config(theme='dark', lang='en', font_size=12)`
- Topics: **kwargs, dictionary methods

### 19. **Phone Number Validator**
- Validate different phone formats: (123) 456-7890, 123-456-7890, etc.
- Topics: Regular expressions

### 20. **Email Extractor**
- Extract all emails from a text
- Topics: Regular expressions (`.findall()`)

### 21. **File Statistics**
- Read file and show: number of lines, words, chars, average word length
- Handle multiple exception types (FileNotFoundError, PermissionError, etc.)
- Topics: File handling, exception handling (multiple except blocks)

### 22. **Logging Function**
- `log(level, *messages, **details)` 
- Example: `log('ERROR', 'Failed', 'Retry', user='john', time='10:30')`
- Topics: *args, **kwargs

### 20. **Text Cleaner**
- Remove special characters, extra spaces, format text
- Topics: Regular expressions (`.sub()`, `.match()`)

### 21. **URL Parser**
- Extract protocol, domain, path from URL
- Topics: Regular expressions, tuple unpacking

### 22. **Flexible Greeter**
- `greet(*names, greeting='Hello', sep=', ')`
- Should handle any number of names
- Topics: *args, **kwargs, string methods

---

## 🌲 ADVANCED LEVEL (Focus: Generators + Combined Concepts)

### 23. **File Line Reader (Generator)**
- Read large file line by line using generator
- Topics: Generator functions, `yield`

### 24. **Fibonacci Generator**
- Generate infinite Fibonacci sequence
- Topics: Generator functions

### 25. **Prime Number Generator**
- Generate prime numbers up to N using generator
- Topics: Generator functions, functions

### 26. **Safe File Reader with Context Manager**
- Use `with` statement to safely read files
- Handle encoding errors
- Topics: File handling (context manager), exception handling

### 27. **Data Pipeline**
- Create generators that filter, transform, and process data
- Example: numbers → square them → only evens → sum
- Topics: Generator chaining, `yield`

### 27. **CSV Parser (Generator)**
- Parse CSV file line by line, yield dictionary for each row
- Topics: Generator, dictionaries, string methods

### 30. **Password Generator**
- Generate random passwords with custom rules
- `generate_password(length=12, **options)` (uppercase, numbers, symbols)
- Topics: **kwargs, string methods, functions

### 31. **Batch Processor (Generator)**
- Process items in batches
- `batch([1,2,3,4,5,6], size=2)` → yields `[1,2], [3,4], [5,6]`
- Topics: Generators, list slicing

### 32. **Multi-File Reader (Generator)**
- Read from multiple files sequentially using generator
- Yield one line at a time from all files
- Handle missing files gracefully
- Topics: Generators, file handling, exception handling

### 33. **Text Search with Context**
- Search for pattern in text, return surrounding lines
- Topics: Regular expressions, generators, string methods

---

## 🏔️ EXPERT LEVEL (Focus: Complex Combinations)

### 31. **Command Line Argument Parser**
- Parse commands like: `--name John --age 25 --hobbies reading gaming`
- Topics: *args, **kwargs, string methods, dictionaries

### 32. **Transaction Logger**
- Log transactions to file with timestamps
- Implement rollback on errors
- Topics: File handling (append), exception handling, functions

### 33. **Data Validator Framework**
- Create validation functions that accept any rules
- `validate(data, *validators, **options)`
- Topics: *args, **kwargs, functions, regular expressions

### 33. **Smart Dictionary Merger**
- Merge multiple dictionaries with conflict resolution
- `merge_dicts(*dicts, strategy='override')`
- Topics: *args, **kwargs, dictionary methods

### 36. **Log File Analyzer (Generator)**
- Parse log files, extract errors, warnings, count occurrences
- Topics: Generators, regex, dictionaries, string methods

### 37. **Configuration File Parser**
- Parse INI/config files into nested dictionaries
- Topics: Generators, regex, dictionaries, string methods

### 38. **Retry Decorator**
- Create a decorator that retries function on exception
- `@retry(times=3, exceptions=(ValueError, TypeError))`
- Topics: Exception handling, functions, *args, **kwargs

### 39. **Query Builder**
- Build SQL-like queries from Python
- `query('users', *fields, **conditions)`
- Topics: *args, **kwargs, string methods, `.join()`

### 37. **Data Transformation Pipeline**
- Chain multiple transformations on data
- `pipeline(data, *transformers, **options)` 
- Topics: Generators, *args, **kwargs, functions

### 38. **Smart Text Formatter**
- Format text with templates and variables
- Handle missing variables, apply transformations
- Topics: Regular expressions, **kwargs, string methods, dictionaries

---

## 🎯 MASTER LEVEL (Real-World Projects)

### 44. **Mini Database System**
- In-memory database with CRUD operations
- Persist data to file, handle corruption
- Automatic backups, transaction support
- Topics: All concepts combined

### 45. **Text-Based Adventure Game**
- Room navigation, inventory system, command parser
- Save/load game state to file
- Handle invalid commands gracefully
- Topics: Dictionaries, tuples, sets, functions, file handling, exception handling

### 46. **Report Generator**
- Generate formatted reports from data
- Support multiple output formats (text, markdown)
- Handle missing data gracefully
- Topics: Generators, **kwargs, string methods, dictionaries, file handling

### 47. **Expression Evaluator**
- Parse and evaluate math expressions: "2 + 3 * 4"
- Handle division by zero and invalid syntax
- Topics: Regular expressions, functions, dictionaries, exception handling

### 48. **Data Aggregator**
- Aggregate data from multiple sources
- `aggregate(*sources, by='sum', **filters)`
- Topics: Generators, *args, **kwargs, dictionaries, sets

### 49. **Robust Web Scraper Parser**
- Parse HTML/text, extract specific patterns
- Clean and structure data
- Handle malformed data gracefully
- Topics: Regular expressions, generators, dictionaries, exception handling, all string methods

### 50. **Task Scheduler Simulator**
- Schedule tasks, handle priorities, dependencies
- Save schedule to file, load on restart
- Handle task failures and retries
- Topics: Dictionaries, tuples, sets, functions, generators, file handling, exception handling

---

## 🎓 Progression Path

- **Novice (1-9)**: 1-2 weeks, solve atleast 1-2 per day
- **Beginner (10-20)**: 2 weeks, solve atleast 1 per day
- **Intermediate (21-34)**: 3 weeks, solve atleast 1 per 1-2 days
- **Advanced (35-43)**: 3 weeks, solve atleast 1 per 2 days
- **Expert (44-50)**: 4 weeks, solve atleast 1 per 3 days
- **Master (51-56)**: 4-6 weeks, solve atleast 1 per week
---