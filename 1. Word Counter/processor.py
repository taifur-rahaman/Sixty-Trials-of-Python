
class Processor:
    def __init__(self, string): 
        self._string = string
    
    def count_words(self):
        return len(self._string.split())
    
    def count_vowels(self):
        count = 0
        for char in self._string:
            if char.isalpha() and char in "aeiou":
                count += 1
        return count
    
    def _count_letters(self):
        count = 0
        combine_string = ("").join(self._string.split())
        for char in combine_string:
            if char.isalpha():
                count += 1
        return count
    
    def count_consonants(self):
        return self._count_letters() - self.count_vowels()
    

# NOTE: Test Code
if __name__ == "__main__":
    print("What the Hell are you doing? \nThis is not the Main File.\nPlease run the main.py file.")