FILE_NAME = "student.txt"


class Student:
    def __init__(self, name, age, grade, city):
        self._name = name
        self._age = self._age_verify(age)
        self._grade = self._grade_verify(grade)
        self._city = city
        self._save_on_file()

    @staticmethod
    def _age_verify(age):
        if 12 <= age <= 30:
            return age
        else:
            raise ValueError("Age must be between 12 and 30")

    @staticmethod
    def _grade_verify(grade):
        if 'a' <= grade.casefold() <= 'f':
            return grade
        else:
            raise ValueError("Grade must be between A and F")

    def _save_on_file(self):
        with open(FILE_NAME, "a") as file:
            file.write(f"{self._name},{self._age},{self._grade},{self._city}\n")
