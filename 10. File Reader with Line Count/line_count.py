import functionalities

FILE_NAME = "file.txt"

class LineCount:
    def __init__(self):
        pass

    @staticmethod
    def write_lines():
        try:
            with open(FILE_NAME, "a") as file:
                file.write(functionalities.usr_input())
        except FileExistsError as e:
            raise e

    @staticmethod
    def read_lines():
        try:
            with open(FILE_NAME, "r") as file:
                return file.read()
        except FileNotFoundError as e:
            raise e

    @staticmethod
    def count_lines():
        try:
            with open(FILE_NAME, "r") as file:
                return len(file.readlines())
        except FileNotFoundError as e:
            raise e

    @staticmethod
    def clear_file():
        try:
            with open(FILE_NAME, "w") as file:
                file.write("")
                print("File has been Cleared")
        except FileNotFoundError as e:
            raise e
