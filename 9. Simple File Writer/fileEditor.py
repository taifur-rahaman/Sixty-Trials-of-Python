
FILE_NAME = "file.txt"

class FileEditor:
    def __init__(self):
        pass

    @staticmethod
    def write_file(string):
        with open(FILE_NAME, "a") as file:
            file.write(string + "\n")

    @staticmethod
    def read_file():
        with open(FILE_NAME, "r") as file:
            return file.read()

    @staticmethod
    def delete_content():
        with open(FILE_NAME, "w") as file:
            pass

if __name__ == "__main__":
    FileEditor.delete_content()
    FileEditor.write_file("Hello World")
    print(FileEditor.read_file())
    FileEditor.write_file("Hello World the second time")
    print(FileEditor.read_file())
