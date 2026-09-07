# Instance Method
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):       # Instance method
        print("Name:", self.name)
        print("Salary:", self.salary)
e1 = Employee("Pavithra", 30000)
e2 = Employee("Rahul", 40000)
e1.display()
e2.display()

#2.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
e1 = Employee("Rahul", 30000)
e1.display()

#class method
class Employee:
    company = "ABC Technologies"
    @classmethod
    def display_company(cls):
        print("Company:", cls.company)
Employee.display_company()

#2.
class Student:
    college = "ABC College"
    @classmethod
    def display_college(cls):
        print("College:", cls.college)
Student.display_college()

#static method
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
print(Calculator.add(10, 20))

# static method
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
print(Calculator.add(10, 20))

#2.
class Number:
    @staticmethod
    def is_even(n):
        if n % 2 == 0:
            return True
        else:
            return False
print(Number.is_even(10))
