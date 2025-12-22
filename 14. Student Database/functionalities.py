from student import *
from utils import *

def store_in_dict():
    student_dict = {}
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split(",")
            student_dict[line[0]] = (line[1], line[2], line[3])
    return student_dict

def add_student():
    show_dict = {}
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    city = input("Enter city: ")

    try:
        Student(name, age, grade, city)
        show_dict[name] = (age, grade, city)
    except ValueError as e:
        raise e
    except TypeError as e:
        raise e
    except Exception as e:
        raise e
    else:
        print("Student added successfully")
    return show_dict

def search_student():
    name = input("Enter name: ")
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        for line in lines:
            if name in line:
                line = line.split(",")
                print(f"\nName: {line[0]}"
                      f"\nAge: {line[1]}"
                      f"\nGrade: {line[2]}"
                      f"\nCity: {line[3]}"
                      f"\n")

def delete_students():
    name = input("Enter Name: ")
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    with open(FILE_NAME, "w") as file:
        for line in lines:
            if name not in line:
                file.write(line)
    print("Student deleted successfully")

def view_students(student_dict):
    count = 1
    for key, value in student_dict.items():
        beautify(f"Student {count}")
        print(f"\nName: {key}")
        print(f"Age: {value[0]}")
        print(f"Grade: {value[1]}")
        print(f"City: {value[2]}\n")
        count += 1