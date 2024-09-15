"""
Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses.

Example:
There are different types of pizza. Each type of pizza is made in a different way.
"""
from abc import ABC, abstractmethod

# Product
class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.sauce = ""
        self.dough = ""
        self.toppings = []

    def prepare(self):
        print("Preparing Pizza")
        print(f"Adding {self.sauce} sauce")
        print(f"Adding {self.dough} dough")
        print("Adding toppings:")
        for topping in self.toppings:
            print(topping)

    def bake(self):
        print("Baking Pizza")

    def cut(self):
        print("Cutting Pizza into diagonal slices")

    def box(self):
        print("Putting Pizza in a box")

# Concrete Products
class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.sauce = "Tomato"
        self.dough = "Regular"
        self.toppings = ["Mozzarella", "Parmesan"]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.sauce = "Tomato"
        self.dough = "Regular"
        self.toppings = ["Cheeze", "Mozzarella", "Parmesan"]

    def cut(self):
        print("Cutting Pizza into square slices")   

# Creator
class PizzaStore(ABC):
    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        pass

# Concrete Creators
class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        match pizza_type:
            case "Cheese":
                return NYStyleCheesePizza()
            case _:
                raise ValueError(f"Unknown Pizza Type: {pizza_type}")
            

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        match pizza_type:
            case "Cheese":
                return ChicagoStyleCheesePizza()
            case _:
                raise ValueError(f"Unknown Pizza Type: {pizza_type}")
            

# Usage
if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("Cheese")
    print(f"Ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("Cheese")
    print(f"Ordered a {pizza.name}\n")


