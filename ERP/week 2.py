# WEEK 2 - Menu Using Loop
# Basic menu driven system

while True:
    print("\n1. View Courses")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Courses Available")
    elif choice == "2":
        print("Exiting...")
        break
    else:
        print("Invalid Choice")