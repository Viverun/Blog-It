# Learning about abstract classes
from abc import ABC, abstractmethod
class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def go(self, name):
        self.name = name
        print(f"{self.name} can go")
    
    def stop(self, name):
        self.name = name
        print(f"{self.name} can stop now")
    pass
    
car = Car()
car.go("Corvette")
car.stop("Bugatti")