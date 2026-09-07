#swaping variables
a = 10
b = 20
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)

# numeric data type
a = 10
b = 10.5
c = 3 + 4j
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#strings operations
first_name = "Pavithra"
last_name = "Reddy"
full_name = first_name + " " + last_name
print("Full Name:", full_name)
print("Length:", len(full_name))

#Lists
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)
print(type(fruits))

#Tuples
student = ("Pavithra", 22, "Python")
print("Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])

#Range
numbers = range(1, 11)
print(list(numbers))