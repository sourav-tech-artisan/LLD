"""
Interface Segregation Principle (ISP) states that a client should not be forced to implement an interface
that it does not use.
"""

from abc import ABC, abstractmethod
# Violation of the Interface Segregation Principle
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def set_temperature(self):
        pass

    def set_volume(self):
        pass

class SmartThermoStat(SmartDevice):
    def turn_on(self):
        print("Turning on the thermostat")

    def turn_off(self):
        print("Turning off the thermostat")

    def set_temperature(self):
        print("Setting the temperature")

    # Violation of the Interface Segregation Principle - The SmartThermoStat class is forced to implement the set_volume() method
    def set_volume(self):
        raise NotImplementedError("Thermostat does not have volume controls")

class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Turning on the speaker")

    def turn_off(self):
        print("Turning off the speaker")

    # Violation of the Interface Segregation Principle - The SmartSpeaker class is forced to implement the set_temperature() method
    def set_temperature(self):
        raise NotImplementedError("Speaker does not have temperature controls")

    def set_volume(self):
        print("Setting the volume")

### Adhering to the Interface Segregation Principle
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class TemperatureContrallable(ABC):
    @abstractmethod
    def set_temperature(self):
        pass

class VolumeControllable(ABC):
    @abstractmethod
    def set_volume(self):
        pass

class SmartThermoStat(Switchable, TemperatureContrallable):
    def turn_on(self):
        print("Turning on the thermostat")

    def turn_off(self):
        print("Turning off the thermostat")

    def set_temperature(self):
        print("Setting the temperature")

class SmartSpeaker(Switchable, VolumeControllable):
    def turn_on(self):
        print("Turning on the speaker")

    def turn_off(self):
        print("Turning off the speaker")

    def set_volume(self):
        print("Setting the volume")

# Usage
if __name__ == "__main__":
    smart_thermostat = SmartThermoStat()
    smart_thermostat.turn_on()
    smart_thermostat.set_temperature()

    smart_speaker = SmartSpeaker()
    smart_speaker.turn_on()
    smart_speaker.set_volume()