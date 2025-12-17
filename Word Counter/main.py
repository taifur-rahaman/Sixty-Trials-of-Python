from processor import Processor

string = input("Enter a String: ").casefold()

process = Processor(string)

while True:
    choice = input("1. Count Words\n2. Count Vowels\n3. Count Consonants\n0. Exit\nEnter your Choice: ")

    match choice:
        case "1":
            print(process.count_words())
        case "2":
            print(process.count_vowels())
        case "3":
            print(process.count_consonants())
        case "0":
            print("Thank You For Using the Application\nGoodBye!!!")
            exit()
        case _:
            print("Invalid Input. Please Try Again.")