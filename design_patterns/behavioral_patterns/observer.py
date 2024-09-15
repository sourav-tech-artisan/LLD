"""
Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
Observer Pattern is used when there is a one-to-many relationship between objects such as if one object is modified, its dependent objects are to be notified automatically.

Example:
There is a weather station that measures temperature, humidity, and pressure. There are different displays that show the current weather conditions.
When the weather station updates the weather conditions, all the displays should be updated automatically.
"""

from abc import ABC, abstractmethod

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

# Concrete Subject
class WeatherData(Subject):
    def __init__(self):
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
        self._observers = []
    
    def register_observer(self, observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

# Concrete Observer
class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data: WeatherData):
        self._temperateure  = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
        self._weather_data = weather_data
        self._weather_data.register_observer(self)
    
    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.display()
    
    def display(self):
        print(f"Current Conditions: {self._temperature}F degrees, {self._humidity}% humidity, and {self._pressure} pressure")


# Usage
if __name__ == "__main__":
    weather_data = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)