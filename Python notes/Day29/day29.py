#ZeroDivisionError
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

#2.
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")

#3.try,except,else,finally
try:
    num = int(input())
    print(num * num)
except ValueError:
    print("Invalid input")
else:
    print("Program executed successfully")
finally:
    print("Program completed")

#4.raise
age = int(input())

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Eligible")
except ValueError as e:
    print(e)
