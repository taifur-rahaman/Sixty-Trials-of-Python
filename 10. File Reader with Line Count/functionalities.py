
def usr_input():
    lines = input("Enter your Input: ")
    if lines == "":
        raise ValueError("Input cannot be empty")
    return lines + "\n"

def beautify(string):
    print("="*40)
    print(string.center(40))
    print("="*40)