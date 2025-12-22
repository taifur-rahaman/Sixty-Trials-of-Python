from utils import *
from functionalities import *

student_dict = store_in_dict()
show_dict = student_dict.copy()

while True:
    beautify("Student Database")

    choice = input("\n"
                       "\n1. Add Student"
                       "\n2. Search Student"
                       "\n3. Delete Student"
                       "\n4. List All Students"
                       "\n0. Exit"
                       "\n\nEnter your choice: ")

    match choice:
        case "1":
            show_dict.update(add_student())
        case "2":
            search_student()
        case "3":
            delete_students()
        case "4":
            view_students(show_dict)
        case "0":
            print("Thank You for Using the Application"
                  "\nGoodbye!!!")
            exit()
        case _:
            print("Invalid Input"
                  "\nPlease Try Again")