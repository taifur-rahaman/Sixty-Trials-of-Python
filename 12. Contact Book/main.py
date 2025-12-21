import functionalities as func
from contact import Contact

contacts = func.store_from_file()

while True:
    func.beautify("Contact Book")

    print("\n1. Add Contact"
          "\n2. Show Contact"
          "\n3. Delete Contact"
          "\n4. Update Contact"
          "\n5. Search Contact"
          "\n0. Exit")

    choice = input("Enter Your Choice: ")

    match choice:
        case "1":
            name, phone = func.add_contact()
            try:
                Contact(name, phone)
            except ValueError as e:
                print(e)
            else:
                contacts[name] = phone
        case "2":
            func.show_contact(contacts)
        case "3":
            func.delete_contact(contacts)
        case "4":
            func.update_contact(contacts)
        case "5":
            func.search_contact(contacts)
        case "0":
            print("Thank You for Using the Application"
                  "\nGoodbye!!!")
            exit()
        case _:
            print("Invalid Choice"
                  "\nPlease Try Again.")