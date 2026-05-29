# Password Manager

A simple command-line Password Manager built in Python that securely stores passwords using SHA-256 hashing.

## Features

* Add new passwords
* View stored accounts
* Search passwords by website
* Delete saved passwords
* Secure password input using `getpass`
* Password hashing using SHA-256

## Technologies Used

* Python
* hashlib
* getpass

## How It Works

When a user adds a password:

1. The password is entered securely without being displayed on the screen.
2. The password is converted into a SHA-256 hash.
3. The hashed password is stored in memory along with the username and website.

Example:

Website: GitHub
Username: user123
Password: mypassword

Stored as:

SHA256 Hash:
89e01536ac207279409d4de1e5253e01f4a4d8c4e385a7f4c3c6eb9e7f7b4e7c

## Menu

```text
===== PASSWORD MANAGER =====

1. Add Password
2. View Passwords
3. Search Password
4. Delete Password
5. Exit
```

## Project Structure

```text
password-manager/
│
├── main.py
├── README.md
```

## Learning Outcomes

This project helped practice:

* Functions
* Dictionaries
* Password hashing
* User input handling
* Python modules
* Command-line application development

## Future Improvements

* Store passwords in JSON files
* Password generator
* Password strength checker
* Master password authentication
* Encryption support

## Author

Built as a Python practice project to learn hashing and secure password handling.
