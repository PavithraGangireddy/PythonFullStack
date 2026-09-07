
# 1. Simple if
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")

# 2. if-else – Even or Odd
number = int(input("Enter number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Positive or Negative
number = int(input("Enter number: "))
if number >= 0:
    print("Positive")
else:
    print("Negative")

# 4. Pass or Fail
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 5. Greater Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
else:
    print("Second number is greater")

# 6. Check Dictionary Value
student = {"name": "kavya", "marks": 75}

if student["marks"] >= 40:
    print("Student Passed")
else:
    print("Student Failed")