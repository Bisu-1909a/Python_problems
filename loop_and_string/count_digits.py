"""
## 4. Count the Number of Digits

=================================================
COUNT DIGITS USING MODULO
=================================================

Problem Statement:
Write a Python program that takes a positive
integer as input and counts the number of
digits in it. You MUST solve this using the
modulo (%) and integer division (//) operators
inside a loop.

-------------------------------------------------
Instructions:
1. Take a positive integer n as input.
2. Do NOT convert the number to a string.

-------------------------------------------------
Input Example 1:
5839

Output Example 1:
Digit Count: 4

-------------------------------------------------
Input Example 2:
0

Output Example 2:
Digit Count: 1

-------------------------------------------------
Explanation:
For 5839:
   5839 % 10 = 9, 5839 // 10 = 583  -> count 1
   583  % 10 = 3, 583  // 10 = 58   -> count 2
   58   % 10 = 8, 58   // 10 = 5    -> count 3
   5    % 10 = 5, 5    // 10 = 0    -> count 4
Loop stops. Total digits = 4.
=================================================

"""
# --- code is from here ---

number = int(input("Enter a positive integer: "))
count = 0
while number > 0:
    digit = number % 10 
    number = number // 10
    count += 1
print("Number of digits:", count) 
