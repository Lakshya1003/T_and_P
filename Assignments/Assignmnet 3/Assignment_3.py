import random
from datetime import datetime

# =========================users Class===================================
class User:
    def __init__(self, enrollment="", name="", email="", branch="", year="", contact="", password=""):
        self.enrollment = enrollment
        self.name = name
        self.email = email
        self.branch = branch
        self.year = year
        self.contact = contact
        self.password = password

    def save(self):
        with open("users.txt", "a") as f:
            f.write(f"{self.enrollment},{self.name},{self.email},{self.branch},{self.year},{self.contact},{self.password}\n")

    @staticmethod
    def load():
        users = {}
        try:
            with open("users.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 7:
                        e, n, em, b, y, c, p = parts
                        users[e] = User(e, n, em, b, y, c, p)
        except FileNotFoundError:
            pass
        return users

    @staticmethod
    def update(updated_user):
        users = User.load()
        users[updated_user.enrollment] = updated_user
        with open("users.txt", "w") as f:
            for u in users.values():
                f.write(f"{u.enrollment},{u.name},{u.email},{u.branch},{u.year},{u.contact},{u.password}\n")


# ==========================Quix class================
class Quiz:
    questions = {
        "DSA": [
            ("Which data structure uses LIFO principle?", ["Stack", "Queue", "Tree", "Graph"], "Stack"),
            ("Which sorting algorithm has worst-case O(n^2)?", ["Quick", "Merge", "Heap", "Bubble"], "Bubble"),
            ("Python uses which data structure for recursion?", ["Queue", "Stack", "Heap", "List"], "Stack"),
            ("In a BST, left subtree nodes are:", ["Greater", "Equal", "Less", "Unrelated"], "Less"),
            ("Which of these is dynamic?", ["Array", "Queue", "Tree", "Stack"], "Tree")
        ],
        "DBMS": [
            ("What does DBMS stand for?", ["Database Management System", "Data Basic Management System", "Database Management Software", "Data Management System"], "Database Management System"),
            ("What is a primary key used for?", ["Uniquely identify records", "Link tables", "Sort data", "Store objects"], "Uniquely identify records"),
            ("Which language interacts with RDBMS?", ["SQL", "Java", "Python", "C++"], "SQL"),
            ("Which joins tables?", ["JOIN", "SELECT", "DELETE", "UPDATE"], "JOIN"),
            ("Normalization reduces?", ["Redundancy", "Speed", "Size", "Security"], "Redundancy")
        ],
        "PYTHON": [
            ("Keyword for function in Python?", ["func", "define", "def", "function"], "def"),
            ("Symbol for single-line comment?", ["//", "/* */", "#", "<!-- -->"], "#"),
            ("List is?", ["Mutable", "Immutable", "Constant", "None"], "Mutable"),
            ("Operator for power?", ["^", "**", "%", "//"], "**"),
            ("Dictionaries store?", ["Ordered pairs", "Key-value pairs", "Characters", "Loops"], "Key-value pairs")
        ]
    }

    @staticmethod
    def start_quiz(user):
        print("\nChoose Category:\n1. DSA\n2. DBMS\n3. PYTHON")
        choice = input("Enter choice: ")
        category = {"1": "DSA", "2": "DBMS", "3": "PYTHON"}.get(choice)

        if not category:
            print("Invalid category.\n")
            return

        qs = Quiz.questions[category]
        random.shuffle(qs)
        score = 0
        total = min(len(qs), 5)

        print(f"\nStarting {category} Quiz...")
        for q, opts, ans in qs[:total]:
            print(f"\n{q}")
            for i, op in enumerate(opts, 1):
                print(f"{i}. {op}")
            user_ans = input("Your answer (number): ")

            if user_ans.isdigit() and 1 <= int(user_ans) <= len(opts):
                if opts[int(user_ans) - 1] == ans:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! Correct answer: {ans}")
            else:
                print("Invalid input, skipped question.")

        print(f"\nYour score: {score}/{total}")
        with open("scores.txt", "a") as f:
            f.write(f"{user.enrollment},{category},{score}/{total},{datetime.now()}\n")


# ============================System class======================================
class System:
    def __init__(self):
        self.logged_user = None

    def register(self):
        print("\n--- Registration ---")
        e = input("Enrollment: ")
        users = User.load()
        if e in users:
            print("Enrollment already registered!")
            return

        n = input("Name: ")
        em = input("Email: ")
        b = input("Branch: ")
        y = input("Year: ")
        c = input("Contact: ")
        p = input("Password: ")

        user = User(e, n, em, b, y, c, p)
        user.save()
        print("Registration successful!")

    def login(self):
        print("\n--- Login ---")
        e = input("Enrollment: ")
        p = input("Password: ")

        if e == "admin" and p == "admin123":
            self.admin_panel()
            return

        users = User.load()
        if e in users and users[e].password == p:
            self.logged_user = users[e]
            print("Login successful!")
            self.quiz_menu()
        else:
            print("Invalid credentials!")

    def quiz_menu(self):
        while self.logged_user:
            print("\n==== QUIZ MENU ====")
            print("1. Attempt Quiz")
            print("2. View Profile")
            print("3. Update Profile")
            print("4. Logout")
            ch = input("Enter choice: ")

            if ch == "1":
                Quiz.start_quiz(self.logged_user)
            elif ch == "2":
                self.show_profile()
            elif ch == "3":
                self.update_profile()
            elif ch == "4":
                self.logged_user = None
                print("Logged out.")
            else:
                print("Invalid choice!")

    def update_profile(self):
        if not self.logged_user:
            print("Login first.")
            return
        u = self.logged_user
        u.email = input(f"Email ({u.email}): ") or u.email
        u.branch = input(f"Branch ({u.branch}): ") or u.branch
        u.year = input(f"Year ({u.year}): ") or u.year
        u.contact = input(f"Contact ({u.contact}): ") or u.contact
        u.name = input(f"Name ({u.name}): ") or u.name
        User.update(u)
        print("Profile updated!")

    def show_profile(self):
        if not self.logged_user:
            print("Login first.")
            return
        u = self.logged_user
        print("\n--- PROFILE ---")
        print(f"Enrollment: {u.enrollment}")
        print(f"Name: {u.name}")
        print(f"Email: {u.email}")
        print(f"Branch: {u.branch}")
        print(f"Year: {u.year}")
        print(f"Contact: {u.contact}")

    def admin_panel(self):
        while True:
            print("\n=== ADMIN PANEL ===")
            print("1. View All Users")
            print("2. View All Scores")
            print("3. Exit Admin Panel")
            ch = input("Enter choice: ")

            if ch == "1":
                self.view_users()
            elif ch == "2":
                self.view_scores()
            elif ch == "3":
                break
            else:
                print("Invalid choice.")

    def view_users(self):
        users = User.load()
        if not users:
            print("No users registered.")
            return
        print("\n--- ALL USERS ---")
        for u in users.values():
            print(f"{u.enrollment} | {u.name} | {u.email} | {u.branch} | {u.year} | {u.contact}")

    def view_scores(self):
        try:
            with open("scores.txt", "r") as f:
                lines = f.readlines()
                if not lines:
                    print("No scores recorded.")
                    return
                print("\n--- ALL SCORES ---")
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print("No scores file found yet.")

    def main_menu(self):
        while True:
            print("\n==== MAIN MENU ====")
            print("1. Register")
            print("2. Login (User/Admin)")
            print("3. Exit")
            ch = input("Enter choice: ")

            if ch == "1":
                self.register()
            elif ch == "2":
                self.login()
            elif ch == "3":
                print("Exiting system.")
                break
            else:
                print("Invalid choice!")

#============================Main=================================
if __name__ == "__main__":
    app = System()
    app.main_menu()
