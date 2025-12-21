
from unique_word import UniqueWord

def string_input():
    usr_string = input("Enter the string: ")

    if UniqueWord.check_duplicate(usr_string):
        print("String Contains Duplicate Elements")
        return
    else:
        print(f"Total Unique Letters: {UniqueWord.count_unique_word(usr_string)}")

def tuple_list():
    usr_tuple = sorted(tuple(input("Enter the elements separate by space: ").split()))

    if UniqueWord.check_duplicate(usr_tuple):
        print("Tuple Contains Duplicate Elements")
        return
    else:
        print(f"Total Unique Words: {UniqueWord.count_unique_word(usr_tuple)}")

def list_input():
    usr_list = []
    n = int(input("Enter Number of Elements: "))

    for i in range(n):
        usr_list.append(input(f"Enter Element {i+1}: "))

    if UniqueWord.check_duplicate(usr_list):
        print("List Contains Duplicate Elements")
        return
    else:
        print(f"Total Unique Words: {UniqueWord.count_unique_word(usr_list)}")
