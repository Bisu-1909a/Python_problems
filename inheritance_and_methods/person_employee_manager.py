"""
## 5. Person -> Employee -> Manager (Multi-Level Inheritance)  *(Hard)*

=================================================
PERSON -> EMPLOYEE -> MANAGER
(MULTI-LEVEL INHERITANCE + METHOD TYPES)
=================================================

Problem Statement:
Build a THREE-LEVEL inheritance chain:

   Person          (level 1 — base)
   └── Employee    (level 2 — inherits Person)
       └── Manager (level 3 — inherits Employee)

Each level ADDS its own NEW methods and
attributes. NO method on the parent should be
OVERRIDDEN — every child must extend its
parent ONLY by introducing new behaviour, and
must call super().__init__() to reuse the
parent's constructor.

This problem teaches:
   - multi-level inheritance
   - super().__init__() in every level
   - instance / class / static method types
   - one class can use methods INHERITED from
     ALL its ancestors (without overriding)

-------------------------------------------------
Instructions:

Person (level 1)
   class attribute is:
       species = "Homo sapiens"

   __init__(self, name, age):
       self.name = name
       self.age  = age

   greet(self) -> str:
       return f"Hi, I'm {self.name}, age {self.age}"

   @staticmethod
   def is_adult(age) -> bool:
       return age >= 18

Employee (level 2, inherits Person)
   class attribute is:
       company   = "Acme Corp"
       bonus_pct = 5

   __init__(self, name, age, emp_id, salary):
       - call super().__init__(name, age)
       - store emp_id and salary

   work_intro(self) -> str:
       return (f"I work at {Employee.company} "
               f"as id {self.emp_id}")

   apply_bonus(self):
       self.salary += self.salary * Employee.bonus_pct / 100

   @classmethod
   def set_bonus(cls, new_pct):
       cls.bonus_pct = new_pct

Manager (level 3, inherits Employee)
   __init__(self, name, age, emp_id, salary, team):
       - call super().__init__(name, age, emp_id, salary)
       - store team (a LIST of Employee objects)

   add_member(self, employee):
       - append to self.team

   team_intro(self) -> str:
       return f"I lead a team of {len(self.team)} people."

   team_total_salary(self) -> float:
       - return self's salary PLUS the sum of
         every team member's salary
       (use a for loop to walk self.team)

In the driver code:
   - create one Person and call greet()
   - create two Employee objects, and on each
     call greet() (inherited from Person) AND
     work_intro() (defined in Employee)
   - create one Manager, add the two Employee
     objects to her team, and call
     greet()      (inherited from Person)
     work_intro() (inherited from Employee)
     team_intro() (defined in Manager)
   - call apply_bonus() on every employee
     INCLUDING the manager
     (Manager inherits apply_bonus from
      Employee unchanged)
   - call Employee.set_bonus(10) to change
     the class-wide bonus percentage, then
     call apply_bonus() again to confirm BOTH
     subclasses see the new value
   - call Person.is_adult(age) with several
     ages, including ones from the objects
   - call m.team_total_salary() and print it

Do NOT use:
   - any external library
   - global keyword
   - method overriding (each child must only
     ADD new methods, not redefine any of the
     parent's methods)
   - manually rewriting parent __init__ logic
     in the child (must use super())

-------------------------------------------------
Input Example:
p = Person("Sam", 17)

e1 = Employee("Alice", 25, "E001", 100000)
e2 = Employee("Bob",   30, "E002", 80000)

m  = Manager("Carol", 40, "M001", 150000, [])
m.add_member(e1)
m.add_member(e2)

e1.apply_bonus()
e2.apply_bonus()
m.apply_bonus()                      # inherited from Employee
Employee.set_bonus(10)
m.apply_bonus()                      # inherited, now at 10%

Output Example (representative):
Hi, I'm Sam, age 17

Hi, I'm Alice, age 25
I work at Acme Corp as id E001

Hi, I'm Bob, age 30
I work at Acme Corp as id E002

Hi, I'm Carol, age 40
I work at Acme Corp as id M001
I lead a team of 2 people.

Alice salary -> 105000.0
Bob   salary -> 84000.0
Carol salary -> 157500.0   # one 5% bonus
Carol salary -> 173250.0   # one 10% bonus on top

is_adult(17) -> False
is_adult(25) -> True

Team total salary -> 173250.0 + 105000.0 + 84000.0

=================================================

"""
# --- code is from here ---

class Person:
    species = "Homo sapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        return f"Hi, I'm {self.name}, age {self.age}"
    
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18


class Employee(Person):
    company = "Acme Corp"
    bonus_pct = 5
    
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age) 
        self.emp_id = emp_id
        self.salary = salary
    
    def work_intro(self) -> str:
        return f"I work at {Employee.company} as id {self.emp_id}"
    
    def apply_bonus(self):
        self.salary += self.salary * Employee.bonus_pct / 100
    
    @classmethod
    def set_bonus(cls, new_pct: int):
        cls.bonus_pct = new_pct


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, team):
        super().__init__(name, age, emp_id, salary) 
        self.team = team  
    
    def add_member(self, employee: Employee):
        self.team.append(employee)
    
    def team_intro(self) -> str:
        return f"I lead a team of {len(self.team)} people."
    
    def team_total_salary(self) -> float:
        total = self.salary
        for member in self.team:
            total += member.salary
        return total


if __name__ == "__main__":
    p = Person("Sam", 17)
    print(p.greet())                  
    print()
 
    e1 = Employee("Alice", 25, "E001", 100000)
    e2 = Employee("Bob", 30, "E002", 80000)
    
    print(e1.greet())                   
    print(e1.work_intro())            
    print()
    
    print(e2.greet())                 
    print(e2.work_intro())             
    print()
    
    
    m = Manager("Carol", 40, "M001", 150000, [])
    m.add_member(e1)                  
    m.add_member(e2)
    
    print(m.greet())                  
    print(m.work_intro())              
    print(m.team_intro())              
    print()
    
    e1.apply_bonus()
    e2.apply_bonus()
    m.apply_bonus()                   
    
    Employee.set_bonus(10)
    m.apply_bonus()                
    
    print(f"Alice salary -> {e1.salary}")
    print(f"Bob   salary -> {e2.salary}")
    print(f"Carol salary -> {m.salary}")
    print()
    
    print(f"is_adult(17) -> {Person.is_adult(17)}")
    print(f"is_adult(25) -> {Person.is_adult(25)}")
    print()
    
    total = m.team_total_salary()
    print(f"Team total salary -> {total}")
    