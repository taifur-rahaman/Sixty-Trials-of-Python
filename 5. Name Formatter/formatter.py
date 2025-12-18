
class Formatter:
    def __init__(self):
        pass
    
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