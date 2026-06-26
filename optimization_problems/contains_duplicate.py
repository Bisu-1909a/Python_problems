"""
## 3. Contains Duplicate  *(Easy)*

=================================================
CONTAINS DUPLICATE
=================================================

Problem Statement:
You are given a list of integers. Return TRUE
if any value appears AT LEAST TWICE in the
list, otherwise return FALSE.

Write the BRUTE-FORCE O(n^2) version FIRST,
then optimize it to O(n) using a SET.

-------------------------------------------------
Instructions:
Write TWO functions:

1. has_duplicate_brute(nums)
   - Use two nested for loops to compare every
     pair (i, j) with i < j.
   - Return True as soon as nums[i] == nums[j].
   - If no duplicate is found, return False.
   - Time complexity:  O(n^2)
   - Space complexity: O(1)

2. has_duplicate_fast(nums)
   - Create an empty SET called `seen`.
   - Use a SINGLE for loop over nums:
        - if the value is already in `seen`,
          return True
        - otherwise, add it to `seen`
   - If the loop finishes without finding
     a duplicate, return False.
   - Time complexity:  O(n)
   - Space complexity: O(n)

Do NOT use:
   - list.count()
   - len(set(nums)) trick
   - sorted() / list.sort()
   - any external library

Call BOTH functions on the same input and
print both results.

-------------------------------------------------
Input Example 1:
nums = [1, 2, 3, 1]

Output Example 1:
Brute Force: True   # O(n^2)
Optimized:   True   # O(n)

-------------------------------------------------
Input Example 2:
nums = [1, 2, 3, 4]

Output Example 2:
Brute Force: False  # O(n^2)
Optimized:   False  # O(n)
=================================================

"""
# --- code is from here ---

def has_duplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def has_duplicate_fast(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]

print("Brute Force:", has_duplicate_brute(nums1))   
print("Optimized:  ", has_duplicate_fast(nums1))   

print("Brute Force:", has_duplicate_brute(nums2))   
print("Optimized:  ", has_duplicate_fast(nums2))   
