"""
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.
Strategy Pattern favors composition over inheritance.

Example:
There are ducks that can fly and quack. But there are different types of ducks that can fly and quack in different ways.
"""

from abc import ABC, abstractmethod

# Strategy Interface for flying
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

# Concrete Strategies for flying
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying with wings")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Can't fly")

# Strategy Interface for quacking
class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

# Concrete Strategies for quacking
class Quack(QuackBehavior):
    def quack(self):
        print("Quack!")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak!")


# Context class
class Duck:
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        # Composition
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior
    
    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()
    
    # Setter method for fly behavior - to change behavior at runtime
    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior


# Subclasses of Duck

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())


# Usage
if __name__ == "__main__":
    mallard_duck = MallardDuck()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()    

    rubber_duck = RubberDuck()
    rubber_duck.perform_fly()
    rubber_duck.perform_quack()