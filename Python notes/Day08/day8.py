# 1. upper() and lower()
text = "codegnan"
print(text.upper())
print(text.lower())

# 2. strip()
text = "  Python  "
print(text.strip())

# 3. replace()
text = "I like Java"
print(text.replace("Java", "Python"))

# 4. split()
text = "Python Full Stack"
print(text.split())

# 5. find() and count()
text = "banana"
print(text.find("a"))
print(text.count("a"))

# 6. startswith() and endswith()
text = "Python"
print(text.startswith("Py"))
print(text.endswith("on"))

# 7. Create and access
numbers = [10, 20, 30, 40]
print(numbers)
print(numbers[0])
print(numbers[-1])

# 8. Add elements
numbers.append(50)
numbers.insert(1, 15)
print(numbers)

# 9. Remove elements
numbers.remove(20)
numbers.pop()
print(numbers)

# 10. Update and sort
numbers[0] = 5
numbers.sort()
print(numbers)

# 11. Slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# 12. Loop through list
for number in numbers:
    print(number)