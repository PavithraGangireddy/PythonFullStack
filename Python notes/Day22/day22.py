#Instance variable
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("Ram", 22)
s2 = Student("Anjali", 21)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)

#2. 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
e1 = Employee("Pavithra", 60000)
e2 = Employee("Rahul", 40000)
print(e1.name)
print(e1.salary)
print(e2.name)
print(e2.salary)

#class variable
class Student:
    college = "ABC College"
    def __init__(self, name):
        self.name = name
s1 = Student("ramya")
s2 = Student("Anjali")
print(s1.name)
print(s1.college)
print(s2.name)
print(s2.college)

#2.
class Employee:
    company = "TCS"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
e1 = Employee("sai", 50000)
e2 = Employee("Rahul", 40000)
print(e1.name, e1.company)
print(e2.name, e2.company)

#Local variable
class Student:
    def __init__(self):
        self.name = "Pavithra"
        def display(self):
            print("Name:", self.name)
s1 = Student()
s1.display()

#2.
class Employee:
    def __init__(self):
        self.name = "Karthik"
        def display(self):
            print("Name:", self.name)
e1 = Employee()
e1.display()