"""
## 4. Count Pairs with Given Sum  *(Easy)*

=================================================
COUNT PAIRS WITH GIVEN SUM
=================================================

Problem Statement:
You are given a list of integers and a target
integer. Count the TOTAL number of UNORDERED
PAIRS (i, j) with i < j such that
        nums[i] + nums[j] == target.

Write the BRUTE-FORCE O(n^2) version FIRST,
then optimize it to O(n) using a DICTIONARY.

-------------------------------------------------
Instructions:
Write TWO functions:

1. count_pairs_brute(nums, target)
   - Use two nested for loops to consider
     every pair (i, j) with i < j.
   - Increment a counter when
     nums[i] + nums[j] == target.
   - Return the counter.
   - Time complexity:  O(n^2)
   - Space complexity: O(1)

2. count_pairs_fast(nums, target)
   - Create an empty DICTIONARY `freq` that
     maps   value -> how many times it has
     been seen so far.
   - Initialize count = 0.
   - Use a SINGLE for loop over nums:
        - complement = target - x
        - if complement is in freq:
              count += freq[complement]
        - then add x to freq:
              freq[x] = freq.get(x, 0) + 1
   - Return count.
   - Time complexity:  O(n)
   - Space complexity: O(n)

Do NOT use:
   - itertools.combinations
   - collections.Counter
   - sorted() / list.sort()

Call BOTH functions on the same input and
print both results.

-------------------------------------------------
Input Example 1:
nums   = [1, 5, 7, -1, 5]
target = 6

Output Example 1:
Brute Force: 3   # O(n^2)
Optimized:   3   # O(n)

-------------------------------------------------
Input Example 2:
nums   = [1, 1, 1, 1]
target = 2

Output Example 2:
Brute Force: 6   # O(n^2)
Optimized:   6   # O(n)

-------------------------------------------------
Explanation:
For [1, 5, 7, -1, 5] and target = 6:
   (1, 5)   -> indices (0, 1)
   (1, 5)   -> indices (0, 4)
   (7, -1)  -> indices (2, 3)
   Total pairs = 3.

For [1, 1, 1, 1] and target = 2:
   every pair (i, j) with i < j adds to 2.
   With 4 ones, the number of such pairs is
   4*3/2 = 6.

The brute force checks every pair, costing
O(n^2). The optimized version keeps a
running frequency map and, for each new
element x, asks "how many earlier elements
equal (target - x)?". That answer is
available in O(1) from the dictionary, so
the overall algorithm runs in O(n).
=================================================

"""
# --- code is from here ---

def pairs_brute(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                count += 1
    return count


def pairs_fast(nums, target):
    freq = {}
    count = 0
    for x in nums:
        comp = target - x
        if comp in freq:
            count += freq[comp]
        freq[x] = freq.get(x, 0) + 1
    return count


nums1 = [1, 5, 7, -1, 5]
target1 = 6

nums2 = [1, 1, 1, 1]
target2 = 2

print("Brute Force:", pairs_brute(nums1, target1))
print("Optimized:  ", pairs_fast(nums1, target1))

print("Brute Force:", pairs_brute(nums2, target2))
print("Optimized:  ", pairs_fast(nums2, target2))
