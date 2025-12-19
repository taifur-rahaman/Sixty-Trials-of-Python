# Name Formatter

A Python program that formats and displays names using property decorators and custom string representation. The program demonstrates encapsulation, getter/setter properties, and formatted output with centered text display.

## Features

1. **Property Decorators**
   - Uses `@property` for getter methods
   - Uses `@setter` for controlled attribute assignment
   - Encapsulates first and last name attributes

2. **Automatic Title Case Formatting**
   - Converts input to Title Case on entry
   - Additional formatting in `__str__()` method
   - Ensures consistent name capitalization

3. **Custom String Representation**
   - Overrides `__str__()` method for formatted output
   - Centers full name in 40-character width
   - Clean, professional display format

4. **Simple User Interface**
   - Clear visual separators (equals signs)
   - Centered header title
   - Intuitive input prompts

5. **Object-Oriented Design**
   - Formatter class with private attributes
   - Demonstrates proper encapsulation
   - Clean separation of data and display logic

## How It Works

### Formatter Class Structure

```python
class Formatter:
    def __init__(self):
        pass  # Empty initialization
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
    
    def __str__(self):
        return f"{self._first_name} {self._last_name.title()}".center(40)
```

**Key Components:**
- **Empty Constructor**: No initialization parameters needed
- **Property Decorators**: Provide controlled attribute access
- **Private Attributes**: `_first_name` and `_last_name`
- **Custom String Method**: Returns formatted name string

### Property Pattern

**Getter (Read Access):**
```python
@property
def first_name(self):
    return self._first_name
```
- Accessed like an attribute: `name.first_name`
- Returns the private `_first_name` value
- No parentheses needed when accessing

**Setter (Write Access):**
```python
@first_name.setter
def first_name(self, first_name):
    self._first_name = first_name
```
- Set like an attribute: `name.first_name = "John"`
- Allows validation before assignment (not used here)
- Maintains encapsulation

### String Formatting Flow

```python
Input: "john" → .title() → "John" → setter → self._first_name = "John"
Input: "doe" → .title() → "Doe" → setter → self._last_name = "Doe"

When printed:
__str__() → f"{John} {Doe.title()}" → "John Doe".center(40)
         → "              John Doe              "
```

### Property Pattern

**Getter (Read Access):**
```python
@property
def first_name(self):
    return self._first_name
```
- Accessed like an attribute: `name.first_name`
- Returns the private `_first_name` value
- No parentheses needed when accessing

**Setter (Write Access):**
```python
@first_name.setter
def first_name(self, first_name):
    self._first_name = first_name
```
- Set like an attribute: `name.first_name = "John"`
- Allows validation before assignment (not used here)
- Maintains encapsulation
