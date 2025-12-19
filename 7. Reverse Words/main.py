
from reverse import Reverse

print("="*40)
print("Reversy".center(40))
print("="*40)

while True:
    choice = input("\n\n1. Enter a New String\n0. Exit\nEnter your Choice: ")
    if choice == "1":
        string = input("Enter a String: ").casefold()
        reverse = Reverse()
    elif choice == "0":
        print("Exiting the program.\nGoodbye!")
        exit()
        
    while True:
        choice = input("\n\n1. Reverse Words\n2. Reverse Letters\n0. Main Menu\nEnter your Choice: ")

        match choice:
            case "1":
                print(reverse.reverse_words(string).title())
            case "2":
                print(reverse.reverse_letters(string).title())
            case "0":
                break
            case _:
                print("Invalid Choice. Please Try Again.\n")
    

