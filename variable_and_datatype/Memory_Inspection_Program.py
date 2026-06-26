'''
Q.Write a Python program that:
  • creates two variables pointing to the same integer,
  • prints their memory addresses using id().
'''
# --- code is from here ---

a = 100
b = a   # b points to the same integer as a

print("Memory address of a:", id(a))
print("Memory address of b:", id(b))
