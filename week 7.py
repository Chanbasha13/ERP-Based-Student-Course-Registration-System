# WEEK 7 - Validation
# Duplicate registration checking

registered = ["Python", "DSA"]

course = input("Enter course name: ")

if course in registered:
    print("Already Registered")
else:
    registered.append(course)
    print("Registered Successfully")