# WEEK 12 - Matplotlib
# Graph visualization

import matplotlib.pyplot as plt

courses = ["Python", "DSA", "DBMS"]
students = [50, 40, 35]

plt.bar(courses, students)
plt.title("Course Enrollment")
plt.xlabel("Courses")
plt.ylabel("Students")
plt.show()