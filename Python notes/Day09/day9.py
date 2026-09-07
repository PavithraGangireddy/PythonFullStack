# 1. Create and access Tuple
t = (10, 20, 30, 40)
print(t)
print(t[0])
print(t[-1])

# 2. Tuple slicing
print(t[1:3])

# 3. Tuple length
print(len(t))

# 4. Tuple count and index
t = (10, 20, 20, 30)
print(t.count(20))
print(t.index(30))

# 5. Tuple loop
for x in t:
    print(x)

# 6. Tuple unpacking
student = ("Akash", 22, 85)
name, age, marks = student
print(name)
print(age)
print(marks)

# 7. Create Set
s = {10, 20, 30, 20}
print(s)

# 8. Add elements
s.add(40)
print(s)

# 9. Update Set
s.update([50, 60])
print(s)

# 10. Remove elements
s.remove(20)
print(s)

# 11. Discard element
s.discard(100)
print(s)

# 12. Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

# 13. Intersection
print(a.intersection(b))

# 14. Difference
print(a.difference(b))

# 15. Set membership
print(2 in a)
print(10 not in a)

# 16. Set loop
for x in a:
    print(x)