'''
 Q. Write a Python program that:
    • demonstrates why 0.1 + 0.2 is not exactly equal to 0.3,
    • prints the result,
    • explains the issue using comments.
'''
# --- code is from here ---

x = 0.1
y = 0.2
z = 0.3

result = x + y

print("0.1 + 0.2 =", result)
print("Is 0.1 + 0.2 equal to 0.3?", result == z)

print('''
 Explanation:
            Computers store decimal numbers in binary (base-2).
            Some decimals like 0.1 and 0.2 cannot be represented exactly in binary.
            They are stored as very close approximations.
            When added, the tiny errors accumulate, so 0.1 + 0.2 becomes 0.30000000000000004.
            That is why the comparison with 0.3 returns False.
 '''
)
