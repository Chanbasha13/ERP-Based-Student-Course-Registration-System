# WEEK 6 - OOP
# Student class

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def register(self, course):
        self.courses.append(course)

    def show(self):
        print("Name:", self.name)
        print("Courses:", self.courses)

s = Student("Chan")
s.register("Python")
s.show()