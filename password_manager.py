import hashlib

passwords = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- Password Manager Functions ----------

def add_password():
    website = input("Enter website: ")
    print("Website received")

    username = input("Enter username: ")
    print("Username received")

    password = input("Enter password: ")

    passwords[website] = {
        "username": username,
        "password": hash_password(password)
    }

    print("Password added successfully.\n")

def view_passwords():
    if not passwords:
        print("No passwords stored.\n")
        return

    print("\nStored Passwords:")
    for website, details in passwords.items():
        print(f"""
Website : {website}
Username: {details['username']}
Password Hash: {details['password']}
""")
    print()


def search_password():
    website = input("Enter website to search: ")

    if website in passwords:
        details = passwords[website]

        print(f"""
Website : {website}
Username: {details['username']}
Password Hash: {details['password']}
""")
    else:
        print("Website not found.\n")


def delete_password():
    website = input("Enter website to delete: ")

    if website in passwords:
        del passwords[website]
        print("Password deleted successfully.\n")
    else:
        print("Website not found.\n")


while True:
    print("""
===== PASSWORD MANAGER =====
1. Add Password
2. View Passwords
3. Search Password
4. Delete Password
5. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        delete_password()

    elif choice == "5":
        print("Exiting Password Manager.")
        break

    else:
        print("Invalid choice. Try again.\n")