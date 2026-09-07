# 1. Find Factors
num = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# 2. Reverse a Number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse =", reverse)

# 3. Check Prime Number
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")


# 4. Count Even Digits

num = int(input("Enter a number: "))
count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num = num // 10

print("Count of even digits =", count)


# 5. Factorial

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)


# 6. Sum of All Digits

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits =", sum)
