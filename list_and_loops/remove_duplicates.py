"""
## 4. Remove Duplicates from a List (Preserve Order)  *(Medium)*

=================================================
REMOVE DUPLICATES FROM A LIST
=================================================

Problem Statement:
Write a Python program that takes a list as
input and returns a NEW list with all
duplicates removed, while preserving the
ORIGINAL ORDER of first occurrences.

-------------------------------------------------
Instructions:
1. Take a list as input.
2. Use a for loop to traverse the original list.
3. Build a new list of unique elements.
4. Do NOT use:
   - set()
   - dict.fromkeys()
   - any other data structure besides lists
5. To check whether an element is already in
   the new list, write your own check using
   another for loop (do NOT use the 'in'
   operator).
6. Print:
   - the new list

-------------------------------------------------
Input Example 1:
[1, 2, 2, 3, 4, 4, 5, 1]

Output Example 1:
Unique List: [1, 2, 3, 4, 5]

-------------------------------------------------
Input Example 2:
[7, 7, 7, 7]

Output Example 2:
Unique List: [7]

-------------------------------------------------
Explanation:
For [1, 2, 2, 3, 4, 4, 5, 1]:
   keep first occurrence of each value
   -> [1, 2, 3, 4, 5]

For [7, 7, 7, 7]:
   only one unique value -> [7]
=================================================

"""
# --- code is from here ---

a = input("Enter list: ").split()

result = []

for i in a:
    found = False
    for j in result:
        if j == i:
            found = True
            break
    if not found:
        result.append(i)
print("List without duplicates:", result) 
