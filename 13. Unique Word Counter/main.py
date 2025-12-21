import utils
import functionalities as func

while True:
    utils.beautify("Unique Word Counter")

    choice = input("\n"
                   "\n1. Enter List"
                   "\n2. Enter Tuple"
                   "\n3. Enter String"
                   "\n0. Exit"
                   "\nEnter Your Choice: ")

    match choice:
        case "1":
            func.list_input()
        case "2":
            func.tuple_list()
        case "3":
            func.string_input()
        case "0":
            print("Thank You for using the Application"
                  "\nGoodbye!!!")
            exit()
        case "_":
            print("Invalid Input"
                  "\nPlease Try Again")