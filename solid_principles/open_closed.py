"""
Open Closed Principle: Software entities should be open for extension but closed for modification.
"""

# Violation of the Open Closed Principle
class ShippingCostCalculator:
    """This class violates the Open Closed Principle because it is not open for extension.
    If we want to add a new shipping method, we would need to modify the class.
    """
    def calculate(self, order):
        if order.shipping_method == "ground":
            return self.calculate_ground_shipping(order)
        elif order.shipping_method == "air":
            return self.calculate_air_shipping(order)
        elif order.shipping_method == "ship":
            return self.calculate_ship_shipping(order)
    
    def calculate_ground_shipping(self, order):
        return 5 + (0.1 * order.total)
    
    def calculate_air_shipping(self, order):
        return 10 + (0.2 * order.total)
    
    def calculate_ship_shipping(self, order):
        return 20 + (0.4 * order.total)
    

# Adhering to the Open Closed Principle
from abc import ABC, abstractmethod

class ShippingCostCalculator(ABC):
    """This class adheres to the Open Closed Principle by being open for extension but closed for modification.
    If we want to add a new shipping method, we can create a new subclass without modifying the existing class.
    """
    @abstractmethod
    def calculate_cost(self, order):
        pass

class GroundShippingCostCalculator(ShippingCostCalculator):
    def calculate_cost(self, order):
        return 5 + (0.1 * order.total)

class AirShippingCostCalculator(ShippingCostCalculator):
    def calculate_cost(self, order):
        return 10 + (0.2 * order.total)
    
class ShipShippingCostCalculator(ShippingCostCalculator):
    def calculate_cost(self, order):
        return 20 + (0.4 * order.total)

# Adding a new shipping method without modifying the existing class
class DroneShippingCostCalculator(ShippingCostCalculator):
    def calculate_cost(self, order):
        return 15 + (0.3 * order.total)
    
class Order:
    def __init__(self, total, shipping_method):
        self.total = total
        self.shipping_method = shipping_method

    def calculate_shipping_cost(self):
        return self.shipping_method.calculate_cost(self)
    
# Usage
if __name__ == "__main__":
    order = Order(total=100, shipping_method=GroundShippingCostCalculator())
    print(order.calculate_shipping_cost())
    
    order = Order(total=100, shipping_method=AirShippingCostCalculator())
    print(order.calculate_shipping_cost())
    
    order = Order(total=100, shipping_method=ShipShippingCostCalculator())
    print(order.calculate_shipping_cost())
    
    order = Order(total=100, shipping_method=DroneShippingCostCalculator())
    print(order.calculate_shipping_cost())