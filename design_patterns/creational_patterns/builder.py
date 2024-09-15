"""
Builder Pattern is used when the construction of an object is complex and involves multiple steps.
Builder Pattern separates the construction of a complex object from its representation.
Builder Pattern allows the same construction process to create different representations.

Example:
There is a Pizza class that has multiple attributes such as name, sauce, dough, and toppings.
There are different types of pizza that can be made with different attributes.
"""

from abc import ABC, abstractmethod

# Product
class Pizza:
    def __init__(self):
        self.sauce = ""
        self.dough = ""
        self.toppings = []
    
    def __str__(self):
        return f"{self.name} Pizza with {self.sauce} sauce, {self.dough} dough, and toppings: {', '.join(self.toppings)}"

# Abstract Builder
class PizzaBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_toppings(self):
        pass

    @abstractmethod
    def get_pizza(self) -> Pizza:
        pass

# Concrete Builder
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self._pizza = Pizza()

    def reset(self):
        self._pizza = Pizza()
    
    def build_sauce(self):
        self._pizza.sauce = "Tomato"
    
    def build_dough(self):
        self._pizza.dough = "Regular"
    
    def build_toppings(self):
        self._pizza.toppings = ["Ham", "Pineapple"]
    
    def get_pizza(self) -> Pizza:
        return self._pizza

# Concrete Builder
class SpicyPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self._pizza = Pizza()

    def reset(self):
        self._pizza = Pizza()
    
    def build_sauce(self):
        self._pizza.sauce = "Tomato"
    
    def build_dough(self):
        self._pizza.dough = "Thin"
    
    def build_toppings(self):
        self._pizza.toppings = ["Pepperoni", "Jalapeno"]
    
    def get_pizza(self) -> Pizza:
        return

# Director
class Waiter:
    def __init__(self):
        self._builder = None
    
    def set_builder(self, builder: PizzaBuilder):
        self._builder = builder
    
    def construct_pizza(self):
        self._builder.reset()
        self._builder.build_sauce()
        self._builder.build_dough()
        self._builder.build_toppings()
    
    def get_pizza(self) -> Pizza:
        return self._builder.get_pizza()
    

# Client Code
if __name__ == "__main__":
    waiter = Waiter()

    hawaiin_pizza_builder = HawaiianPizzaBuilder()
    spicy_pizza_builder = SpicyPizzaBuilder()

    waiter.set_builder(hawaiin_pizza_builder)
    waiter.construct_pizza()
    pizza = waiter.get_pizza()
    print(pizza)

    waiter.set_builder(spicy_pizza_builder)
    waiter.construct_pizza()
    pizza = waiter.get_pizza()
    print(pizza)