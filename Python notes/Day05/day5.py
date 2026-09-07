
#Arithmetic operations
a = 20
b = 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#comparison operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Assignment operators
a = 10
a += 5
print(a)
a -= 2
print(a)
a *= 3
print(a)
a /= 2
print(a)
a //= 2
print(a)
a %= 2
print(a)
a **= 2
print(a)

#logical operators
a = 10
b = 5
print(a > 5 and b < 10)
print(a > 15 or b < 10)
print(not(a > 5))

#membership operators
numbers = [10, 20, 30, 40]
print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)

#identity operators
a = [10, 20]
b = a
c = [10, 20]
print(a is b)
print(a is c)
print(a is not c)

#bitwise operators
a = 10
b = 4
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)