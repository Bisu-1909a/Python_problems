"""
=================================================
PALINDROME CHECKER
=================================================

Problem Statement:
Write a Python program to check whether a string
is palindrome or not.

-------------------------------------------------
Instructions:
1. Take string input.
2. Reverse the string.
3. Compare original and reversed string.
4. Print:
   - "Palindrome"
   - "Not Palindrome"

-------------------------------------------------
Input Example:
madam

Output Example:
Palindrome

-------------------------------------------------
Hints:
Use slicing or loop.

-------------------------------------------------
Expected Concepts:
- operators
- string slicing
- conditional statements

=================================================
"""

# --- code is from here ---

string = input("Enter a string: ")
reversed = string[::-1]
if string == reversed:
    print("Palindrome")
else:
    print("Not Palindrome") 
    