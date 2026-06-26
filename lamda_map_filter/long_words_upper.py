"""
## 2. Filter Long Words and Convert to Uppercase  *(Easy)*

=================================================
LONG WORDS TO UPPERCASE
=================================================

Problem Statement:
Write a Python program that takes a list of
strings and returns a TUPLE of two values:
   1. a list of words whose length is greater
      than 4, all converted to UPPERCASE
   2. a set of unique FIRST letters of those
      long words (also uppercase)

You MUST use lambda, filter(), and map().


-------------------------------------------------
Input Example:
["apple", "kiwi", "banana", "fig", "orange", "pear"]

Output Example:
Long Words: ['APPLE', 'BANANA', 'ORANGE']
First Letters: {'A', 'B', 'O'}

-------------------------------------------------
Explanation:
filter (len > 4)  -> ['apple', 'banana', 'orange']
map    (upper)    -> ['APPLE', 'BANANA', 'ORANGE']
First letters set -> {'A', 'B', 'O'}
=================================================

"""
# --- code is from here ---

words = ["apple", "kiwi", "banana", "fig", "orange", "pear"]

longs = list(filter(lambda w: len(w) > 4, words))
upper = list(map(lambda w: w.upper(), longs))
first = set(map(lambda w: w[0], upper))

result = (upper, first)

print("Long Words:", result[0])
print("First Letters:", result[1])
