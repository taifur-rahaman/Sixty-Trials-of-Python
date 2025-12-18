# Email Validator

A Python program that validates email addresses using regular expressions (regex). The validator checks if an email follows standard formatting rules including proper username structure, @ symbol, domain name, and .com extension.

## Features

1. **Regex-Based Validation**
   - Uses regular expressions for pattern matching.
   - Validates email structure and format.
   - Fast and efficient validation method.

2. **Email Format Requirements**
   - Username can contain letters, numbers, underscores.
   - Optional dots or hyphens between username parts.
   - Must have @ symbol separating username and domain.
   - Domain name followed by .com extension.

3. **Object-Oriented Design**
   - Encapsulated Validator class.
   - Email stored as private attribute.
   - Clean, reusable validation method.

4. **Simple Interface**
   - One-line validation check: `validator.is_valid()`.
   - Returns True for valid, False for invalid.
   - Clear console feedback to user.

## How It Works

### Validator Class Structure

```python
class Validator:
    def __init__(self, email):
        self._email = email  # Private attribute
        
    def is_valid(self):
        pattern = r'^\w+([\.-]?\w+)*@\w+([\.]com$)+'
        return re.match(pattern, self._email)
```

**Key Components:**
- **Private Attribute**: `_email` stores the input email
- **Validation Method**: `is_valid()` returns match object or None
- **Regex Pattern**: Defines valid email structure
- **re.match()**: Checks if pattern matches from start of string

### Regex Pattern Breakdown

```regex
^\w+([\.-]?\w+)*@\w+([\.]com$)+
```

Let's break this down piece by piece:

| Pattern | Meaning | Example |
|---------|---------|---------|
| `^` | Start of string | - |
| `\w+` | One or more word characters (letters, digits, underscore) | john, user123 |
| `([\.-]?\w+)*` | Optional dot or hyphen followed by word characters (repeatable) | .doe, -smith |
| `@` | Literal @ symbol | @ |
| `\w+` | One or more word characters (domain name) | gmail, company |
| `([\.]com$)+` | Literal dot followed by "com" at end | .com |
| `$` | End of string | - |

**Valid Patterns:**
- `username@domain.com`
- `first.last@company.com`
- `user-name@site.com`
- `user_123@email.com`

**Invalid Patterns:**
- Missing @ symbol
- No .com extension
- Spaces in email
- Special characters not allowed
- Multiple @ symbols

### Validation Flow

```python
email = "john.doe@example.com"
validator = Validator(email)
result = validator.is_valid()  # Returns Match object or None

if result:  # Truthy if match found
    print("Valid")
else:  # None is falsy
    print("Invalid")
```

## Project Structure

```
project/
├── main.py              # Main program with user interface
└── validator.py         # Validator class with regex logic
```

## Key Concepts Demonstrated

### Regular Expressions (Regex)
```python
import re
pattern = r'^\w+([\.-]?\w+)*@\w+([\.]com$)+'
re.match(pattern, string)
```
- **re.match()**: Checks pattern from start of string
- **Raw String (r'')**: Prevents backslash escaping issues
- **Metacharacters**: Special characters with meaning (\w, ^, $, +, *, etc.)

### Common Regex Metacharacters

| Metacharacter | Meaning | Example |
|---------------|---------|---------|
| `\w` | Word character [a-zA-Z0-9_] | a, Z, 5, _ |
| `\d` | Digit [0-9] | 0-9 |
| `^` | Start of string | ^hello matches "hello..." |
| `$` | End of string | world$ matches "...world" |
| `+` | One or more | a+ matches "a", "aa", "aaa" |
| `*` | Zero or more | a* matches "", "a", "aa" |
| `?` | Zero or one (optional) | a? matches "" or "a" |
| `[]` | Character class | [abc] matches "a" or "b" or "c" |
| `()` | Grouping | (ab)+ matches "ab", "abab" |
| `\.` | Escaped dot (literal) | \. matches "." |
| `.` | Any character except newline | . matches any char |

### Object-Oriented Encapsulation
```python
class Validator:
    def __init__(self, email):
        self._email = email  # Private by convention
```
- Leading underscore signals internal use
- Encapsulates validation logic
- Can be extended with more validation methods

### Truthy/Falsy Pattern
```python
if validator.is_valid():  # Match object is truthy, None is falsy
    print("Valid")
```
- `re.match()` returns Match object (truthy) or None (falsy)
- Simplifies conditional logic
- Pythonic way to check for matches

## Pattern Limitations

### Current Restrictions
1. **Extension**: Only accepts `.com` emails
   - Rejects `.org`, `.net`, `.edu`, etc.
   - International domains like `.co.uk` not supported

2. **Domain**: Limited validation
   - Doesn't verify actual domain existence
   - No subdomain support validation

3. **Characters**: Limited special characters
   - Allows: letters, numbers, underscore, dot, hyphen
   - Doesn't allow: +, %, &, etc. (which are technically valid)

4. **Local Part**: Basic validation
   - No length checking
   - Doesn't validate against RFC 5322 fully

### More Comprehensive Pattern (Alternative)

For more robust validation:
```python
# Accepts multiple TLDs
pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*\.(com|org|net|edu|gov)$'

# Even more permissive (closer to RFC 5322)
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

## Notes

- **Required Module**: Uses Python's built-in `re` module (no installation needed).
- Only validates format, not whether email actually exists.
- Pattern is case-sensitive but emails are typically case-insensitive.
- Returns Match object (truthy) for valid, None (falsy) for invalid.
- Does not validate email deliverability or DNS records.
- Running `validator.py` directly shows a humorous error message.

## Easter Egg

Try running `validator.py` directly to see a humorous message:
```bash
python validator.py
```
Output:
```
What the Hell are you doing? 
This is not the Main File.
Please run the main.py file.
```

## Common Issues and Solutions

**Pattern doesn't match valid emails:**
- Check for typos in regex pattern
- Ensure proper escaping of special characters
- Test pattern with online regex testers

**False positives:**
- Pattern may be too permissive
- Add more specific constraints
- Validate length and character limits


## Real-World Usage

This type of validation is useful for:
- ✅ Frontend form validation (quick format check)
- ✅ Basic input sanitization
- ✅ User experience improvement (immediate feedback)
- ✅ Educational purposes

Not suitable for:
- ❌ Final validation in production systems
- ❌ Security-critical applications
- ❌ Email deliverability verification
- ❌ RFC 5322 full compliance checking
