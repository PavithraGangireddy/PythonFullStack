#method overridding
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
c = Calculator()
print(c.add(10))
print(c.add(10, 20))
print(c.add(10, 20, 30))


#operator overloading
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)

#method overloading
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
d = Dog()
c = Cat()
d.sound()
c.sound()
