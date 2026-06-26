"""
## 5. First Repeating Element  *(Easy)*

=================================================
FIRST REPEATING ELEMENT
=================================================

Problem Statement:
You are given a list of integers. Find the
FIRST element that appears more than once
(i.e. the element whose SECOND occurrence
appears EARLIEST in the list).

If no element repeats, return -1.

Write the BRUTE-FORCE O(n^2) version FIRST,
then optimize it to O(n) using a SET.

-------------------------------------------------
Instructions:
Write TWO functions:

1. first_repeating_brute(nums)
   - Use two nested for loops:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ...
   - Return the FIRST nums[j] that matches
     some earlier nums[i].
   - If no repeat is found, return -1.
   - Time complexity:  O(n^2)
   - Space complexity: O(1)

2. first_repeating_fast(nums)
   - Create an empty SET called `seen`.
   - Use a SINGLE for loop over nums:
        - if the value is already in `seen`,
          return that value
        - otherwise, add it to `seen`
   - If the loop finishes without finding
     a repeat, return -1.
   - Time complexity:  O(n)
   - Space complexity: O(n)

Do NOT use:
   - list.count()
   - collections.Counter
   - sorted() / list.sort()

Call BOTH functions on the same input and
print both results.

-------------------------------------------------
Input Example 1:
nums = [10, 5, 3, 4, 3, 5, 6]

Output Example 1:
Brute Force: 3   # O(n^2)
Optimized:   3   # O(n)

-------------------------------------------------
Input Example 2:
nums = [1, 2, 3, 4, 5]

Output Example 2:
Brute Force: -1  # O(n^2)
Optimized:   -1  # O(n)

-------------------------------------------------
Explanation:
For [10, 5, 3, 4, 3, 5, 6]:
   scanning left to right, the first element
   whose value has already appeared earlier
   is 3 (the second 3, at index 4).
   -> 3

The brute force compares every pair, costing
O(n^2). The optimized version walks the list
ONCE, asking "is this value already in `seen`?"
in O(1) using a SET. As soon as the answer
is yes, that value is the first repeating
element, giving an overall O(n) algorithm.
=================================================

"""
# --- code is from here ---

def first_repeating_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return nums[j]
    return -1


def first_repeating_fast(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    return -1


nums1 = [10, 5, 3, 4, 3, 5, 6]
nums2 = [1, 2, 3, 4, 5]

print("Brute Force:", first_repeating_brute(nums1))
print("Optimized:  ", first_repeating_fast(nums1))

print("Brute Force:", first_repeating_brute(nums2))
print("Optimized:  ", first_repeating_fast(nums2))
