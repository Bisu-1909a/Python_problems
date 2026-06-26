"""
## 2. Count Words in a Sentence (Without split)  *(Medium)*

=================================================
COUNT WORDS MANUALLY
=================================================

Problem Statement:
Write a Python program that takes a sentence
as input and counts the number of WORDS in it,
WITHOUT using the built-in split() method.

A word is any group of non-space characters
separated by one or more spaces. The sentence
may begin or end with spaces, and may contain
multiple spaces between words.

-------------------------------------------------
Instructions:
1. Take a sentence as input.
2. Use a for loop to scan the sentence
   character by character.
3. Do NOT use:
   - str.split()
   - str.count()
   - len() on a list of words
4. Track whether you are currently INSIDE a word.
   A new word begins when you move from a space
   to a non-space character.
5. Print:
   - total number of words

-------------------------------------------------
Input Example 1:
Hello world from Python

Output Example 1:
Word Count: 4

-------------------------------------------------
Input Example 2:
   I   love    coding   

Output Example 2:
Word Count: 3

-------------------------------------------------
Explanation:
For "Hello world from Python":
   words -> "Hello", "world", "from", "Python" -> 4

For "   I   love    coding   ":
   leading/trailing/extra spaces are ignored.
   words -> "I", "love", "coding" -> 3
=================================================

"""
# --- code is from here ---

string = input("Enter a sentence: ")

count = 0
inside = False   

for ch in string:
    if ch != " ":        
        if not inside:   
            count += 1
            inside = True
    else:             
        inside = False   

print("Number of words:", count) 
