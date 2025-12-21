import re

FILE_NAME = "contact.txt"


class Contact:
    def __init__(self, user_name = "John Doe", user_phone = "+8801234567890"):
        self._usr_name = user_name
        self._usr_phone = self._phone_validity(user_phone)
        self._save_on_file()

    @staticmethod
    def _phone_validity(user_phone):
        pattern = r"^\+8801?[3,4,5,6,7,8,9]{1}[\d]{8}$"
        if re.match(pattern, user_phone):
            return user_phone
        else:
            raise ValueError("Invalid Phone Number")

    def _save_on_file(self):
        with open(FILE_NAME, "a") as file:
            file.write(f"{self._usr_name},{self._usr_phone}\n")

    def __str__(self):
        return (f"\nName: {self._usr_name}"
                f"\nPhone: {self._usr_phone}")

if __name__ == "__main__":
    contact = Contact("Taifur Rahaman", "+8801777620949")