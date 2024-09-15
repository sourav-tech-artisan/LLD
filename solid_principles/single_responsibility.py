"""
Solid Principle 1: Single Responsibility Principle
A class should have only one reason to change, meaning that a class should have only one job or responsibility.
"""
# violating the Single Responsibility Principle
class Order:
    """This class violates the Single Responsibility Principle because it has multiple reasons to change.
    It has the responsibility of managing the order details and processing the payment.
    """
    def __init__(self, customer_id, items) -> None:
        self.customer_id = customer_id
        self.items = items
        self.total = sum(item.price for item in items)

    def add_item(self, item):
        self.items.append(item)
        self.total += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total -= item.price
    
    def process_payment(self, payment_processor):
        payment_processor.process_payment(self.total)

    def generate_invoice(self):
        print("Generating invoice")
        print(f"Customer ID: {self.customer_id}")
        print(f"Total: {self.total}")
    

# adhering to the Single Responsibility Principle
class Order:
    """This class adheres to the Single Responsibility Principle by having only one reason to change.
    It has the responsibility of managing the order details.
    """
    def __init__(self, customer_id, items) -> None:
        self.customer_id = customer_id
        self.items = items
        self.total = sum(item.price for item in items)

    def add_item(self, item):
        self.items.append(item)
        self.total += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total -= item.price

class PaymentProcessor:
    """This class adheres to the Single Responsibility Principle by having only one reason to change.
    It has the responsibility of processing the payment.
    """
    def process_payment(self, order, amount):
        print(f"Processing payment of ${amount} for order with total ${order.total}")

class InvoiceGenerator:
    """This class adheres to the Single Responsibility Principle by having only one reason to change.
    It has the responsibility of generating the invoice.
    """
    def generate_invoice(self, order):
        print("Generating invoice")
        print(f"Customer ID: {order.customer_id}")
        print(f"Total: {order.total}")

# Usage
if __name__ == "__main__":
    order = Order(customer_id=1, items=[{"id": 2, "name": "item1", "price": 50}, {"id": 2, "name": "item2", "price": 100}])
    payment_processor = PaymentProcessor()
    invoice_generator = InvoiceGenerator()

    payment_processor.process_payment(order, order.total)
    invoice_generator.generate_invoice(order)
