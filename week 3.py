# WEEK 3 - Lists and Search
# Course list management

courses = ["Python", "DSA", "DBMS", "OS"]

search = input("Enter course name: ")

for course in courses:
    if search.lower() == course.lower():
        print("Course Found:", course)