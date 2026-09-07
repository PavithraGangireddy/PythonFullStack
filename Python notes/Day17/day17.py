# Recursion

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

n = int(input())
print(sum_n(n))

#2. 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))


#3. 
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

x = int(input())
n = int(input())

print(power(x, n))


#4
def count_chars(s):
    if s == "":
        return 0
    return 1 + count_chars(s[1:])

s = input()
print(count_chars(s))


#5
def print_pattern(s, n=1):
    if n > len(s):
        return
    print(s[:n])
    print_pattern(s, n + 1)

s = input()
print_pattern(s)


#6.
def reverse_pattern(s):
    if s == "":
        return
    print(s)
    reverse_pattern(s[:-1])

s = input()
reverse_pattern(s)

#7.
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input())

if n == 0:
    print(0)
else:
    print(decimal_to_binary(n))