"""
=================================================
CONSECUTIVE CHARACTER COUNTER
=================================================

Problem Statement:
Write a Python program to count the maximum number
of consecutive occurrences of the same character
in a string.

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Use a for loop.
3. Find the longest consecutive repeating character.
4. Print:
   - character
   - count

-------------------------------------------------
Input Example:
aaabbccccdde

Output Example:
Character: c
Count: 4

-------------------------------------------------
Explanation:
a -> 3 times
b -> 2 times
c -> 4 times
d -> 2 times
e -> 1 time

Highest consecutive count:
c -> 4

-------------------------------------------------
Hints:
1. Compare current character with previous character.
2. Keep track of:
   - current count
   - maximum count
3. Update maximum when needed.

-------------------------------------------------
Expected Concepts:
- Don't use dictionary.
- for loops
- string indexing
- operators
- conditional statements
- logical thinking

=================================================
"""

# ---code is from here ---

s = input("Enter a string: ")

count = 0
max_count = 0
ch = s[0]
max_ch = s[0]

for i in s:
    if i == ch:
        count = count + 1
    else:
        if count > max_count:
            max_count = count
            max_ch = ch
        count = 1
        ch = i

if count > max_count:
    max_count = count
    max_ch = ch

print("Character:", max_ch)
print(f"Count: {max_count}")   
