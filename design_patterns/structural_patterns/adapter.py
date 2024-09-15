"""
Adapter Pattern allows objects with incompatible interfaces to collaborate.
It acts as a bridge between two incompatible interfaces.
There is a client that expects a target interface.
There is an adaptee that has an incompatible interface.

Example:
Payment Gateway A has a method process_payment() that accepts a payment amount.
Payment Gateway B has a method send_payment() that accepts a payment amount.
"""

from abc import ABC, abstractmethod

# Target Interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

# Concrete Target - Payment Gateway A (Existing System)
class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} using Stripe")

# Adaptee - Payment Gateway B (New System)
class PayPalPaymentGateway:
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def send_payment(self, amount: float):
        print(f"Sending payment of ${amount} using PayPal")

# Adapter
class PayPalPaymentAdapter(PaymentProcessor):
    def __init__(self, paypal_payment_gateway: PayPalPaymentGateway):
        self.paypal_payment_gateway = paypal_payment_gateway
    
    def process_payment(self, amount: float):
        self.paypal_payment_gateway.send_payment(amount)

# Client Code
def process_payment(payment_processor: PaymentProcessor, amount: float):
    payment_processor.process_payment(amount)

# Usage
if __name__ == "__main__":
    stripe_payment_processor = StripePaymentProcessor()
    process_payment(stripe_payment_processor, 100.0)

    paypal_payment_gateway = PayPalPaymentGateway("api_key")
    paypal_payment_adapter = PayPalPaymentAdapter(paypal_payment_gateway)
    process_payment(paypal_payment_adapter, 200.0)