"""
## 2. Merge Two Dictionaries (Sum Values of Common Keys)  *(Medium)*

=================================================
MERGE TWO DICTIONARIES
=================================================

Problem Statement:
Write a Python program that takes TWO
dictionaries (with integer values) and merges
them into a SINGLE dictionary.

Rules:
   - If a key exists in BOTH dictionaries,
     the value in the merged dictionary must
     be the SUM of the two values.
   - If a key exists in only one dictionary,
     keep it as it is.

-------------------------------------------------
Input Example 1:
Dict 1: {'a': 10, 'b': 20, 'c': 30}
Dict 2: {'b': 5,  'c': 15, 'd': 25}

Output Example 1:
Merged: {'a': 10, 'b': 25, 'c': 45, 'd': 25}

-------------------------------------------------
Input Example 2:
Dict 1: {'x': 1}
Dict 2: {'y': 2}

Output Example 2:
Merged: {'x': 1, 'y': 2}

-------------------------------------------------
Explanation:
For the first example:
   'a' -> only in dict1 -> 10
   'b' -> 20 + 5  = 25
   'c' -> 30 + 15 = 45
   'd' -> only in dict2 -> 25
=================================================

"""
# ---- code is from here ----

d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 10, "c": 15, "d": 25}

merged = {}

for k in d1:
    merged[k] = d1[k]

for k in d2:
    if k in merged:       
        merged[k] += d2[k]
    else:                   
        merged[k] = d2[k]

print("Merged dictionary:", merged)
