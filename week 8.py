# WEEK 8 - File Handling
# Save student data

with open("student.txt", "w") as file:
    file.write("Chan\n")
    file.write("Python")

print("Data Saved Successfully")