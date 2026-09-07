# 1.Armstrong Numbers Between 1 and 1000
# Write a Python program to print all Armstrong numbers between the range 1 to 1000.

for num in range(1, 1001):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num)



 # 2.Write a Python program to print all palindrome numbers between the range 1 to 100.

for num in range(1, 101):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if original == reverse:
        print(original)

# 3.Fibonacci Numbers Between 10 and 50
# Write a Python program to print all Fibonacci numbers between the range 10 and 50.

a, b = 0, 1
while a < 10:
    a, b = b, a + b
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b

#4. Write a Python program using nested for loops to print * 9 times.
for i in range(3):
    for j in range(3):
        print("*")


#5. A loop inside another loop is called a nested loop.

for i in range(3):
    for j in range(3):
        print("*")


#6. Alphabet Pattern
 # Print:
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

#7. while loop problems
s = 10
e = 1
while s>= e:
    print(s)
    s = s-1


# 8. jumping statement problems
for i in range(1,6):
    if i == 4:
        break
    print(i)


# for-else  problems
#1.
id = [101,102,103,104]
key = 103
for i in range(len(id)):
    if id[i] == key:
        print("key is found")
        break
    else:
        print("key is not found")
        print("end")

# assert keyword problems
age = 10
assert age <= 18, " not eligible for vote due to age" 
print("eligible for vote")


