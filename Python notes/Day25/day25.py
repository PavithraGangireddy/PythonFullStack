#single inheritance
class Employee:
    def employee_details(self):
        print("Employee Name: Sai")
        print("Employee ID: 101")
class Developer(Employee):
    def developer_details(self):
        print("Role: Python Developer")
        print("Technology: Python")
d = Developer()
d.employee_details()
d.developer_details()

#multiple inheritance
class Account:
    def account_details(self):
        print("Account Number: 456321")
class Customer:
    def customer_details(self):
        print("Customer Name: sai")
class Bank(Account, Customer):
    def bank_details(self):
        print("Bank Name: SBI")
b = Bank()
b.account_details()
b.customer_details()
b.bank_details()

#multi-level inheritance
class Company:
    def company_details(self):
        print("Company: codegnan Technologies")
class Employee(Company):
    def employee_details(self):
        print("Employee ID: 101")
class Developer(Employee):
    def developer_details(self):
        print("Role: Python Developer")
d = Developer()
d.company_details()
d.employee_details()
d.developer_details()

#hierarchical inheritance
class Vehicle:
    def vehicle_details(self):
        print("Vehicle has an engine")
class Car(Vehicle):
    def car_details(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def bike_details(self):
        print("Bike has 2 wheels")
car = Car()
bike = Bike()
car.vehicle_details()
car.car_details()
bike.vehicle_details()
bike.bike_details()

#hybrid inheritance
class Company:
    def company_details(self):
        print("Company: codegnan Technologies")
class Developer(Company):
    def developer_details(self):
        print("Developer: Python Developer")
class Tester(Company):
    def tester_details(self):
        print("Tester: Software Tester")
class Project(Developer, Tester):
    def project_details(self):
        print("Project: Banking Application")
p = Project()
p.company_details()
p.developer_details()
p.tester_details()
p.project_details()