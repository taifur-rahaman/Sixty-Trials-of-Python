from line_count import LineCount
import functionalities

while True:
    functionalities.beautify("File Reader with Line Count")

    choice = input("\n"
                   "\n1. Write to file"
                   "\n2. Read from file"
                   "\n3. Count lines"
                   "\n4. Clear File"
                   "\n0. Exit"
                   "\n\nEnter your choice: ")

    match choice:
        case "1":
            LineCount.write_lines()
        case "2":
            print(LineCount.read_lines())
        case "3":
            print(f"Number of lines: {LineCount.count_lines()}")
        case "4":
            LineCount.clear_file()
        case "0":
            print("\n"
                  "Thank You for Using the Application\n"
                  "Goodbye!!!")
            exit()
        case _:
            print("Invalid Input.\n"
                  "Please Try Again")