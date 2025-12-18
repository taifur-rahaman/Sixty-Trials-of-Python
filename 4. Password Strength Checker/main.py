from validator import Validator

print("="*40)
print("Password Strength Checker".center(40))
print("="*40)

while True:
    password = input("Enter a Password: ")
    validator = Validator(password)
    if validator.is_valid():
        print("Password is Valid.\n")
    else:
        print("Password is Invalid.\n")
    
    choice = input("Do you want to check any more Passwords? (y/n): ").casefold()
    if choice == "n":
        print("Thank You for Using this Program\nGoodBye!!!")
        break