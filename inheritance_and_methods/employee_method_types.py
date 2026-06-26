"""
## 3. Employee Class with Instance, Class & Static Methods  *(Medium)*

=================================================
EMPLOYEE: INSTANCE vs CLASS vs STATIC METHODS
=================================================

Problem Statement:
Write a Python class called `Employee` that
demonstrates the THREE method types in
Python:

   1. INSTANCE method  -> takes `self`
   2. CLASS method     -> decorated with
                          @classmethod,
                          takes `cls`
   3. STATIC method    -> decorated with
                          @staticmethod,
                          takes neither

The class also has a CLASS attribute used by
the class method, and INSTANCE attributes set
in __init__.

-------------------------------------------------
Instructions:
1. Define the class:
      class Employee:
          company    = "Acme Corp"   # class attr
          raise_pct  = 5             # class attr

          def __init__(self, name, salary):
              self.name   = name
              self.salary = salary

2. INSTANCE method:
      def apply_raise(self):
          - increase self.salary by raise_pct %
            (read Employee.raise_pct)

3. CLASS method:
      @classmethod
      def set_raise_percentage(cls, new_pct):
          - cls.raise_pct = new_pct
          - this changes the class attribute
            for EVERY existing and future
            employee at once

      @classmethod
      def from_string(cls, csv_line):
          - csv_line looks like "Alice,90000"
          - split it, build and RETURN a new
            Employee instance using cls(...)
          - this is an ALTERNATE constructor.

4. STATIC method:
      @staticmethod
      def is_valid_salary(amount):
          - return True if amount is an int or
            float AND amount > 0, else False.

5. In the driver code:
      - create two employees using __init__
      - create one employee using
        Employee.from_string("Carol,75000")
      - call apply_raise() on every employee
      - change the global raise via
        Employee.set_raise_percentage(10)
      - call apply_raise() again
      - call Employee.is_valid_salary(...)
        with several values
      - print each employee's name and salary
6. Do NOT use:
   - any external library
   - global keyword

-------------------------------------------------
Input Example:
e1 = Employee("Alice", 100000)
e2 = Employee("Bob",   80000)
e3 = Employee.from_string("Carol,75000")

e1.apply_raise()                  # 5% raise
Employee.set_raise_percentage(10) # change class attr
e2.apply_raise()                  # 10% raise
e3.apply_raise()                  # 10% raise

Output Example:
Alice -> 105000.0
Bob   -> 88000.0
Carol -> 82500.0
is_valid_salary(50000)  -> True
is_valid_salary(-100)   -> False
is_valid_salary("abc")  -> False

=================================================

"""
# --- code is from here ---

class Employee:
    company = "Acme Corp"
    raise_pct = 5                    

    def __init__(self, name: str, salary: float):
        self.name = name              
        self.salary = salary            

    def apply_raise(self):
        self.salary = self.salary * (1 + Employee.raise_pct / 100)


    @classmethod
    def set_raise_percentage(cls, new_pct: int):
        cls.raise_pct = new_pct

    @classmethod
    def from_string(cls, csv_line: str):
        name, salary_str = csv_line.split(',')
        return cls(name, int(salary_str))

  
    @staticmethod
    def is_valid_salary(amount) -> bool:
        return isinstance(amount, (int, float)) and amount > 0


if __name__ == "__main__":
    e1 = Employee("Alice", 100000)
    e2 = Employee("Bob",   80000)
    e3 = Employee.from_string("Carol,75000")

    e1.apply_raise()

    Employee.set_raise_percentage(10)

    e2.apply_raise()
    e3.apply_raise()

    print(f"{e1.name} -> {e1.salary}")
    print(f"{e2.name} -> {e2.salary}")
    print(f"{e3.name} -> {e3.salary}")

    print(f"is_valid_salary(50000)  -> {Employee.is_valid_salary(50000)}")
    print(f"is_valid_salary(-100)   -> {Employee.is_valid_salary(-100)}")
    print(f"is_valid_salary(\"abc\")  -> {Employee.is_valid_salary('abc')}")
    
    