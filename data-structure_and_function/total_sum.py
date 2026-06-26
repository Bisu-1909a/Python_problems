"""
## 1. Sum of Any Number of Values  *(Easy)*

=================================================
SUM USING *ARGS
=================================================

Problem Statement:
Write a Python FUNCTION called `total_sum`
that accepts ANY number of numeric arguments
using *args and returns their total sum.

The function must also accept a list or tuple
of numbers when unpacked with the * operator
at the call site.

-------------------------------------------------
Input Example:
total_sum(1, 2, 3, 4, 5)
total_sum(*[10, 20, 30])
total_sum()

Output Example:
Sum: 15
Sum: 60
Sum: 0

-------------------------------------------------
Explanation:
*args collects all positional arguments into
a tuple. The function iterates over that tuple
with a for loop and adds the values together.
=================================================

"""
# --- code is from here ---

def total_sum(*args):
    total = 0

    for num in args:
        total += num
    return total

print("Sum:", total_sum(1, 2, 3, 4, 5))
print("Sum:", total_sum(*[10, 20, 30]))
print("Sum:", total_sum())
