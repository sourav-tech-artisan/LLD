from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"
    
class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"
    
class AnimalFactory:
    def create_animals(self, animal_type: str) -> Animal:
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            return ValueError(f"Unknown Animal Found! {animal_type}")
        

# Usage
factory = AnimalFactory()
dog = factory.create_animals("Dog")
cat = factory.create_animals("Cat")
print(dog.speak())
print(cat.speak())