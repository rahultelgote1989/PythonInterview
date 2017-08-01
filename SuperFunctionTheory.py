"""
In Python, super() built-in has two major use cases:
1. Allows us to avoid using base class explicitly
2. Working with Multiple Inheritance
"""

## super() with single inheritance
class Mammal(object):

	def __init__(self, mammalName):
		print(mammalName, "is going through class: Mammal")


class Dog(Mammal):
	def __init__(self):
		print("Dog is going through class: Dog")
		super().__init__('Dog')

d1 = Dog()

"""
Since, we do not need to specify the name of the base class if we use super(), 
we can easily change the base class for Dog method easily (if we need to).
The super() builtin returns a proxy object, a substitute object that has ability 
to call method of the base class via delegation. This is called indirection 
(ability to reference base object with super()) Since the indirection is 
computed at the runtime, we can use point to different base class at different
time (if we need to).
"""

## super() with multiple inheritance:

class Animal:
	def __init__(self, animalName):
		print(animalName, "is going through class: Animal")

class Mammal(Animal):
	def __init__(self, mammalName):
		print(mammalName, "is going through class: Mammal")
		super().__init__('Mammal')

class NonWingedMammal(Mammal):
	def __init__(self, NonWingedMammalName):
		print(NonWingedMammalName, "is going through class: NonWingedMammal")
		super().__init__('NonWingedMammal')

class NonMarineMammal(Mammal):
	def __init__(self, NonMarineMammalName):
		print(NonMarineMammalName, "is going through class: NonMarineMammal")
		super().__init__('NonMarineMammal')

class Cat(NonMarineMammal, NonWingedMammal):
	def __init__(self):
		print("Cat is going through class: Cat")
		super().__init__('Cat')


## Method Resolution Order (MRO):
"""
It's the order in which method should be inherited in the presence of multiple inheritance. 
You can view the MRO by using __mro__ attribute. Here is how MRO is calculated in Python:
A method in the derived calls is always called before the method of the base class.
In our example, Dog class is called before NonMarineMammal or NoneWingedMammal. These two
classes are called before Mammal which is called before Animal, and Animal class is called 
before object. If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal), 
method of NonMarineMammal is invoked first because it appears first.
"""
print(Cat.__mro__)
