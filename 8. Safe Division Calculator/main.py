
from calculator import Operation

def beautify(string):
    print("="*40)
    print(string.center(40))
    print("="*40)

beautify("Calculator")

operation = Operation()
while True:
    choice = input("\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. "
                   "Division\n0. Exit\nEnter Your Choice: ")
    
    match choice:
        case "1":
            beautify("Addition")
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "0":
            print("Exiting the program. GoodBye!!!")
            exit()
        case _:
            print("Invalid Input. Please Try Again.")