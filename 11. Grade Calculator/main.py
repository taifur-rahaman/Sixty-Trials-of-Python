import utils

while True:
    utils.beautify("Grade Calculator")

    choice = input("\n"
                   "\n1. Add Student"
                   "\n2. View Students"
                   "\n0. Exit"
                   "\nEnter Your Choice: ")

    match choice:
        case "1":
            utils.add_student()
        case "2":
            utils.display_students()
        case "0":
            print("Thank You for using the Application"
                  "\nGoodbye!!!")
            exit()
        case _:
            print("Invalid Input."
                  "\nPlease Try Again")