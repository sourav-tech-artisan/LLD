"""
Composition is a "has a" relationship. It is a more restrictive form of aggregation.
"""

class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped" 
    
class Car:
    def __init__(self):
        self.engine = Engine("2.0L")

    def start(self):
        return f"Car with engine {self.engine.capacity} {self.engine.start()}"
    
    def stop(self):
        return f"Car with engine {self.engine.capacity} {self.engine.stop()}"