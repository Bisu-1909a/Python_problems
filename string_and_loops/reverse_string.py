"""
=================================================
REVERSE A STRING
=================================================

Problem Statement:
Write a Python program to reverse a string.

-------------------------------------------------
Instructions:
1. Take string input from the user.
2. Reverse the string using:
   - slicing AND
   - loop
3. Print reversed string.

-------------------------------------------------
Input Example:
Python

Output Example:
nohtyP

-------------------------------------------------
Expected Concepts:
- string slicing
- loops
- indexing

=================================================
"""

# --- code is from here ---

string= input("Enter a string: ")

# Method 1: 
print("Reversed :", string[::-1])

# Method 2:
reversed_text = ""
for ch in string:
    reversed_text = ch + reversed_text
    print("Reversed :", reversed_text) 
    