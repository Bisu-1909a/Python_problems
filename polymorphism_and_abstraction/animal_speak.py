"""
## 1. Animal Speak — Polymorphism Basics  *(Easy)*

=================================================
ANIMAL SPEAK (POLYMORPHISM BASICS)
=================================================

Problem Statement:
Build a small set of classes that demonstrate
POLYMORPHISM — the idea that the SAME method
call (`speak()`) produces DIFFERENT behaviour
depending on the actual object's class.

Classes to build:
   Animal  (parent)
   ├── Dog
   ├── Cat
   └── Cow

Each child class OVERRIDES the speak()
method with its own sound.

-------------------------------------------------
Instructions:
1. Define the parent class:
      class Animal:
          def __init__(self, name):
              self.name = name

          def speak(self):
              print(f"{self.name} makes a sound")

2. Define three child classes:
      class Dog(Animal):
          def speak(self):
              print(f"{self.name} says Woof")

      class Cat(Animal):
          def speak(self):
              print(f"{self.name} says Meow")

      class Cow(Animal):
          def speak(self):
              print(f"{self.name} says Moo")

3. In the driver code:
      - put one Dog, one Cat, and one Cow
        object into a LIST called `animals`
      - use a SINGLE for loop to call
        animal.speak() on each object
      - Python automatically picks the right
        version based on the object's class —
        that is polymorphism.
4. Do NOT use:
   - isinstance() / type() checks to decide
     what to print
   - if / elif chains to pick a sound

-------------------------------------------------
Input Example:
animals = [
   Dog("Buddy"),
   Cat("Whiskers"),
   Cow("Bessie"),
]

Output Example:
Buddy says Woof
Whiskers says Meow
Bessie says Moo

-------------------------------------------------
Explanation:
- The for loop calls the SAME method name
  speak() on every object.
- Each object responds DIFFERENTLY based on
  its own class.
- The caller does NOT need to know whether
  the object is a Dog, Cat, or Cow — this is
  the heart of polymorphism.
=================================================

"""
# --- code is from here ---

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow")


class Cow(Animal):
    def speak(self):
        print(f"{self.name} says Moo")


animals = [ Dog("Buddy") , Cat("Whiskers") , Cow("Bessie") ]
for a in animals:
    a.speak()
    