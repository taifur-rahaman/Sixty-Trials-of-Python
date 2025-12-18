import list_manager as listManager


items = []

try:
    with open("list.txt", "r") as file:
        for item in file.readlines():
            items.append(item.strip())
except FileNotFoundError:
    with open("list.txt", "w"):
        pass

while True:
    print("\n" + "="*40)
    print("SHOPPING LIST")
    print("="*40)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("0. Exit")
    print("="*40)
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            items.append(listManager.add_item())
        case "2":
            listManager.file_delete_item()
        case "3":
            listManager.display()
        case "0":
            print("Thank You for using the Application\nGoodbye!!!")
            exit()
        case _:
            print("Invalid Input. Please Try Again.")