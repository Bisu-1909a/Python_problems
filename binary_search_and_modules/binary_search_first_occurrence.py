"""
##  Binary Search for FIRST Occurrence  *(Medium)*

=================================================
BINARY SEARCH - FIRST OCCURRENCE
=================================================

Problem Statement:
Write a Python FUNCTION called
`first_occurrence` that takes a SORTED list
(ascending) and a target value, and returns
the INDEX of the FIRST occurrence of the
target.

If the target is not present, return -1.

The list MAY contain duplicates. A normal
binary search can land on ANY occurrence of
the target, so you must keep searching the
LEFT half after a match to make sure you find
the earliest index.

-------------------------------------------------
Instructions:
1. Define a function:
      def first_occurrence(sorted_list, target):
2. Use two pointers:
      low = 0, high = len(sorted_list) - 1
3. Keep a variable `result = -1` to remember
   the earliest match found so far.

-------------------------------------------------
Input Example 1:
sorted_list = [1, 2, 2, 2, 3, 4, 5]
target      = 2

Output Example 1:
First occurrence at index: 1

-------------------------------------------------
Input Example 2:
sorted_list = [1, 1, 1, 1, 1]
target      = 1

Output Example 2:
First occurrence at index: 0

-------------------------------------------------
Input Example 3:
sorted_list = [1, 3, 5, 7]
target      = 4

Output Example 3:
Not Found

-------------------------------------------------
Explanation:
For [1, 2, 2, 2, 3, 4, 5] and target = 2:
   low=0, high=6 -> mid=3 -> 2 == 2
       record result=3, then go LEFT: high=2
   low=0, high=2 -> mid=1 -> 2 == 2
       record result=1, then go LEFT: high=0
   low=0, high=0 -> mid=0 -> 1 < 2 -> low=1
   loop ends with low > high -> return 1.
The earliest index of 2 is 1.
=================================================

"""
# --- code is from here ---

def first_occurrence(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    result = -1   # to remember the earliest match

    while low <= high:
        mid = (low + high) // 2   

        if sorted_list[mid] == target:
            result = mid          # record this match
            high = mid - 1        # keep searching LEFT side
        elif sorted_list[mid] < target:
            low = mid + 1        
        else:
            high = mid - 1       

    return result


nums = [1, 2, 2, 2, 3, 4, 5]
target = 2
pos = first_occurrence(nums, target)
if pos != -1:
    print("First occurrence at index:", pos)
else:
    print("Not Found") 
    
nums = [1, 1, 1, 1, 1]
target = 1
pos = first_occurrence(nums, target)
if pos != -1:
    print("First occurrence at index:", pos)
else:
    print("Not Found")
    
    
nums = [1, 3, 5, 7]
target = 4
pos = first_occurrence(nums, target)
if pos != -1:
    print("First occurrence at index:", pos)
else:
    print("Not Found")
    