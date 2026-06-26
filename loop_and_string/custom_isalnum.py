"""
## 2. Build Your Own `isalnum()`

=================================================
CUSTOM ISALNUM IMPLEMENTATION
=================================================

Problem Statement:
Without using the built-in str.isalnum() method,
write a Python program that checks whether a
given string contains ONLY alphanumeric
characters (letters A-Z, a-z, and digits 0-9).

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Write your own function my_isalnum(s).
3. Use a for loop to inspect each character.
4. Do NOT use:
   - str.isalnum()
   - str.isalpha()
   - str.isdigit()
   You may compare characters using their
   ASCII range (e.g. 'a' <= ch <= 'z').
5. Return True if all characters are
   alphanumeric, otherwise False.
6. Print:
   - True or False

-------------------------------------------------
Input Example 1:
Hello123

Output Example 1:
True

-------------------------------------------------
Input Example 2:
Hello 123!

Output Example 2:
False

-------------------------------------------------
Explanation:
"Hello123" -> every character is a letter or
digit, so the result is True.
"Hello 123!" contains a space and '!', which
are not alphanumeric, so the result is False.
=================================================

"""
# --- code is from here ---
def my_isalnum(s):
    for ch in s:
        if (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')):
            return True
        else :
            return False
         
string = input("Enter a string: ")

print(my_isalnum(string))
