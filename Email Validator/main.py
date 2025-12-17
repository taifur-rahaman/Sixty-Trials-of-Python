from validator import Validator

email = input("Enter your email: ")
validator = Validator(email)
if validator.is_valid():
    print("Your mail is Valid email")
else:
    print("Your mail is Invalid email")