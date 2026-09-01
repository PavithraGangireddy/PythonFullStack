# Local scope 
def student():
    name= "Rudra"
print(name)
student()

# Global scope
company = "TCS"
def display():
    print("inside the function:" , company)
    print("start-1")
display()
print("outside the function:", company)
print("start-2")

2.
number = 10
def display():
    number = 100
    print(" number inside  function:" , number)
print(" number outside function:", number)


#Non local scope
def outer():
    count = 10
    def inner():
        nonlocal count
        count += 5
        inner()
        print(count)

#2. 
def outer():
    def inner():
        print("inner")
    inner()
    print("outer")
print("start")
outer()
print("end")

# lambda functions
def square(n):
    return n*n
print(square(10))

# addition of two numbers
add = lambda a,b : a+b
print(add(100,200))

#3.
square = lambda x : x*x
print(square(10))