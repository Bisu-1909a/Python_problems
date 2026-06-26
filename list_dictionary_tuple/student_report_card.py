"""
## 5. Student Report Card Generator  *(Hard)*

=================================================
STUDENT REPORT CARD GENERATOR
=================================================

Problem Statement:
You are given a LIST of TUPLES, where each
tuple represents one exam record:
        (student_name, subject, marks)

A single student may appear MULTIPLE times,
once per subject.

Write a Python program that builds a REPORT
CARD as a dictionary in the following form:

   {
      student_name: {
          "subjects": { subject: marks, ... },
          "total":   <sum of marks>,
          "average": <average marks>,
          "grade":   <A / B / C / F>
      },
      ...
   }

Grading rule (based on AVERAGE marks):
   - average >= 90  -> "A"
   - average >= 75  -> "B"
   - average >= 50  -> "C"
   - else           -> "F"

Finally, print the name of the student with
the HIGHEST average.

-------------------------------------------------
Instructions:
1. Take a list of (name, subject, marks)
   tuples as input.
2. Build the report card dictionary using
   for loops only.
3. Use nested dictionaries to store per-subject
   marks for each student.
4. Compute total, average, and grade for each
   student.
5. Use a for loop to find the student with the
   highest average.
6. Do NOT use:
   - collections module
   - pandas / numpy
   - sorted() / max() with key= / lambda
7. Print:
   - the report card dictionary
   - the topper's name and their average

-------------------------------------------------
Input Example:
[
  ("Alice", "Math",    95),
  ("Alice", "Science", 88),
  ("Bob",   "Math",    70),
  ("Bob",   "Science", 60),
  ("Carol", "Math",    50),
  ("Carol", "Science", 40),
]

Output Example:
{
  'Alice': {
      'subjects': {'Math': 95, 'Science': 88},
      'total': 183, 'average': 91.5, 'grade': 'A'
  },
  'Bob': {
      'subjects': {'Math': 70, 'Science': 60},
      'total': 130, 'average': 65.0, 'grade': 'C'
  },
  'Carol': {
      'subjects': {'Math': 50, 'Science': 40},
      'total': 90,  'average': 45.0, 'grade': 'F'
  }
}
Topper: Alice (average = 91.5)

-------------------------------------------------
Explanation:
For Alice:
   subjects -> Math=95, Science=88
   total    -> 95 + 88 = 183
   average  -> 183 / 2 = 91.5
   grade    -> 91.5 >= 90 -> 'A'

Repeat for Bob and Carol. The student with the
highest average is Alice, so she is the topper.
=================================================

"""
# --- code is from here ---

records = [("Biswajeet", "Math", 95),("Biswajeet", "Science", 85),
    ("Som", "Math", 70),("Som", "Science", 60),
    ("Prem", "Math", 40),("Prem", "Science", 55)]

report = {}

for name, subject, marks in records:
    if name not in report:
        report[name] = {"subjects": {}, "total": 0, "average": 0, "grade": ""}
    report[name]["subjects"][subject] = marks

for name in report:
    subs = report[name]["subjects"]
    total = 0                        # sum of all subject marks
    count = 0                        # number os subjects
    for s in subs:
        total += subs[s]
        count += 1
    avg = total / count              # averge mark obtained

    report[name]["total"] = total
    report[name]["average"] = avg

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"

    report[name]["grade"] = grade

# Find topper
top_name = None
top_avg = 0

for name in report:
    if report[name]["average"] >= top_avg:
        top_avg = report[name]["average"]
        top_name = name

print("Report Card:", report)
print("Topper:", top_name, "with average", top_avg)
