"""
## 2. Pair with Given Difference  *(Easy)*

=================================================
PAIR WITH GIVEN DIFFERENCE
=================================================

Problem Statement:
You are given a list of distinct integers and
a positive integer K. Return TRUE if there
exist two numbers in the list whose ABSOLUTE
DIFFERENCE is exactly K, otherwise return
FALSE.

Write the BRUTE-FORCE O(n^2) version FIRST,
then optimize it to O(n) using a SET.

-------------------------------------------------
Instructions:
Write TWO functions:

1. has_pair_brute(nums, k)
   - Use two nested for loops to try every
     pair (i, j) with i < j.
   - Return True as soon as
     abs(nums[i] - nums[j]) == k.
   - If no pair is found, return False.
   - Time complexity:  O(n^2)
   - Space complexity: O(1)

2. has_pair_fast(nums, k)
   - Build a SET of all numbers in the list.
   - Use a SINGLE for loop over the list.
     For each number x, check whether
        (x + k) is in the set
        or (x - k) is in the set.
   - Return True as soon as a match is found,
     otherwise False.
   - Time complexity:  O(n)
   - Space complexity: O(n)

Do NOT use:
   - sorted() / list.sort()
   - itertools.combinations
   - any external library

Call BOTH functions on the same input and
print both results.

-------------------------------------------------
Input Example 1:
nums = [1, 5, 3, 4, 2]
k    = 3

Output Example 1:
Brute Force: True   # O(n^2)
Optimized:   True   # O(n)

-------------------------------------------------
Input Example 2:
nums = [8, 12, 16, 4, 0, 20]
k    = 9

Output Example 2:
Brute Force: False  # O(n^2)
Optimized:   False  # O(n)

-------------------------------------------------
Explanation:
For [1, 5, 3, 4, 2] and k = 3:
   |5 - 2| = 3  -> a valid pair exists
   -> True

The brute force checks every pair in O(n^2).
The optimized version stores the numbers in
a SET so that for each number x we can ask
"is x + k present?" in O(1), giving an
overall O(n) algorithm.
=================================================

"""
# --- code is from here ---

def has_pair_brute(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                return True
    return False

def has_pair_fast(nums, k):
    seen = set(nums)   # store all numbers
    for x in nums:
        if (x + k) in seen or (x - k) in seen:
            return True
    return False

nums = [1, 5, 3, 4, 2]
k = 3
print("Brute Force:", has_pair_brute(nums, k))
print("Optimized:  ", has_pair_fast(nums, k))

nums = [8, 12, 16, 4, 0, 20]
k = 9
print("Brute Force:", has_pair_brute(nums, k))
print("Optimized:  ", has_pair_fast(nums, k))
