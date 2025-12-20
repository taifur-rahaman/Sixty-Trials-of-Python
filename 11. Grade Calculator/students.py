import uuid

FILE_NAME = "students.txt"

class Student:
    def __init__(self, student_name="John Doe"):
        self._student_name = student_name
        self._student_id_generator()
        self.std_scores = []
        self.scores()
        self.save_to_file()

    def _student_id_generator(self):
        self._student_id = str(uuid.uuid4())

    def scores(self):
        sub_qty = input(f"Student: {self._student_name}, "
                        "\nEnter How many subjects scores you want to enter: ")
        for i in range(int(sub_qty)):
            score = float(input("Enter score: "))
            if score < 0:
                print("Score cannot be negative")
                continue
            elif score > 100:
                print("Score cannot be greater than 100")
                continue
            self.std_scores.append(score)

    def __str__(self):
        return (f"Student Name: {self._student_name},"
                f"\nStudent ID: {self._student_id},"
                f"\nHighest Score : {max(self.std_scores)}"
                f"\nLowest Score : {min(self.std_scores)}"
                f"\nAverage Score : {sum(self.std_scores) / len(self.std_scores)}")

    def save_to_file(self):
        with open(FILE_NAME, "a") as file:
            file.write(f"{self._student_name}, {self._student_id}, {max(self.std_scores)}, {min(self.std_scores)}, {sum(self.std_scores) / len(self.std_scores)}\n")





