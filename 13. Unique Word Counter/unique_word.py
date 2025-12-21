
class UniqueWord:
    def __init__(self):
        pass

    @staticmethod
    def check_duplicate(iterable):
        if sorted(tuple(set(iterable))) == sorted(tuple(iterable)):
            return False
        return True

    @staticmethod
    def count_unique_word(iterable):
        if isinstance(iterable, str):
            return len(list(iterable))
        return len(iterable)
