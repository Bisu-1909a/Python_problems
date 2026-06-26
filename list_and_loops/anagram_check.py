"""
## 5. Check if Two Strings are Anagrams (*Hard*)

=================================================
ANAGRAM CHECK
=================================================

Problem Statement:
Write a Python program that takes TWO strings
as input and checks whether they are ANAGRAMS
of each other.

Two strings are anagrams if they contain the
exact same characters with the same frequency,
just in a different order. The check must be
case-insensitive and should ignore spaces.

-------------------------------------------------
Instructions:
1. Take two strings as input.
2. Convert both strings to lowercase and
   remove all spaces using a for loop
   (do NOT use str.replace()).
3. If their lengths are different, they cannot
   be anagrams.
4. Do NOT use:
   - sorted() or .sort()
   - dictionaries
   - sets
   - collections.Counter
   - str.count()
5. Print:
   - "Anagram" or "Not Anagram"

-------------------------------------------------
Input Example 1:
String 1: Listen
String 2: Silent

Output Example 1:
Anagram

-------------------------------------------------
Input Example 2:
String 1: Hello
String 2: World

Output Example 2:
Not Anagram

-------------------------------------------------
Explanation:
"Listen" -> "listen"
"Silent" -> "silent"
Both have the same characters with the same
frequency (l, i, s, t, e, n) -> Anagram.

"Hello" and "World" do not contain the same
characters, so they are Not Anagram.
=================================================

"""
# --- code is from here ---

a = input("enter the first string: ")
b = input("enter the second string: ")

# clean strings (lowercase + no spaces)
x = ""
for c in a:
    if c != " ":
        x += c.lower()

y = ""
for c in b:
    if c != " ":
        y += c.lower()

if len(x) != len(y):
    print("Not Anagram")
    
else:
    lst = list(y)
    ok = True

    for c in x:
        found = False
        for i in range(len(lst)):
            if lst[i] == c:
                lst[i] = None
                found = True
                break
        if not found:
            ok = False
            break

    if ok:
        print("Anagram")
    else:
        print("Not Anagram") 
        