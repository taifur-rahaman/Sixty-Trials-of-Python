
class Count:
    def __init__(self):
        pass

    @staticmethod
    def count_words(string):
        count_dict = {}
        temp_string = tuple(string.split())
        for word in temp_string:
            count_dict[word] = temp_string.count(word)
        print(count_dict)


if __name__ == "__main__":
    Count.count_words("Hello World, How are you? Are you here to capture me? Are you insane?")
