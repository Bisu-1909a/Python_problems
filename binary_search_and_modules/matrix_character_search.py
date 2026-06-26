"""
## 7. Find a Character in a 2D Matrix  *(Easy)*

=================================================
SEARCH CHARACTER IN A 2D MATRIX
=================================================

Problem Statement:
A 2D matrix of characters is generated using
the following code:

   table = [list("abcd"), list("efgh"), list("ijkl")]

This produces:

   a b c d
   e f g h
   i j k l

Write a Python program that takes a single
TARGET CHARACTER as input and prints the
ROW INDEX and COLUMN INDEX (0-based) of the
character in the matrix.

If the character is NOT present, print
"Not found".

-------------------------------------------------
Input Example 1:
Enter target character: h

Output Example 1:
1 3

-------------------------------------------------
Input Example 2:
Enter target character: z

Output Example 2:
Not found

-------------------------------------------------
Explanation:
table = [
   ['a', 'b', 'c', 'd'],   # row 0
   ['e', 'f', 'g', 'h'],   # row 1
   ['i', 'j', 'k', 'l'],   # row 2
]
'h' is in row 1, column 3 -> print "1 3".
'z' does not exist in the matrix -> print
"Not found".
=================================================

"""
# --- code is from here ---

table = [list("abcd"), list("efgh"), list("ijkl")]
target = input("Enter target character: ")

found = False

for row in range(len(table)):
    for col in range(len(table[row])):
        if table[row][col] == target:
            found = True
            print(f"Found in row : {row } and colume : {col}\n({row},{col})")
            break   
         
    if found:
        break       
if not found:
    print("Not found")
    