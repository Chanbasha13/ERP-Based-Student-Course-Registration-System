def capture_lost_item():
    print("Enter Lost Item Details")

    name = input("Item Name: ")
    description = input("Description: ")
    location = input("Location Lost: ")
    date = input("Date Lost: ")
    contact = input("Contact Number: ")

    item = {
        "name": name,
        "description": description,
        "location": location,
        "date": date,
        "contact": contact
    }

    return item

    def display_item(item):
        print("\nLost Item Recorded Successfully")

    print("Item Name:", item["name"])
    print("Description:", item["description"])
    print("Location:", item["location"])
    print("Date Lost:", item["date"])
    print("Contact:", item["contact"])

    if __name__ == "__main__":
        lost_item = capture_lost_item()
        display_item(lost_item)

    lost_items = []


found_items = []


def add_lost_item():
    name = input("Item Name: ")
    description = input("Description: ")
    location = input("Location Lost: ")
    date = input("Date Lost: ")
    contact = input("Contact: ")

    item = {
        "type": "lost",
        "name": name,
        "description": description,
        "location": location,
        "date": date,
        "contact": contact
    }

    lost_items.append(item)
    print("Lost item added successfully")


def add_found_item():
    name = input("Item Name: ")
    description = input("Description: ")
    location = input("Location Found: ")
    date = input("Date Found: ")
    contact = input("Contact: ")

    item = {
        "type": "found",
        "name": name,
        "description": description,
        "location": location,
        "date": date,
        "contact": contact
    }

    found_items.append(item)
    print("Found item added successfully")


def search_items():
    keyword = input("Enter item name to search: ").lower()

    print("\nSearch Results:")

    found = False

    for item in lost_items + found_items:
        if keyword in item["name"].lower():
            print(item)
            found = True

    if not found:
        print("No matching items found")


def menu():
    while True:
        print("\nLIL CAMP MENU")
        print("1 Add Lost Item")
        print("2 Add Found Item")
        print("3 Search Items")
        print("4 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_lost_item()
        elif choice == "2":
            add_found_item()
        elif choice == "3":
            search_items()
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()

# WEEK 3 – Strings & Lists

lost_items = []
found_items = []


def clean_input(text):
    return text.strip().lower()


def add_item(item_type):
    name = clean_input(input("Item Name: "))
    description = input("Description: ").strip()
    location = input("Location: ").strip()
    date = input("Date: ").strip()
    contact = input("Contact: ").strip()

    item = {
        "type": item_type,
        "name": name,
        "description": description,
        "location": location,
        "date": date,
        "contact": contact
    }

    if item_type == "lost":
        lost_items.append(item)
    else:
        found_items.append(item)

    print("Item added successfully")


def list_items():
    print("\nLost Items:")
    for item in lost_items:
        print(item)

    print("\nFound Items:")
    for item in found_items:
        print(item)


def search_items():
    keyword = clean_input(input("Search by name: "))
    found = False

    for item in lost_items + found_items:
        if keyword in item["name"]:
            print(item)
            found = True

    if not found:
        print("No items found")


def menu():
    while True:
        print("\n1 Add Lost Item")
        print("2 Add Found Item")
        print("3 List Items")
        print("4 Search Items")
        print("5 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_item("lost")
        elif choice == "2":
            add_item("found")
        elif choice == "3":
            list_items()
        elif choice == "4":
            search_items()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()

    # WEEK 4 – Functional Architecture

lost_items = []
found_items = []


def add_lost_item():
    add_item("lost")


def add_found_item():
    add_item("found")


def add_item(item_type):
    item = {
        "name": input("Item Name: "),
        "description": input("Description: "),
        "location": input("Location: "),
        "date": input("Date: "),
        "contact": input("Contact: "),
        "type": item_type
    }

    if item_type == "lost":
        lost_items.append(item)
    else:
        found_items.append(item)

    print("Item added successfully")


def search_item():
    keyword = input("Enter name: ").lower()
    found = False

    for item in lost_items + found_items:
        if keyword in item["name"].lower():
            print(item)
            found = True

    if not found:
        print("No matching items found")


def list_items():
    print("\nAll Items:")
    for item in lost_items + found_items:
        print(item)


def menu():
    while True:
        print("\n1 Add Lost Item")
        print("2 Add Found Item")
        print("3 Search Item")
        print("4 List Items")
        print("5 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_lost_item()
        elif choice == "2":
            add_found_item()
        elif choice == "3":
            search_item()
        elif choice == "4":
            list_items()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()

    # WEEK 5 – Dictionaries & Sets

lost_items = []
found_items = []


def create_item():
    item = {
        "item_name": input("Item Name: "),
        "description": input("Description: "),
        "location": input("Location: "),
        "date": input("Date: "),
        "contact": input("Contact: ")
    }
    return item


def add_lost_item():
    item = create_item()
    lost_items.append(item)
    print("Lost item added successfully")


def add_found_item():
    item = create_item()
    found_items.append(item)
    print("Found item added successfully")


def list_items():
    print("\nLost Items:")
    for item in lost_items:
        print(item)

    print("\nFound Items:")
    for item in found_items:
        print(item)


if __name__ == "__main__":
    add_lost_item()
    add_found_item()
    list_items()


# WEEK 6 – OOP: Item Class

class Item:

    def __init__(self, item_name, description, location, date, contact):
        self.item_name = item_name
        self.description = description
        self.location = location
        self.date = date
        self.contact = contact

    def display(self):
        print("Item Name:", self.item_name)
        print("Description:", self.description)
        print("Location:", self.location)
        print("Date:", self.date)
        print("Contact:", self.contact)

    def to_dict(self):
        return {
            "item_name": self.item_name,
            "description": self.description,
            "location": self.location,
            "date": self.date,
            "contact": self.contact
        }

    # WEEK 7 – Inheritance & Encapsulation


class BaseRecord:

    def __init__(self, record_id):
        self._record_id = record_id

    def get_record_id(self):
        return self._record_id


class Item(BaseRecord):

    def __init__(self, record_id, item_name, description, location, date, contact):
        super().__init__(record_id)
        self.item_name = item_name
        self.description = description
        self.location = location
        self.date = date
        self.contact = contact

    def display(self):
        print("Record ID:", self.get_record_id())
        print("Item Name:", self.item_name)
        print("Description:", self.description)
        print("Location:", self.location)
        print("Date:", self.date)
        print("Contact:", self.contact)
    # WEEK 8 – File Handling (CSV + JSON)


import json
import csv
import os


class JsonStore:

    def __init__(self):
        self.lost_file = "data/lost_items.json"
        self.found_file = "data/found_items.json"
        self.backup_file = "data/backup.csv"

        if not os.path.exists("data"):
            os.makedirs("data")

    def save_lost_items(self, lost_items):
        try:
            with open(self.lost_file, "w") as file:
                json.dump(lost_items, file, indent=4)
            print("Lost items saved")
        except:
            print("Error saving lost items")

    def save_found_items(self, found_items):
        try:
            with open(self.found_file, "w") as file:
                json.dump(found_items, file, indent=4)
            print("Found items saved")
        except:
            print("Error saving found items")

    def load_lost_items(self):
        try:
            if not os.path.exists(self.lost_file):
                return []
            with open(self.lost_file, "r") as file:
                return json.load(file)
        except:
            print("Error loading lost items")
            return []

    def load_found_items(self):
        try:
            if not os.path.exists(self.found_file):
                return []
            with open(self.found_file, "r") as file:
                return json.load(file)
        except:
            print("Error loading found items")
            return []

    def backup_to_csv(self, all_items):
        try:
            with open(self.backup_file, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow([
                    "type",
                    "item_name",
                    "description",
                    "location",
                    "date",
                    "contact"
                ])

                for item in all_items:
                    writer.writerow([
                        item.get("type"),
                        item.get("item_name"),
                        item.get("description"),
                        item.get("location"),
                        item.get("date"),
                        item.get("contact")
                    ])

            print("Backup created successfully")

        except:
            print("Error creating backup")

    # WEEK 9 – Multi-Module Integration


from storage.json_store import JsonStore

store = JsonStore()

lost_items = store.load_lost_items()
found_items = store.load_found_items()


def add_lost_item():
    item = {
        "type": "lost",
        "item_name": input("Item Name: "),
        "description": input("Description: "),
        "location": input("Location: "),
        "date": input("Date: "),
        "contact": input("Contact: ")
    }

    lost_items.append(item)
    store.save_lost_items(lost_items)


def add_found_item():
    item = {
        "type": "found",
        "item_name": input("Item Name: "),
        "description": input("Description: "),
        "location": input("Location: "),
        "date": input("Date: "),
        "contact": input("Contact: ")
    }

    found_items.append(item)
    store.save_found_items(found_items)


def list_items():
    print("\nLost Items:")
    for item in lost_items:
        print(item)

    print("\nFound Items:")
    for item in found_items:
        print(item)


def backup():
    all_items = lost_items + found_items
    store.backup_to_csv(all_items)


def menu():
    while True:
        print("\nLIL CAMP SYSTEM")
        print("1 Add Lost Item")
        print("2 Add Found Item")
        print("3 List Items")
        print("4 Backup Data")
        print("5 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_lost_item()
        elif choice == "2":
            add_found_item()
        elif choice == "3":
            list_items()
        elif choice == "4":
            backup()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()

    # WEEK 10 – Validators with Exception Handling


def validate_item_name(name):
    try:
        if not name.strip():
            raise ValueError("Item name cannot be empty")
        return name
    except Exception as e:
        print("Error:", e)
        return None


def validate_category(category):
    valid_categories = ["Documents", "Electronics", "Accessories", "Books"]

    try:
        if category not in valid_categories:
            raise ValueError("Invalid category")
        return category
    except Exception as e:
        print("Error:", e)
        return None


def validate_contact(contact):
    try:
        if len(contact) != 10 or not contact.isdigit():
            raise ValueError("Contact must be 10 digits")
        return contact
    except Exception as e:
        print("Error:", e)
        return None


def validate_date(date):
    try:
        parts = date.split("-")
        if len(parts) != 3:
            raise ValueError("Date must be in YYYY-MM-DD format")
        year, month, day = parts

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            raise ValueError("Date must contain numbers only")

        return date
    except Exception as e:
        print("Error:", e)
        return None

    # Example test


if __name__ == "__main__":
    print(validate_item_name("Wallet"))
    print(validate_category("Electronics"))
    print(validate_contact("9876543210"))
    print(validate_date("2026-04-10"))

    # WEEK 11 – Simple Analytics using Pandas & NumPy

import pandas as pd
import numpy as np

# Sample data (you can replace with CSV later)
data = [
    {"item": "Wallet", "category": "Accessories", "status": "lost"},
    {"item": "Phone", "category": "Electronics", "status": "found"},
    {"item": "ID Card", "category": "Documents", "status": "lost"},
    {"item": "Book", "category": "Books", "status": "found"},
    {"item": "Calculator", "category": "Electronics", "status": "lost"},
]

# Convert to DataFrame
df = pd.DataFrame(data)


# 1. Count lost items
def count_lost_items():
    lost_count = np.sum(df["status"] == "lost")
    print("Total Lost Items:", lost_count)

    # 2. Count found items
    def count_found_items():
        found_count = np.sum(df["status"] == "found")

    print("Total Found Items:", found_count)

    # 3. Category-wise count


def category_wise():
    print("\nCategory Wise Count:")
    print(df["category"].value_counts())

    # 4. Recovery Rate


def recovery_rate():
    total = len(df)
    found = np.sum(df["status"] == "found")
    rate = (found / total) * 100
    print("\nRecovery Rate:", rate, "%")

    # Run all


if __name__ == "__main__":
    count_lost_items()
    count_found_items()
    category_wise()
    recovery_rate()

    # WEEK 12 – Visualization using Matplotlib

import matplotlib.pyplot as plt

# Sample data
categories = ["Documents", "Electronics", "Accessories", "Books"]
counts = [5, 8, 3, 4]

status_labels = ["Recovered", "Not Recovered"]
status_counts = [10, 10]


# 1. Bar Chart (Category Wise)
def plot_category_chart():
    plt.figure()
    plt.bar(categories, counts)
    plt.title("Lost Items by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Items")
    plt.show()

    # 2. Pie Chart (Recovery Status)


def plot_recovery_pie():
    plt.figure()
    plt.pie(status_counts, labels=status_labels, autopct='%1.1f%%')
    plt.title("Recovery Status")
    plt.show()

    # 3. Line Graph (Example Trend)


def plot_trend():
    days = [1, 2, 3, 4, 5]
    lost_items = [2, 4, 3, 5, 6]

    plt.figure()
    plt.plot(days, lost_items, marker='o')
    plt.title("Lost Items Trend")
    plt.xlabel("Days")
    plt.ylabel("Items Lost")
    plt.show()

    # Run all charts


if __name__ == "__main__":
    plot_category_chart()
    plot_recovery_pie()
    plot_trend()