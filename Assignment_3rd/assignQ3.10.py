# Q 3.10 - Write a Python program using multilevel inheritance to implement student admission in
    # MCA course and display the result by assuming Student as base class. 
    # MCA is derived from Student.
    # Result is derived from MCA. 
    # Choose appropriate properties and methods to be included in the above classes.

class Student:
    # Represents a student with a name, roll number, and course.
    def __init__(self, name, roll_number, course):
        """
        Initializes a student with a name, roll number, and course.

        Args:
            name (str): The name of the student.
            roll_number (int): The roll number of the student.
            course (str): The course of the student.
        """
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display_student(self):
        # Displays the student's details.
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Course: {self.course}")


class MCA(Student):
    # Represents an MCA student with a specialization and semester.
    def __init__(self, name, roll_number, course, specialization, semester):
        """
        Initializes an MCA student with a name, roll number, course, specialization, and semester.

        Args:
            name (str): The name of the student.
            roll_number (int): The roll number of the student.
            course (str): The course of the student.
            specialization (str): The specialization of the student.
            semester (int): The semester of the student.
        """
        super().__init__(name, roll_number, course)
        self.specialization = specialization
        self.semester = semester

    def display_mca(self):
        # Displays the MCA student's details.
        self.display_student()
        print(f"Specialization: {self.specialization}")
        print(f"Semester: {self.semester}")


class Result(MCA):
    # Represents an MCA student's result with marks and grade.
    def __init__(self, name, roll_number, course, specialization, semester, marks, grade):
        """
        Initializes an MCA student's result with a name, roll number, course, specialization, semester, marks, and grade.

        Args:
            name (str): The name of the student.
            roll_number (int): The roll number of the student.
            course (str): The course of the student.
            specialization (str): The specialization of the student.
            semester (int): The semester of the student.
            marks (float): The marks of the student.
            grade (str): The grade of the student.
        """
        super().__init__(name, roll_number, course, specialization, semester)
        self.marks = marks
        self.grade = grade

    def display_result(self):
        # Displays the MCA student's result.
        self.display_mca()
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")


def main():
    name = input("Enter student name: ")
    roll_number = int(input("Enter student roll number: "))
    course = input("Enter student course: ")
    specialization = input("Enter student specialization: ")
    semester = int(input("Enter student semester: "))
    marks = float(input("Enter student marks: "))
    grade = input("Enter student grade: ")

    result = Result(name, roll_number, course, specialization, semester, marks, grade)
    result.display_result()


if __name__ == "__main__":
    main()