from abc import ABC, abstractmethod


# Abstract class
class Evaluation(ABC):

    @abstractmethod
    def calculate_grade(self):
        pass


# Base class
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Student class
class Student(Person, Evaluation):

    count = 0

    def __init__(self, name, age, roll_no, mark1, mark2, mark3):
        super().__init__(name, age)

        self.roll_no = roll_no
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

        Student.count = Student.count + 1

    # Static method
    @staticmethod
    def check_marks(mark):
        if mark >= 0 and mark <= 100:
            return True
        else:
            return False

    # Calculate total
    def total_marks(self):
        return self.mark1 + self.mark2 + self.mark3

    # Calculate average
    def average_marks(self):
        return self.total_marks() / 3

    # Grade calculation
    def calculate_grade(self):

        average = self.average_marks()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    # Display details
    def display(self):

        print("Name:", self.get_name())
        print("Age:", self.get_age())
        print("Roll Number:", self.roll_no)
        print("Marks:", self.mark1, self.mark2, self.mark3)
        print("Total Marks:", self.total_marks())
        print("Average:", round(self.average_marks(), 2))
        print("Grade:", self.calculate_grade())

    # Operator overloading
    def __lt__(self, other):

        return self.total_marks() > other.total_marks()

    # Class method
    @classmethod
    def show_count(cls):
        print("Total number of students:", cls.count)


# Sports class
class Sports:

    def __init__(self, sports_score):
        self.sports_score = sports_score

    def show_sports(self):
        print("Sports Score:", self.sports_score)


# Multiple inheritance
class Result(Student, Sports):

    def __init__(self, name, age, roll_no,
                 mark1, mark2, mark3, sports_score):

        Student.__init__(
            self, name, age, roll_no,
            mark1, mark2, mark3
        )

        Sports.__init__(self, sports_score)


# Main program

n = int(input("Enter number of students: "))

students = []


for i in range(n):

    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    roll_no = input("Enter roll number: ")

    # Enter marks
    while True:
        mark1 = float(input("Enter mark for subject 1: "))

        if Student.check_marks(mark1):
            break
        else:
            print("Enter marks between 0 and 100.")

    while True:
        mark2 = float(input("Enter mark for subject 2: "))

        if Student.check_marks(mark2):
            break
        else:
            print("Enter marks between 0 and 100.")

    while True:
        mark3 = float(input("Enter mark for subject 3: "))

        if Student.check_marks(mark3):
            break
        else:
            print("Enter marks between 0 and 100.")

    sports_score =int(input("Enter sports score: "))

    # Create object
    student = Result(
        name, age, roll_no,
        mark1, mark2, mark3,
        sports_score
    )

    # Add object to list
    students.append(student)


# Display student details

print("\n")
print("STUDENT DETAILS")
print("-------------------------")

for student in students:

    student.display()
    student.show_sports()

    print("-------------------------")


# Sort students based on total marks

students.sort()


# Display rank list

print("\n")
print("RANK LIST")
print("-----------------------------------------------")

for i in range(len(students)):

    student = students[i]

    print(
        "Rank:", i + 1,
        " Roll No:", student.roll_no,
        " Name:", student.get_name(),
        " Total:", student.total_marks(),
        " Average:", round(student.average_marks(), 2),
        " Grade:", student.calculate_grade()
    )


# Display total number of students

print("\n")
Student.show_count()