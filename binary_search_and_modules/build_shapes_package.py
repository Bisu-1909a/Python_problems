"""
## 4. Build a Python PACKAGE: shapes  *(Medium)*

=================================================
BUILD A PYTHON PACKAGE
=================================================

Problem Statement:
Create a Python PACKAGE called `shapes` that
contains multiple MODULES (one per shape).
Then write a driver script that IMPORTS from
the package and uses the modules together.

Folder structure to create:

   shapes/
       __init__.py
       circle.py
       rectangle.py
       triangle.py
   use_shapes.py

Module contents:

   circle.py
       - area(radius)         -> float
       - perimeter(radius)    -> float

   rectangle.py
       - area(length, width)      -> float
       - perimeter(length, width) -> float

   triangle.py
       - area(base, height)             -> float
       - perimeter(side_a, side_b, side_c) -> float

   __init__.py
       - Re-export the three modules so
         `from shapes import circle, rectangle, triangle`
         works at the package level.

-------------------------------------------------
Instructions:
1. Build the folder structure exactly as above.
2. In use_shapes.py, demonstrate THREE import
   styles:
      - import shapes
      - from shapes import circle
      - from shapes.rectangle import area as rect_area

-------------------------------------------------
Input Example (in use_shapes.py):
circle radius      = 5
rectangle (l, w)   = (4, 6)
triangle base/ht   = (4, 3)  for area
triangle sides     = (3, 4, 5) for perimeter

Output Example:
('circle',    78.53975, 31.4159)
('rectangle', 24,       20)
('triangle',  6.0,      12)

Areas: {'circle': 78.53975, 'rectangle': 24, 'triangle': 6.0}

-------------------------------------------------
Explanation:
A PACKAGE is just a folder containing an
__init__.py file plus one or more MODULES.
This problem teaches you how to:
   - structure a package
   - re-export modules from __init__.py
   - import a package, a module from a
     package, and a specific symbol from a
     module inside a package.
=================================================

"""