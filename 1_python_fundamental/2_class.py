# encapsulation
'''
self.attribute_name to access and manipulate the object's attributes. The self parameter is crucial - it refers to the specific object on which the method is being called.
'''
class BankAccount:
    def __init__(self, balance): # Constructor method
        self._balance = balance  # Private attribute starts with underscore(_)

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
    
# abstraction
from abc import ABC, abstractmethod
'''
Python's abc module (Abstract Base Classes) takes this a step further by enabling you to define abstract base classes. These classes serve as blueprints for other classes, outlining essential methods that concrete subclasses must implement.
'''

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):  # Concrete subclass
    def make_sound(self):
        return "Bark!"
    
# object
# Add your class definition here (steps 1-3)
class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.breed}.")

# Creating the instance of the Dog class (step 4)
my_dog = Dog("Buddy", "Golden Retriever")
# Directing the dog to bark (step 5)
my_dog.bark()

