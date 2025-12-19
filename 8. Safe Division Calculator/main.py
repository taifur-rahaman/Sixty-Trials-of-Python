import utils

numbers = []
result = 0

while True:
    utils.beautify("calculator".title())
    choice = input("\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n0. Exit\nEnter Your Choice: ")

    match choice:
        case "1":
            print(f"\n\nResult: {utils.exception_handler("addition")}")
        case "2":
            print(f"\n\nResult: {utils.exception_handler("subtraction")}")
        case "3":
            print(f"\n\nResult: {utils.exception_handler("multiplication")}")
        case "4":
            print(f"\n\nResult: {utils.exception_handler("division")}")
        case "0":
            print("Exiting the program. GoodBye!!!")
            exit()
        case _:
            print("Invalid Input. Please Try Again.")