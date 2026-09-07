#Continuous Number Pattern
num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num = num + 1
    print()

#2.
for i in range(1, i+1):
    for k in range(i-i):
        print("*",end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()

#3.
for i in range(1,i+1):
    for j in range(0):
        print("c", end=" ")
        count = count +1
print()


# Reverse number or stars pattern
#1.
for i in range(i,0-1):
    for i in range(i-i):
        print("*", end = " ")
    for j in range(i):
        print("*", end =" ")
print()

# hollow square pattern
n = 5

for i in range(n):
    for j in range(n):

        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

#number triangle pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#same number pattern
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

#Alphabet pattern
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# Diamond pattern
n = 4

# Upper half
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Lower half
for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# outer loop and inner loop
for i in range(1, 4):
    for j in range(1, 4):
        print("*")

        n = int(input("Enter n: "))
num = 1

#Floyd's Triangle
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()