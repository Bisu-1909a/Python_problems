"""
=================================================
LOGIN VALIDATOR SYSTEM
=================================================

Problem Statement:
Write a Python program for a simple login system.

-------------------------------------------------
Conditions:
1. Username should be: admin
2. Password should be: python123

-------------------------------------------------
Requirements:
1. If both username and password are correct:
      Print "Login Successful"

2. If username is wrong:
      Print "Invalid Username"

3. If password is wrong:
      Print "Invalid Password"

4. If both are wrong:
      Print "Invalid Credentials"

-------------------------------------------------
Input Example:
Username: admin
Password: test

Output Example:
Invalid Password

=================================================
"""

# --- code is start from here ---
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
elif username != "admin" and password != "python123":
    print("Invalid Credentials")
elif username != "admin":
    print("Invalid Username")
else:
      print("Invalid Password")
      