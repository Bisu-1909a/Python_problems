"""
## 1. Two Sum (Find Two Numbers that Add to Target)  *(Easy)*

=================================================
TWO SUM
=================================================

Problem Statement:
You are given a list of integers and a target
integer. Find the INDICES of TWO numbers in
the list that add up to exactly the target.

Each input has exactly ONE valid answer, and
you cannot use the same element twice.

The point of this problem is to FIRST write
the simple O(n^2) brute-force solution, and
THEN optimize it to an O(n) solution using a
DICTIONARY (hash map).

-------------------------------------------------
Instructions:
Write TWO functions:

1. two_sum_brute(nums, target)
   - Use two nested for loops to try every
     pair (i, j) with i < j.
   - Return the tuple (i, j) when
     nums[i] + nums[j] == target.
   - Time complexity:  O(n^2)
   - Space complexity: O(1)

2. two_sum_fast(nums, target)
   - Use a SINGLE for loop and a DICTIONARY
     that maps   value -> index.
   - For each element x at index i, compute
     the complement = target - x and check
     whether it already exists in the
     dictionary.
   - If yes, return (dict[complement], i).
   - Otherwise, store dict[x] = i and move on.
   - Time complexity:  O(n)
   - Space complexity: O(n)

Do NOT use:
   - sorted() / list.sort()
   - itertools
   - any external library

Call BOTH functions on the same input and
print:
   - the result of the brute-force version
   - the result of the optimized version
   - the time complexity of each version

-------------------------------------------------
Input Example 1:
nums   = [2, 7, 11, 15]
target = 9

Output Example 1:
Brute Force: (0, 1)   # O(n^2)
Optimized:   (0, 1)   # O(n)

-------------------------------------------------
Input Example 2:
nums   = [3, 2, 4]
target = 6

Output Example 2:
Brute Force: (1, 2)   # O(n^2)
Optimized:   (1, 2)   # O(n)

-------------------------------------------------
Explanation:
For [2, 7, 11, 15] and target = 9:
   2 + 7 = 9
   indices -> (0, 1)

Brute force tries every pair, taking O(n^2)
time. The optimized version scans the list
ONCE and uses a dictionary to remember every
value it has already seen. As soon as the
complement (target - current) is found in
the dictionary, the answer is returned in
O(1) time, giving an overall O(n) algorithm.
=================================================

"""
# --- code is from here ---

def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_fast(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        comp = target - x
        if comp in seen:
            return (seen[comp], i)
        seen[x] = i
    return None

nums = [2, 7, 11, 15]
target = 9
print("Brute Force:", two_sum_brute(nums, target), "# O(n^2)")
print("Optimized:  ", two_sum_fast(nums, target), "# O(n)")

nums = [3, 2, 4]
target = 6
print("Brute Force:", two_sum_brute(nums, target), "# O(n^2)")
print("Optimized:  ", two_sum_fast(nums, target), "# O(n)")
