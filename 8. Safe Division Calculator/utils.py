from calculator import Operation

def beautify(string):
    print("="*40)
    print(string.center(40))
    print("="*40)

def usr_input():
    numbers = []
    qty = input("Enter how many number you want to enter: ")
    if int(qty) == 0:
        raise ValueError("Quantity cannot be zero.")
    elif int(qty) < 0:
        raise ValueError("Quantity cannot be negative.")
    for i in range(int(qty)):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(float(num))
    return numbers

def exception_handler(string):
    result = 0
    if string == "multiplication" or string == "division":
        result = 1
    beautify(string.title())
    try:
        try:
            numbers = usr_input()
        except ValueError as e:
            print(f"Value Error: {e}")
        else:
            result = getattr(Operation, string)(*numbers)
    except ValueError as e:
        print(f"Value Error: {e}")
        return "ERROR"
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return "ERROR"
    return result
