from utils import utils
from fileEditor import FileEditor

def usr_input():
    return input("Enter your Input: ")

while True:
    utils.beautify("File Editor")

    choice = input("\n"
                   "\n1. Write in File"
                   "\n2. Read from File"
                   "\n3. Delete the Contents"
                   "\n0. Exit"
                   "\nEnter Your Choice: ")

    match choice:
        case "1":
            FileEditor.write_file(usr_input())
        case "2":
            print(FileEditor.read_file())
        case "3":
            FileEditor.delete_content()
        case "0":
            print("\n\n"
                  "Thank You for using the Application\n"
                  "Goodbye!!!")
            exit()
        case _:
            print("\n\n"
                  "Invalid Choice\n"
                  "Please Try Again")