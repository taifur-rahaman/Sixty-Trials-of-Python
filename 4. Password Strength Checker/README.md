# Password Strength Checker

A Python program that validates password strength using regular expressions (regex). The validator checks if a password meets common security requirements including lowercase letters, uppercase letters, numbers, and minimum length.

## Features

1. **Multi-Criteria Validation**
   - At least one lowercase letter (a-z)
   - At least one uppercase letter (A-Z)
   - At least one digit (0-9)
   - Minimum 8 characters in length

2. **Regex-Based Pattern Matching**
   - Uses lookahead assertions for efficient validation
   - Single pattern checks all requirements simultaneously
   - Fast and reliable validation method

3. **Interactive Interface**
   - Continuous password checking until user exits
   - Clear visual header with centered title
   - Option to check multiple passwords in one session

4. **Object-Oriented Design**
   - Encapsulated Validator class
   - Password stored as private attribute
   - Clean, reusable validation method

5. **User-Friendly Feedback**
   - Clear valid/invalid messages
   - Option to continue or exit
   - Case-insensitive exit prompt

## How It Works

### Validator Class Structure

```python
class Validator:
    def __init__(self, password):
        self._password = password  # Private attribute
    
    def is_valid(self):
        pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\w]).{8,}'
        if re.match(pattern, self._password):
            return True
        else:
            return False
```

**Key Components:**
- **Private Attribute**: `_password` stores the input password
- **Validation Method**: `is_valid()` returns Boolean (True/False)
- **Regex Pattern**: Uses lookahead assertions for complex validation
- **re.match()**: Checks pattern from start of string

### Regex Pattern Breakdown

```regex
(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\w]).{8,}
```

Let's break this down piece by piece:

| Pattern | Type | Meaning | Example Match |
|---------|------|---------|---------------|
| `(?=.*[a-z])` | Positive Lookahead | Must contain at least one lowercase letter | a, b, z |
| `(?=.*[A-Z])` | Positive Lookahead | Must contain at least one uppercase letter | A, B, Z |
| `(?=.*[0-9])` | Positive Lookahead | Must contain at least one digit | 0, 1, 9 |
| `(?=.*[\w])` | Positive Lookahead | Must contain at least one word character | Any letter, digit, or _ |
| `.{8,}` | Quantifier | Minimum 8 characters of any type | Any 8+ chars |

### Understanding Lookahead Assertions

**Positive Lookahead `(?=...)`:**
- Checks if pattern exists ahead without consuming characters
- Allows multiple conditions to be checked at same position
- Zero-width assertion (doesn't advance cursor)

**Example Flow:**
```python
Password: "Abc123xy"

Check 1: (?=.*[a-z]) → Looks ahead → Finds "b","c","x","y" → ✓
Check 2: (?=.*[A-Z]) → Looks ahead → Finds "A" → ✓
Check 3: (?=.*[0-9]) → Looks ahead → Finds "1","2","3" → ✓
Check 4: (?=.*[\w])  → Looks ahead → Finds word chars → ✓
Check 5: .{8,}       → Counts chars → 8 characters → ✓

Result: Valid password
```

### Validation Flow

```python
password = "SecurePass123"
validator = Validator(password)
result = validator.is_valid()  # Returns True or False

if result:  # True
    print("Valid")
else:
    print("Invalid")
```

### Why These Are Invalid

| Password | Issue | Missing Requirement |
|----------|-------|---------------------|
| `password` | No uppercase, no numbers | A-Z, 0-9 |
| `PASSWORD` | No lowercase, no numbers | a-z, 0-9 |
| `Pass123` | Too short | Minimum 8 characters |
| `Short1` | Too short, no uppercase/lowercase both | Multiple issues |
| `abcdefgh` | No uppercase, no numbers | A-Z, 0-9 |
| `ABCDEFGH` | No lowercase, no numbers | a-z, 0-9 |
| `12345678` | No letters | a-z, A-Z |

## Project Structure

```
project/
├── main.py              # Main program with user interface
└── validator.py         # Validator class with regex logic
```

## Key Concepts Demonstrated

### Regular Expressions - Lookahead Assertions

**Positive Lookahead `(?=...)`:**
```python
# Check if pattern exists ahead
(?=.*[a-z])  # "Does lowercase exist somewhere ahead?"
```

**Why Use Lookaheads?**
- Check multiple conditions at same position
- Order-independent validation
- Don't consume characters
- More flexible than linear patterns

**Alternative Without Lookaheads (more complex):**
```python
# Would need multiple passes or complex alternations
pattern1 = r'[a-z]'  # Has lowercase?
pattern2 = r'[A-Z]'  # Has uppercase?
pattern3 = r'[0-9]'  # Has digit?
pattern4 = r'.{8,}'  # Length check?
# Would need to check each separately - inefficient!
```

### Boolean Return Pattern
```python
def is_valid(self):
    if re.match(pattern, self._password):
        return True
    else:
        return False
```

### Centered String Formatting
```python
"Password Strength Checker".center(40)
# Adds padding to center text in 40 chars width
```

### Case-Insensitive Input
```python
choice = input("Continue? (y/n): ").casefold()
if choice == "n":
    break
```

## Password Requirements

### Current Implementation

✅ **Minimum 8 characters**  
✅ **At least 1 lowercase letter (a-z)**  
✅ **At least 1 uppercase letter (A-Z)**  
✅ **At least 1 digit (0-9)**  
❌ No special character requirement  
❌ No maximum length limit  
❌ No common password check  
❌ No sequential character detection  

### Password Strength Scale

| Criteria Met | Strength | Security Level |
|--------------|----------|----------------|
| 0-1 | Very Weak | 🔴 Unacceptable |
| 2 | Weak | 🟠 Poor |
| 3 | Moderate | 🟡 Fair |
| 4 | Strong | 🟢 Good |
| 4+ with special chars | Very Strong | 🔵 Excellent |

## Notes

- **Required Module**: Uses Python's built-in `re` module (no installation needed).
- Only validates format, not password uniqueness or commonality.
- Does not check against compromised password databases.
- Case-sensitive password checking (as it should be).
- The `(?=.*[\w])` lookahead is redundant (already covered by other checks).
- No password strength scoring (only pass/fail).
- Allows special characters but doesn't require them.


## Real-World Recommendations

For production password validation, consider:

1. **Minimum 12 characters** (not 8)
2. **Require special characters**: `[@$!%*?&#^()_+=]`
3. **Check against HaveIBeenPwned API** for breached passwords
4. **Implement rate limiting** on validation attempts
5. **Use zxcvbn library** for advanced strength estimation
6. **Set maximum length** (e.g., 128 chars to prevent DoS)
7. **Reject common patterns** (keyboard walks, sequences)
8. **Consider passphrase approach** (4+ random words)
