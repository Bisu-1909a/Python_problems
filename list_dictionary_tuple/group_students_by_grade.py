"""
## 4. Group Students by Grade  *(Medium)*

=================================================
GROUP STUDENTS BY GRADE
=================================================

Problem Statement:
You are given a LIST of TUPLES, where each
tuple represents a student in the form:
        (student_name, grade)

Write a Python program that groups the
students by their grade into a DICTIONARY where:
   - key   -> grade
   - value -> list of student names having
              that grade

-------------------------------------------------
Input Example 1:
[("Alice", "A"), ("Bob", "B"), ("Carol", "A"),
 ("Dan", "C"), ("Eve", "B"), ("Frank", "A")]

Output Example 1:
{
  'A': ['Alice', 'Carol', 'Frank'],
  'B': ['Bob', 'Eve'],
  'C': ['Dan']
}

-------------------------------------------------
Input Example 2:
[("Sam", "A")]

Output Example 2:
{'A': ['Sam']}

-------------------------------------------------
Explanation:
Walk through the list and place each student
into the bucket of their grade. Students with
the same grade end up in the same list, in
the order they were seen.
=================================================

"""
# --- code is from here ---

students = [("Biswajeet", "A"),("Som", "B"),
            ("Prem", "A"),("Sourav", "C"),("Nitish", "B")]

result = {}

for name, grade in students:
    if grade in result:
        result[grade].append(name)
    else:
        result[grade] = [name]

print(result)
