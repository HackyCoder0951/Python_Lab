# Q 3.7 - Write a Python program to make a list of students along with their marks using class.

class Student:
    """
    Represents a student with a name and marks.
    """
    def __init__(self, name, marks):
        """
        Initializes a student with a name and marks.

        Args:
            name (str): The name of the student.
            marks (float): The marks of the student.
        """
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


class StudentList:
    """
    Represents a list of students.
    """
    def __init__(self):
        """
        Initializes an empty list of students.
        """
        self.students = []

    def add_student(self, name, marks):
        """
        Adds a student to the list.

        Args:
            name (str): The name of the student.
            marks (float): The marks of the student.
        """
        student = Student(name, marks)
        self.students.append(student)

    def display_students(self):
        for i, student in enumerate(self.students, start=1):
            print(f"\nStudent {i}:")
            student.display()


def main():
    student_list = StudentList()

    while True:
        print("\nStudent List")
        print("1. Add student")
        print("2. Display students")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            name = input("\nEnter student name: ")
            marks = float(input("Enter student marks: "))
            student_list.add_student(name, marks)

        elif choice == "2":
            print("\nStudents:")
            student_list.display_students()

        elif choice == "3":
            break

        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()