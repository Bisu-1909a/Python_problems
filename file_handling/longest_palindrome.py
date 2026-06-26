"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
# --- code is from here ---

def longest_palindromes(filename):
    longest = []
    max_len = 0

    with open(filename, "r") as f:
        for word in f:
            w = word.strip().lower()
            if w == w[::-1]:  # palindrome check
                if len(w) > max_len:
                    longest = [w]
                    max_len = len(w)
                elif len(w) == max_len:
                    longest.append(w)

    return max_len, longest

    length, words = longest_palindromes("sowpods.txt")
    print("Longest palindrome length:", length)
    for w in words:
        print(w)
        