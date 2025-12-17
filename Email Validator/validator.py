import re

class Validator:
    def __init__(self, email):
        self._email = email
        
    def is_valid(self):
        pattern = r'^\w+([\.-]?\w+)*@\w+([\.]com$)+'
        return re.match(pattern, self._email)

# NOTE: Test Code
if __name__ == "__main__":
    print("What the Hell are you doing? \nThis is not the Main File.\nPlease run the main.py file.")