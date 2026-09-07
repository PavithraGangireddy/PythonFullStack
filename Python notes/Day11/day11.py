# elif problems
#1.Input three numbers and print the greatest among them.
a = int(input("enter a number"))
b = int(input("enter b number"))
c = int(input("enter c number"))

if a>b and a>c:
    print(f"{a} is a biggest number")
elif b>a and b>c:
    print(f"{b} is a biggest number")
else:
    print(f"{c} is a biggest number")

 #2.Take an input number and check whether it is a three-digit number.(if-else)

num = int(input(" enter a number"))

if 100 <= abs(num) <= 999:
    print("Its three digit number")
else:
    print("Not a three digit number")

#3.Check if a number is positive, negative, or zero.
num = int(input("enter a number"))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero") 


# Nested if-else statement
#1. Write a Python program to check whether a given number is a multiple of 5.
 #If the number is a multiple of 5, then check whether it is also even or odd and print the appropriate message using nested if.
num= int(input("enter a number"))
if num % 5 == 0:
    if num % 2 == 0:
        print(num, "is a multiple of 5 and it is even")
    else:
        print(num, "is a multiple of 5 and it is odd")
else:
    print(num, "is not a multiple of 5")

 #if statement priblems
# 1.Determine if a number is positive, negative, or zero using only if statements.
num = int(input("enter a number"))

if num > 0:
    print_num = int(input("enter a number"))

if num > 0:
    print("Positive")

if num < 0:
    print("Negative")

if num == 0:
    print("Zero")


#2.Determine if a number is a perfect cube.

n = int(input("enter a number"))

cube_root = round(n ** (1/3))

if cube_root ** 3 == n:
    print("Perfect Cube")
else:
    print("Not a Perfect Cube")


#for loops problems
#1.Calculate the factorial of a number using a for loop?
n = int(input("enter a number"))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)

#2.Count the number of words in a sentence using a for loop ?
sentence = input("enter a number")

count = 0

for word in sentence.split():
    count += 1

print(count)