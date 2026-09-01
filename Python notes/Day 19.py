#modules
def Greet():
    return "Welcome Back!"
print("function call from frist:", Greet())
print("function call from frist:", Greet())

#2.
import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(json_str)
parsed = json.loads(json_str)
print(parsed["name"])

#math modlue

import math
number = 25
result = math.sqrt(number)
print("Square root:", result)




#2.
import math
number = 5
result = math.factorial(number)
print("Factorial:", result)



#Random module
import random
numbers = [10, 20, 30, 40, 50]
print("Random number:", random.randint(1, 100))
print("Random float:", random.random())
print("Random choice:", random.choice(numbers))

random.shuffle(numbers)
print("Shuffled list:", numbers)


#itertools module

import itertools
numbers = [1, 2, 3]
result = itertools.permutations(numbers)
for item in result:
    print(item)

#2.
    import itertools
numbers = [1, 2, 3, 4]
result = itertools.combinations(numbers, 2)
for item in result:
    print(item)