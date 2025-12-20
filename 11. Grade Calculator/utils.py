from students import Student

def beautify(string):
    print("="*40)
    print(string.center(40))
    print("="*40)

def add_student():
    Student(input("Enter Your Name: "))

def display_students():
    count = 0
    with open("students.txt", "r") as file:
        students = file.readlines()
    if not students:
        print("No Students Found")
        return
    else:
        for student in students:
            student = student.strip()
            count += 1
            student = student.split(", ")
            beautify(f"Student : {count}")
            print(f"\nName: {student[0]}"
                  f"\nID: {student[1]}"
                  f"\nHighest Score: {student[2]}"
                  f"\nLowest Score: {student[3]}"
                  f"\nAverage Score: {student[4]}")