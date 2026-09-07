
# 1. Input
name = input("Enter your name: ")
print("Hello", name)

# 2. Two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

# 3. Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 4. Student Details
name = input("Enter name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
print(f"Name: {name}, Age: {age}, Marks: {marks:.2f}")

# 5. Rectangle Area
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print(f"Area = {length * width:.2f}")

# 6. Bill
item = input("Enter item: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"Item: {item}")
print(f"Total: ₹{total:.2f}")

# 7. sep
print(5, 9, 2026, sep="-")

# 8. end
print("Python", end=" ")
print("Full Stack")