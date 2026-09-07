
# 
print("Hello World")

#2.
name = input("Enter your name: ")
print("Hello", name)

#3.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))

#4.
class Student:
    def display(self):
        print("Student Name: Pavithra")
        print("Course: Python Full Stack")

student = Student()
student.display()