"""
## 1. Animal -> Dog with super()  *(Easy)*

=================================================
ANIMAL AND DOG (INHERITANCE BASICS)
=================================================

Problem Statement:
Write two classes that demonstrate the
simplest case of single inheritance:

   - Animal       (PARENT class)
   - Dog          (CHILD class that inherits
                    from Animal)

The Dog class must EXTEND Animal, not replace
it. Use the `super()` keyword to call the
parent's `__init__` instead of repeating the
code in the child class.

-------------------------------------------------
Instructions:
1. Define the parent class:
      class Animal:
          def __init__(self, name, sound):
              self.name  = name
              self.sound = sound

          def speak(self):
              print(f"{self.name} says {self.sound}")

2. Define the child class:
      class Dog(Animal):
          def __init__(self, name, breed):
              - call super().__init__(name, "Woof")
                so the parent stores name and sound
              - then set self.breed = breed

          def describe(self):
              print(f"{self.name} is a {self.breed}")

3. In the driver code:
      - create one Animal (e.g. a cat) and call
        speak()
      - create at least TWO Dog objects of
        different breeds and call BOTH speak()
        (inherited from Animal) AND describe()
        (defined on Dog)
4. Do NOT use:
   - any external library
   - manually copying parent __init__ code
     into the child (must use super())

-------------------------------------------------
Input Example:
a = Animal("Cat", "Meow")
d1 = Dog("Buddy", "Labrador")
d2 = Dog("Rex",   "Beagle")

Output Example:
Cat says Meow
Buddy says Woof
Buddy is a Labrador
Rex says Woof
Rex is a Beagle

=================================================

"""
# --- code is from here ---

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def describe(self):
        print(f"{self.name} is a {self.breed}")


if __name__ == "__main__":
    c = Animal("Cat", "Meow")
    c.speak()

    d1 = Dog("Buddy", "Labrador")
    d1.speak()  
    d1.describe() 

    d2 = Dog("Rex", "Beagle")
    d2.speak()   
    d2.describe() 
    