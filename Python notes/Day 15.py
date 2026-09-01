 #functions
def Add(a, b):
    print(a + b)

Add(10, 20)
Add(100, 200)
Add(50, 30)

#2. real time example of function
def login():
    pass

def calculate_cart_total():
    pass

def apply_discount():
    pass

def place_order():
    pass

#3.function execution flow
print("Start")

def Greet():
    print("Welcome")

print("Before calling")

Greet()

print("End")

# positional arguments
def Greet(name, age):
    print(f"My name is {name} and age is {age}")
Greet("Raju", 23)

# function arguments without return value
def Add(a, b):
    c = a + b
    print("Addition:", c)
Add(10, 20)

# default parameter
def CountryDetails(country="India"):
    print("My country is:", country)
    CountryDetails("USA")
CountryDetails()