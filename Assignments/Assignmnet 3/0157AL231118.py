import json
import csv
import os
import random
from datetime import datetime

# ---------------- FILE SETUP ---------------- #

USER_DB = "users.json"
SCORES_DB = "scores.csv"

QUESTION_PATHS = {
    "DBMS": "Dbms.json",
    "DSA": "Dsa.json",
    "PYTHON": "Python.json"
}

current_user = ""
is_logged_in = False
is_superuser = False
user_data = {}

# ---------------- USER MANAGEMENT ---------------- #

def load_user_data():
    global user_data
    if os.path.exists(USER_DB):
        try:
            with open(USER_DB, "r") as f:
                user_data = json.load(f)
        except:
            user_data = {}
    else:
        user_data = {
            "admin": {
                "password": "admin123",
                "name": "Administrator",
                "email": "",
                "branch": "",
                "year": "",
                "contact": "",
                "enrollment": "0000"
            }
        }
        save_user_data()

def save_user_data():
    with open(USER_DB, "w") as f:
        json.dump(user_data, f, indent=2)

def setup_score_file():
    if not os.path.exists(SCORES_DB):
        with open(SCORES_DB, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["enrollment", "username", "category", "score", "total", "datetime"])


# ---------------- QUESTIONS ---------------- #

def fetch_questions(category):
    file_name = QUESTION_PATHS.get(category)
    if not file_name or not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except:
        return []

def save_questions(category, updated_list):
    file_name = QUESTION_PATHS.get(category)
    if not file_name:
        return
    with open(file_name, "w") as f:
        json.dump(updated_list, f, indent=2)


# ---------------- REGISTRATION & LOGIN ---------------- #

def register_user():
    global user_data
    print("\n-- New User Registration --")
    uname = input("Username: ").strip()
    if uname in user_data:
        print("Username already taken.")
        return

    pwd = input("Password: ").strip()
    name = input("Full Name: ").strip()
    email = input("Email: ").strip()
    branch = input("Branch: ").strip()
    year = input("Year: ").strip()
    contact = input("Contact Number: ").strip()
    enroll = input("Enrollment Number: ").strip()

    user_data[uname] = {
        "password": pwd,
        "name": name,
        "email": email,
        "branch": branch,
        "year": year,
        "contact": contact,
        "enrollment": enroll
    }
    save_user_data()
    print("Registration Successful!")

def login_user():
    global is_logged_in, current_user, is_superuser
    if is_logged_in:
        print("You’re already logged in.")
        return

    uname = input("Username: ").strip()
    pwd = input("Password: ").strip()
    user = user_data.get(uname)

    if user and user.get("password") == pwd:
        is_logged_in = True
        current_user = uname
        is_superuser = (uname == "admin")
        print(f"Logged in as {uname}")
    else:
        print("Invalid credentials.")

def logout_user():
    global is_logged_in, current_user, is_superuser
    if not is_logged_in:
        print("You’re not even logged in.")
        return
    is_logged_in = False
    current_user = ""
    is_superuser = False
    print("Logged Out Successfully.")


# ---------------- PROFILE ---------------- #

def show_profile():
    if not is_logged_in:
        print("Login required.")
        return

    p = user_data.get(current_user, {})
    print("\n-- Profile --")
    print(f"Username   : {current_user}")
    print(f"Name       : {p.get('name')}")
    print(f"Email      : {p.get('email')}")
    print(f"Branch     : {p.get('branch')}")
    print(f"Year       : {p.get('year')}")
    print(f"Contact    : {p.get('contact')}")
    print(f"Enrollment : {p.get('enrollment')}")
    print(f"Role       : {'Admin' if is_superuser else 'User'}")


def edit_profile():
    if not is_logged_in:
        print("Login required.")
        return

    profile = user_data[current_user]
    print("\n-- Update Profile (enter blank to skip) --")

    nm = input(f"Name [{profile['name']}]: ")
    em = input(f"Email [{profile['email']}]: ")
    br = input(f"Branch [{profile['branch']}]: ")
    yr = input(f"Year [{profile['year']}]: ")
    ct = input(f"Contact [{profile['contact']}]: ")
    pw = input("New Password (blank = no change): ")

    if nm: profile["name"] = nm
    if em: profile["email"] = em
    if br: profile["branch"] = br
    if yr: profile["year"] = yr
    if ct: profile["contact"] = ct
    if pw: profile["password"] = pw

    save_user_data()
    print("Profile Updated!")


# ---------------- QUIZ ---------------- #

def take_quiz():
    if not is_logged_in:
        print("Please login to attempt a quiz.")
        return

    print("\n-- Quiz Categories --")
    for i, cat in enumerate(QUESTION_PATHS.keys(), start=1):
        print(f"{i}. {cat}")

    try:
        category = list(QUESTION_PATHS.keys())[int(input("Choose category: ")) - 1]
    except:
        print("Invalid selection.")
        return

    questions = fetch_questions(category)
    if not questions:
        print("No questions available.")
        return

    selected = random.sample(questions, min(len(questions), 10))
    random.shuffle(selected)

    score = 0
    print(f"\nStarting {category} Quiz\n")

    for i, q in enumerate(selected, start=1):
        print(f"Q{i}. {q['question']}")
        for idx, opt in enumerate(q["options"]):
            print(f"  {chr(65+idx)}. {opt}")

        ans = input("Your Answer: ").upper()
        if ans in [chr(65+n) for n in range(len(q["options"]))] and q["options"].index(q["options"][ord(ans)-65]) == q["answer_index"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")

    total = len(selected)
    print(f"You scored {score}/{total}")

    enroll = user_data[current_user].get("enrollment", "")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    setup_score_file()
    with open(SCORES_DB, "a", newline="") as f:
        csv.writer(f).writerow([enroll, current_user, category, score, total, now])

    print("Score Saved!")


# ---------------- MAIN APP ---------------- #

def main():
    load_user_data()
    setup_score_file()

    while True:
        print("""
        === LNCT QUIZ SYSTEM ===
        1. Register
        2. Login
        3. View Profile
        4. Update Profile
        5. Attempt Quiz
        6. Logout
        7. Exit
        """)
        choice = input("Select: ")

        if choice == "1": register_user()
        elif choice == "2": login_user()
        elif choice == "3": show_profile()
        elif choice == "4": edit_profile()
        elif choice == "5": take_quiz()
        elif choice == "6": logout_user()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
