"""
## 3. Abstract Shape with ABC Module  *(Medium)*

=================================================
ABSTRACT SHAPE (USING abc MODULE)
=================================================

Problem Statement:
Use Python's built-in `abc` module to define a
TRUE abstract base class called `Shape`. Any
child class that does NOT implement every
abstract method must NOT be instantiable — the
abc module enforces this for you at object
creation time.

Children to build:
   Circle
   Rectangle
   Triangle

Each child must implement two abstract
methods: `area()` and `perimeter()`.

This problem teaches ABSTRACTION:
   - hiding the details behind a clean
     contract
   - forcing all children to follow that
     contract
   - the caller writes ONE function that
     works on ANY shape

-------------------------------------------------
Instructions:
1. Import the abc module:
      from abc import ABC, abstractmethod

2. Define the abstract base class:
      class Shape(ABC):
          def __init__(self, name):
              self.name = name

          @abstractmethod
          def area(self):
              pass

          @abstractmethod
          def perimeter(self):
              pass

3. Define the children Circle, Rectangle and
   Triangle. Each one:
      - calls super().__init__("Circle" / ...)
      - implements area() and perimeter()
        with the appropriate formula
4. In the driver code:
      - try to instantiate Shape("nope")
        inside a try / except TypeError block
        to show that Python REFUSES because
        the abstract methods are not
        implemented.
      - create at least one of each child
      - put them in a LIST and call area() and perimeter()
            on each one in a for loop, showing that
            on each in a for loop.
5. Do NOT use:
   - the math module (use 3.14159 as PI)
   - any external library
   - isinstance() / type() in the for loop

-------------------------------------------------
Input Example:
Shapes("nope")
shapes = [
   Circle(5),
   Rectangle(4, 6),
   Triangle(3, 4, 5),
]

Output Example:
Cannot create Shape directly:
   TypeError: Can't instantiate abstract class
   Shape with abstract methods area, perimeter

Circle    -> area=78.53975, perimeter=31.4159
Rectangle -> area=24,       perimeter=20
Triangle  -> area=6.0,      perimeter=12

-------------------------------------------------
Explanation:
- The `@abstractmethod` decorator marks
  area() and perimeter() as REQUIRED methods.
- Any class that inherits Shape MUST
  implement them or it cannot be
  instantiated.
- describe() uses the abstract methods but
  ITSELF is concrete. It works for any shape
  because of polymorphism — exactly the
  abstraction we want.
=================================================

"""
# --- code is from here ---

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


print("Cannot create Shape directly:")

try:
    test_shape = Shape("nope")
    
except TypeError as e:
    print(f"   {type(e).__name__}: {e}\n")


my_shapes = [ Circle(5) , Rectangle(4, 6) , Triangle(3, 4, 5) ]

for shp in my_shapes:
    a = shp.area()
    p = shp.perimeter()
    print(f"{shp.name:10} -> area={a:.2f} \t perimeter={p:.2f}")
    
    