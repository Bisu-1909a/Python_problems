"""
##  Binary Search on a Descending Sorted List  *(Medium)*

=================================================
BINARY SEARCH ON A DESCENDING LIST
=================================================

Problem Statement:
Write a Python FUNCTION called
`binary_search_desc` that takes a list of
integers sorted in DESCENDING order and a
target value, and returns the INDEX of the
target using BINARY SEARCH.

If the target is not present, return -1.

The classic binary search assumes ASCENDING
order. For a DESCENDING list, the comparison
directions must be FLIPPED.

-------------------------------------------------
Input Example 1:
desc_list = [50, 40, 30, 20, 10]
target    = 30

Output Example 1:
Found at index: 2

-------------------------------------------------
Input Example 2:
desc_list = [99, 88, 77, 66, 55, 44, 33]
target    = 50

Output Example 2:
Not Found

-------------------------------------------------
Explanation:
For target = 30 in [50, 40, 30, 20, 10]:
   low=0, high=4 -> mid=2 -> value 30 == 30
   return 2

For target = 50 in a list that does not
contain 50, the loop ends with low > high
and the function returns -1.
=================================================

"""
# --- code is from here ---

def binary_search_desc(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if list[mid] == target:
            return mid
         
        elif list[mid] < target:
            high = mid - 1
            
        else:
            low = mid + 1

    return -1


list = [50, 40, 30, 20, 10]
target = 30
result = binary_search_desc(list, target)
if result != -1:
    print("Found at index:", result)
else:
    print("Not Found")
    
list = [99, 88, 77, 66, 55, 44, 33]
target = 50
result = binary_search_desc(list, target)
if result != -1:
    print("Found at index:", result)
else:
    print("Not Found")
