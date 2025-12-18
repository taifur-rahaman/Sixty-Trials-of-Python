import re

class Validator:
    def __init__(self, password):
        self._password = password
    
    def is_valid(self):
        pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\w]).{8,}'
        if re.match(pattern, self._password):
            return True
        else:
            return False
