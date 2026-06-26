"""
=================================================
CHARACTER FREQUENCY COUNTER
=================================================

Problem Statement:
Write a Python program to count how many times
a character appears in a string.

-------------------------------------------------
Instructions:
1. Take input from the user:
   - a string
   - a character
2. Use loop and conditional statements.
3. Print character count.

-------------------------------------------------
Input Example:
String: programming
Character: g

Output Example:
2
-------------------------------------------------
Expected Concepts:
- loops
- strings
- operators
- logical thinking

=================================================
"""

# --- code is from here ---

string = input("Enter the string: ")
char = input("Enter the character to count: ")
count = 0

for i in string:
    if i == char:
        count = count + 1

print(f"the time of repeatation of {char} is {count}")   
