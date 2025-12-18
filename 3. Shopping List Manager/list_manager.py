def file_add(item):
    with open("list.txt", "a") as file:
        file.write(f"{item}\n")

def file_read():
    with open("list.txt", "r") as file:
        return file.read().splitlines()

def file_delete_item():
    items = []
    with open("list.txt", "r") as file:
        items = file.readlines()
    
    item = input("Enter the name of the item to delete: ").casefold()
    item = item + "\n"
    
    try:
        if item in items:
            items.remove(item)
    except ValueError:
        raise ValueError("Item not found in the list.")
    else:
        with open("list.txt", "w") as file:
            for item in items:
                file.write(item)


def add_item():
    item = input("Enter the name of the item to add: ")
    print(f"{item} has been successfully added to the list.")
    file_add(item.casefold())
    return item

def display():
    items = file_read()
    print("Shopping List\n")
    for item in items:
        print(f"- {item.title()}")