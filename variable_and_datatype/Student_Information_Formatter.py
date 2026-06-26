'''
Q. Write a Python program that:
   • takes student name,
   • branch,
   • CGPA,
   • and prints a formatted report using f-strings.
'''
# --- code is from here ---
name = input("Enter student name: ")
branch = input("Enter branch: ")
cgpa = float(input("Enter CGPA: "))

# Print formatted report using f-strings
print("\n--- Student Report ---")
print(f"Name   : {name}")
print(f"Branch : {branch}")
print(f"CGPA   : {cgpa:.2f}")
