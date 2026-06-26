"""
## 1. Count Vowels in a String

=================================================
VOWEL COUNTER
=================================================

Problem Statement:
Write a Python program that takes a string as
input and counts how many vowels (a, e, i, o, u)
it contains. The check must be case-insensitive.

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Use a for loop to traverse each character.
3. Treat uppercase and lowercase vowels as same.
4. Print:
   - total vowel count

Note: use ASCII  check for letters, and compare. 'e', 'i', 'o', '

-------------------------------------------------
Input Example:
Hello World

Output Example:
Vowel Count: 3

-------------------------------------------------
Explanation:
H e l l o   W o r l d
  ^       ^       ^
'e', 'o', 'o' are vowels -> 3 vowels.
=================================================

"""
# --- code is from here ---

String = input("Enter a string: ")
count = 0

for i in String:
    code = ord(i)
    if code == 65 or code == 97:   # 'A' or 'a'
        count += 1
    elif code == 69 or code == 101: # 'E' or 'e'
        count += 1
    elif code == 73 or code == 105: # 'I' or 'i'
        count += 1
    elif code == 79 or code == 111: # 'O' or 'o'
        count += 1
    elif code == 85 or code == 117: # 'U' or 'u'
        count += 1

print("Total vowels:", count)
