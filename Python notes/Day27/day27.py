#abc module
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
d = Dog()
d.sound()

#2.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts")

    def stop(self):
        print("Car stops")
c = Car()
c.start()
c.stop()

#3.
from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass
class SBI(Bank):
    def interest(self):
        print("SBI interest is 7%")
s = SBI()
s.interest()


