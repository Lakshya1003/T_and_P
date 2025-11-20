#This is my 2nd Tnp Assignment
#===========================================================================================
#Verdict is to create a Student registration system with the Functionalities of Registration, Login, Profile view and profile update.

#==========================================================================================

import json

# ===============================
# Utility Functions
# ===============================

def load_data():
    "Load student data from JSON file"
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    """Save student data to JSON file"""
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

# ===============================
# Core Functionalities
# ===============================

def register():
    data = load_data()
    username = input("\nEnter username: ")

    if username in data:
        print("Username already exists! Try a different one.")
        return

    password = input("Enter password: ")
    name = input("Enter full name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    course = input("Enter course: ")
    year = input("Enter year: ")
    address = input("Enter address: ")
    rollno = input("Enter roll number: ")

    data[username] = {
        "password": password,
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "course": course,
        "year": year,
        "address": address,
        "rollno": rollno
    }

    save_data(data)
    print("\n Registration Successful!\n")

def login():
    data = load_data()
    username = input("\nEnter username: ")
    password = input("Enter password: ")

    if username in data and data[username]["password"] == password:
        print(f"\n Welcome, {data[username]['name']}!\n")
        dashboard(username)
    else:
        print("\n Invalid credentials! Please try again.\n")

def show_profile(username):
    data = load_data()
    user = data[username]
    print("\n----- Your Profile -----")
    for key, value in user.items():
        if key != "password":
            print(f"{key.capitalize()}: {value}")
    print("------------------------\n")

def update_profile(username):
    data = load_data()
    user = data[username]

    print("\nWhich field do you want to update?")
    for i, key in enumerate(user.keys(), start=1):
        if key != "password":
            print(f"{i}. {key.capitalize()}")

    choice = input("\nEnter field name to update: ").lower()
    if choice in user and choice != "password":
        new_value = input(f"Enter new value for {choice}: ")
        user[choice] = new_value
        save_data(data)
        print("\n Profile updated successfully!\n")
    else:
        print("\n Invalid field.\n")

def dashboard(username):
    while True:
        print("=== Student Dashboard ===")
        print("1. Show Profile")
        print("2. Update Profile")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_profile(username)
        elif choice == "2":
            update_profile(username)
        elif choice == "3":
            print("\nLogging out...\n")
            break
        else:
            print("\nInvalid choice! Try again.\n")

# ===============================
# Main Program Loop
# ===============================

def main():
    while True:
        print("===== Student Registration System =====")
        print("1. Register New Student")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\n Exiting program... Goodbye!\n")
            break
        else:
            print("\n Invalid choice! Please try again.\n")

# ===============================
# Start the program
# ===============================
if __name__ == "__main__":
    main()
