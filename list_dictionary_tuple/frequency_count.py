"""
## 1. Count Frequency of Elements in a List  *(Easy)*

=================================================
ELEMENT FREQUENCY COUNTER
=================================================

Problem Statement:
Write a Python program that takes a list of
elements as input and counts how many times
EACH unique element appears in the list.
Store the result in a DICTIONARY where:
   - key   -> the element
   - value -> its frequency

-------------------------------------------------
Input Example 1:
['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

Output Example 1:
{'apple': 3, 'banana': 2, 'orange': 1}

-------------------------------------------------
Input Example 2:
[1, 2, 2, 3, 3, 3]

Output Example 2:
{1: 1, 2: 2, 3: 3}

-------------------------------------------------
Explanation:
For ['apple', 'banana', 'apple', 'orange',
     'banana', 'apple']:
   apple  -> 3 times
   banana -> 2 times
   orange -> 1 time
Result -> {'apple': 3, 'banana': 2, 'orange': 1}
=================================================

"""
# --- code is from here ---

i = input("Enter elements: ").split()
count = {}
for key in i:
    k = key.lower()   
    if k in count:
        count[k] = count[k] + 1
    else:
        count[k] = 1
print("Frequency dictionary:", count)
