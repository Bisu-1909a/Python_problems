"""
## 5. Employee Database Manager  *(Hard)*

=================================================
EMPLOYEE DATABASE MANAGER
=================================================

Problem Statement:
You are given a LIST of TUPLES, where each
tuple represents an employee record:
        (emp_id, name, department, salary)

Build a small employee database using FOUR
Python FUNCTIONS that operate on this data:

   1. build_database(records) -> dict
        Convert the list of tuples into a
        dictionary keyed by emp_id, where the
        value is another dictionary:
            {
              "name": ..., "department": ...,
              "salary": ...
            }

   2. get_departments(db) -> set
        Return a SET of all unique departments
        present in the database.

   3. department_totals(db) -> dict
        Return a dictionary mapping each
        department to the TOTAL salary paid
        in that department.

   4. top_earner(db) -> tuple
        Return a tuple (emp_id, name, salary)
        of the employee with the HIGHEST salary.

-------------------------------------------------
Instructions:
1. Implement each function separately.
2. Use only:
   - list, tuple, dictionary, set
   - for loops
   - basic arithmetic and comparisons
3. Do NOT use:
   - pandas / numpy
   - collections module
   - sorted() / max() / min() with key=
   - lambda functions
4. Call all four functions on the sample input
   and print their results.

-------------------------------------------------
Input Example:
[
  (101, "Alice",   "Engineering", 90000),
  (102, "Bob",     "Sales",       60000),
  (103, "Carol",   "Engineering", 95000),
  (104, "Dan",     "HR",          55000),
  (105, "Eve",     "Sales",       70000),
]

Output Example:
Database:
{
  101: {'name': 'Alice', 'department': 'Engineering', 'salary': 90000},
  102: {'name': 'Bob',   'department': 'Sales',       'salary': 60000},
  103: {'name': 'Carol', 'department': 'Engineering', 'salary': 95000},
  104: {'name': 'Dan',   'department': 'HR',          'salary': 55000},
  105: {'name': 'Eve',   'department': 'Sales',       'salary': 70000}
}

Departments: {'Engineering', 'Sales', 'HR'}

Department Totals:
{'Engineering': 185000, 'Sales': 130000, 'HR': 55000}

Top Earner: (103, 'Carol', 95000)

-------------------------------------------------
Explanation:
- build_database converts each tuple into a
  nested dictionary keyed by emp_id.
- get_departments collects unique departments
  using a set.
- department_totals walks the database with a
  for loop and accumulates salary per
  department in a dictionary.
- top_earner walks the database once, keeps
  track of the highest salary seen so far,
  and returns the matching record as a tuple.
=================================================

"""
# --- code is from here ---

records = [(101, "Alice", "Engineering", 90000),(102, "Bob", "Sales", 60000),(103, "Carol", "Engineering", 95000), (104, "Dan", "HR", 55000),    (105, "Eve", "Sales", 70000)]

def build_database(records):
    db = {}
    for emp_id, name, dept, sal in records:
        db[emp_id] = {
            "name": name,
            "department": dept,
            "salary": sal
        }
    return db


def get_departments(db):
    depts = set()
    for emp_id in db:
        depts.add(db[emp_id]["department"])
    return depts


def department_totals(db):
    totals = {}
    for emp_id in db:
        dept = db[emp_id]["department"]
        sal = db[emp_id]["salary"]
        if dept in totals:
            totals[dept] += sal
        else :
           totals[dept] = sal
    return totals


def top_earner(db):
    top_id = None
    top_name = ""
    top_salary = 0
    for emp_id in db:
        sal = db[emp_id]["salary"]
        if sal >= top_salary:
            top_salary = sal
            top_id = emp_id
            top_name = db[emp_id]["name"]
    return (top_id, top_name, top_salary)

db = build_database(records)
print("Database:", db)

depts = get_departments(db)
print("Departments:", depts)

totals = department_totals(db)
print("Department Totals:", totals)

top = top_earner(db)
print("Top Earner:", top)
