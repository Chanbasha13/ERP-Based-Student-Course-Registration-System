import json

# ------------------ MODELS ------------------

class Course:
    def __init__(self, code, name, capacity):
        self.code = code
        self.name = name
        self.capacity = capacity
        self.enrolled = 0

    def has_seat(self):
        return self.enrolled < self.capacity

    def enroll(self):
        if self.has_seat():
            self.enrolled += 1
            return True
        return False

    def drop(self):
        if self.enrolled > 0:
            self.enrolled -= 1


class Student:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.courses = []

    def register(self, course):
        if course.code in self.courses:
            print("Already registered")
            return

        if course.enroll():
            self.courses.append(course.code)
            print("Registered successfully")
        else:
            print("Course full")

    def drop(self, course):
        if course.code in self.courses:
            self.courses.remove(course.code)
            course.drop()
            print("Dropped successfully")
        else:
            print("Not registered in this course")


# ------------------ DATA ------------------

courses = [
    Course("CS101", "Python", 2),
    Course("CS102", "DSA", 2),
    Course("CS103", "DBMS", 2)
]

students = {}

# ------------------ LOGIN SYSTEM ------------------

def login():
    print("\n1. Register\n2. Login")
    ch = input("Enter choice: ")

    if ch == "1":
        u = input("Create username: ")
        p = input("Create password: ")
        students[u] = Student(u, p)
        print("Account created")
        return students[u]

    elif ch == "2":
        u = input("Username: ")
        p = input("Password: ")

        if u in students and students[u].password == p:
            print("Login successful")
            return students[u]
        else:
            print("Invalid login")
            return None


# ------------------ STUDENT MENU ------------------

def student_menu(student):
    while True:
        print("\n--- STUDENT MENU ---")
        print("1. View Courses")
        print("2. Register Course")
        print("3. Drop Course")
        print("4. My Courses")
        print("5. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            for c in courses:
                print(c.code, c.name, f"Seats: {c.capacity - c.enrolled}")

        elif ch == "2":
            code = input("Enter course code: ")
            for c in courses:
                if c.code == code:
                    student.register(c)

        elif ch == "3":
            code = input("Enter course code to drop: ")
            for c in courses:
                if c.code == code:
                    student.drop(c)

        elif ch == "4":
            print("Your Courses:", student.courses)

        elif ch == "5":
            break


# ------------------ ADMIN MENU ------------------

def admin_menu():
    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. Add Course")
        print("2. View All Students")
        print("3. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            code = input("Course code: ")
            name = input("Course name: ")
            cap = int(input("Capacity: "))
            courses.append(Course(code, name, cap))
            print("Course added")

        elif ch == "2":
            for s in students.values():
                print(s.username, s.courses)

        elif ch == "3":
            break


# ------------------ MAIN ------------------

while True:
    print("\n==== ERP SYSTEM ====")
    print("1. Student Login")
    print("2. Admin")
    print("3. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        student = login()
        if student:
            student_menu(student)

    elif ch == "2":
        admin_menu()

    elif ch == "3":
        break