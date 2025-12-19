
class Reverse:
    def __inti__(self):
        pass
    
    def reverse_words(self, string):
        return " ".join(reversed(string.split()))
    
    def reverse_letters(self, string):
        return "".join(reversed(string))
