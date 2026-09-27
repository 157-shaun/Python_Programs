import copy

try:
    n = int(input("Enter the number of students: "))

    if n <= 0:
        raise ValueError("Invalid number of students")

    names = []
    roll_numbers = []
    marks = []

    for i in range(n):
        print("\nStudent", i + 1)

        name = input("Enter Name: ")
        roll = int(input("Enter Roll Number: "))

        m1 = int(input("Enter Mark 1: "))
        m2 = int(input("Enter Mark 2: "))
        m3 = int(input("Enter Mark 3: "))

        names.append(name)
        roll_numbers.append(roll)
        marks.append([m1, m2, m3])

    # Dictionary using zip()
    student_dict = dict(zip(names, roll_numbers))
    print("Dictionary:", student_dict)

    # String operations
    upper_names = [name.upper() for name in names]
    print("Uppercase names:", upper_names)

    long_names = [name for name in names if len(name) > 5]
    print("Names longer than 5 characters:", long_names)

    counts = sum(name.upper().startswith("A") for name in names)
    print("Names starting with A:", counts)

    # List comprehension
    high_average = [
        names[i]
        for i in range(n)
        if sum(marks[i]) / 3 > 75
    ]
    print("Students with average > 75:", high_average)

    even_rolls = [roll for roll in roll_numbers if roll % 2 == 0]
    print("Even roll numbers:", even_rolls)

    # Tuple
    first_marks = tuple(marks[0])
    print("First student's marks as tuple:", first_marks)

    # Set
    unique_marks = set()
    for student_marks in marks:
        unique_marks.update(student_marks)

    print("Unique marks:", unique_marks)

    # Shallow and deep copy
    shallow_copy = copy.copy(marks)
    deep_copy = copy.deepcopy(marks)

    # Modify original list
    marks[0][0] = 100

    print("\nOriginal marks:", marks)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep_copy)

except ValueError:
    print("Invalid input. Please enter numeric values where required.")

except Exception as e:
    print("Unexpected error:", e)