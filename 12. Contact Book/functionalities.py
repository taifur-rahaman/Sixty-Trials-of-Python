from contact import Contact

FILE_NAME = "contact.txt"

def beautify(text):
    print("="*40)
    print(text.center(40))
    print("="*40)

def add_contact():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone Number: ")
    return name, phone

def store_from_file():
    contacts = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        with open(FILE_NAME, "w") as file:
            pass
    else:
        return contacts

def show_contact(contacts):
    beautify("Contact List")
    for name, phone in contacts.items():
        print("\n")
        print("-" * 40)
        print(f"Name: {name}".center(40))
        print(f"Phone: {phone}".center(40))
        print("-" * 40)

def delete_contact(contacts):
    name = input("Enter the contact Name you want to delete: ")
    try:
        del contacts[name]
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        with open(FILE_NAME,"w") as file:
            for line in lines:
                if name not in line:
                    file.write(line)
    except KeyError:
        print("Contact Not Found")
    else:
        print("Contact Deleted Successfully")

def update_contact(contacts):
    try:
        name = input("Enter the contact Name you want to update: ")
        phone = input("Enter the contact Phone you want to update: ")
        contacts[name] = phone
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        with open(FILE_NAME,"w") as file:
            for line in lines:
                if name not in line:
                    file.write(line)
        Contact(name, phone)
    except KeyError:
        print("Contact Not Found")
    else:
        print("Contact Updated Successfully")

def search_contact(contacts):
    name = input("Enter the contact Name you want to search: ")
    try:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]}")
    except KeyError:
        print("Contact Not Found")