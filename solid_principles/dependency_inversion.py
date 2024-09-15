"""
Dependency Inversion Principle: 
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.
"""

# Violation of the Dependency Inversion Principle
class EmailSender:
    def send_email(self, message: str):
        print(f"Sending email: {message}")

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()

    # Violation of the Dependency Inversion Principle - NotificationService depends on the concrete class EmailSender.
    def send_notification(self, message: str):
        self.email_sender.send_email(message)

# Adhering to the Dependency Inversion Principle
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailSender(NotificationSender):
    def send(self, message: str):
        print(f"Sending email: {message}")

class SMSSender(NotificationSender):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, notification_sender: NotificationSender):
        self.notification_sender = notification_sender

    def send_notification(self, message: str):
        self.notification_sender.send(message)

if __name__ == "__main__":
    email_sender = EmailSender()
    notification_service = NotificationService(email_sender)
    notification_service.send_notification("Hello, World!")

    sms_sender = SMSSender()
    notification_service = NotificationService(sms_sender)
    notification_service.send_notification
