"""
Aggregation is type of association where one class is composed of one or more instances of another class.
Unlike composition, the lifecycle of the contained objects is independent of the container object.
Aggregation represents a "has-a" relationship.
"""
class Employee:
    def __init__(self, name: str):
        self.name = name
    
class Department:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee: Employee):
        self.employees.append(employee)