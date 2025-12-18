from formatter import Formatter

print("="*40)
print("Name Formatter".center(40))
print("="*40)

name = Formatter()

name.first_name = input("Enter Your First Name: ").title()
name.last_name = input("Enter Your Last Name: ").title()

print("="*40)
print(name)
print("="*40)