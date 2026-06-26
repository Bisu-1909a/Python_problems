"""
=================================================
EVEN OR ODD CHECKER
=================================================

Problem Statement:
Write a Python program to check whether a number
is Even or Odd.

-------------------------------------------------
Input Example:
7

Output Example:
Odd

=================================================
"""

# --- code is from here ---

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    