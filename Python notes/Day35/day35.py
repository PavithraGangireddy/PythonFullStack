# 1. SHALLOW COPY
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0][0] = 10
print("Shallow Copy")
print("a =", a)
print("b =", b)

# 2. DEEP COPY
a = [[5, 6], [7, 8]]
b = copy.deepcopy(a)
b[0][0] = 50
print("\nDeep Copy")
print("a =", a)
print("b =", b)

# 3. ZIP()
a = [1, 2, 3]
b = [4, 5, 6]
print("\nZip Example")
for x, y in zip(a, b):
    print(x, y)

# 4. ZIP() WITH DIFFERENT VALUES
a = [10, 20, 30]
b = [100, 200, 300]
c = list(zip(a, b))
print("\nZip List")
print(c)

# 5. LIST INPUT
a = list(map(int, input("\nEnter numbers: ").split()))
print("List =", a)

# 6. DICTIONARY INPUT
a = input("Enter key: ")
b = input("Enter value: ")
c = {a: b}
print("Dictionary =", c)

