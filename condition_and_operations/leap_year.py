"""
=================================================
LEAP YEAR CHECKER
=================================================

Problem Statement:
Write a Python program to check whether a given
year is a Leap Year or not.

-------------------------------------------------
Rules:
1. A year is a Leap Year if it is divisible by 4.
2. But if the year is divisible by 100,
   then it is NOT a Leap Year.
3. However, if the year is divisible by 400,
   then it IS a Leap Year.

-------------------------------------------------
Instructions:
1. Take year as input from the user.
2. Use operators and conditional statements only.
3. Print:
   - "Leap Year"
   - "Not a Leap Year"

-------------------------------------------------
Input Example:
2024

Output Example:
Leap Year

-------------------------------------------------
More Examples:

Input:
1900

Output:
Not a Leap Year

-------------------------

Input:
2000

Output:
Leap Year

-------------------------------------------------
Hints:
1. Use modulus (%) operator.
2. Carefully check multiple conditions.
3. Think about the order of conditions.

=================================================
"""

# --- code is from here ---

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
    