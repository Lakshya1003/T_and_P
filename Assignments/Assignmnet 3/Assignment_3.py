import json
import random
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


def attempt_quiz():
    while True:
        print("===== Select Quiz category =====")
        print("1. DSA")
        print("2. DBMS")
        print("3. AIML")
        print("4. Python")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            quiz()
        elif choice == "4":
            print("\n Exiting program... Goodbye!\n")
            break
        else:
            print("\n Invalid choice! Please try again.\n")
#================================
# Quiz Program
# ===============================

def quiz():
    data = load_data()
    username = input("\n Enter username : ")
    password = input("\n Enter password: ")
    if username in data and data[username]["password"] == password:
        print("1. Attempt Quiz")
        print("2. View past score")
        print("3. Back to main menu")
        choice = input("What's in your mind : ")

        if choice == "1":
            # attempt_quiz()
            pass
        elif choice == "2":
            # view_score(username)
            pass
        elif choice == "3":
            main()
        else:
            print("\n Invalid choice! Please try again.\n")
    else:
        print("\n Invalid credentials! Please try again\n")
        print("\n Press y to register press n to return to main menu : \n")

        nextStep = input("Enter your choice:")
        if nextStep == "y":
            register()
        elif nextStep == "n":
            main()
        else :
            print("Returning to Main menu...")
            main()

# ===============================
# Main Program Loop
# ===============================

def main():
    while True:
        print("===== Student Registration System =====")
        print("1. Register New Student")
        print("2. Login")
        print("3. Quiz")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            quiz()
        elif choice == "4":
            print("\n Exiting program... Goodbye!\n")
            break
        else:
            print("\n Invalid choice! Please try again.\n")

# ===============================
# Start the program
# ===============================
if __name__ == "__main__":
    main()
