"""
## 2. Invert a Dictionary  *(Medium)*

=================================================
INVERT A DICTIONARY
=================================================

Problem Statement:
Write a Python FUNCTION called `invert_dict`
that takes a dictionary as input and returns
a NEW dictionary where:
   - the original VALUES become keys
   - the original KEYS become values

If multiple original keys share the same value,
the inverted dictionary must map that value to
a LIST of all the original keys that had it.

-------------------------------------------------
Instructions:
1. Define a function:
      def invert_dict(d):
2. Create an empty result dictionary.
3. Use a for loop to iterate over d.items().
4. For each (key, value):
   - if value is already a key in the result,
     append the original key to its list
   - otherwise, add it with a list containing
     the original key
5. Do NOT use:
   - dict comprehensions
   - collections.defaultdict
6. Return the inverted dictionary and print it.

-------------------------------------------------
Input Example 1:
{'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

Output Example 1:
{1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}

-------------------------------------------------
Input Example 2:
{'x': 10, 'y': 20}

Output Example 2:
{10: ['x'], 20: ['y']}

-------------------------------------------------
Explanation:
For the first example:
   value 1 came from keys 'a' and 'c'
   value 2 came from keys 'b' and 'e'
   value 3 came from key  'd'
So the inverted dictionary groups original
keys under each unique original value.
=================================================

"""
# --- code is from here ---

def invert_dict(d):
    result = {}

    for key, value in d.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]

    return result

original = {"x" : 10 , "y" : 20 , "z" : 30}

inverted = invert_dict(original)
print("Original Dictionary:", original)
print("Inverted Dictionary:", inverted)
