# Generators

def square(l):
    k = []
    for i in l:
        k.append(i*i)
        return k
    n = input()
l = [1,2,3,4,5]
r = square(l)
print(l)

#2.
def my_gen():
    yield "frist"
    yield "second"
m = my_gen()
print(m)
print(next(m))
print(next(m))

#3.
def numbers():
    for i in range(1,6):
        yield i
        n = numbers()
        for val in range(1,6):
            print(val)
#4
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
print(next(counter))
print(next(counter))

#5.
def fetch_posts():
    post_id = 1
    while True:
        yield f"Post {post_id}"
        post_id += 1
news_feed = fetch_posts()
print(next(news_feed)) 
print(next(news_feed)) 

#6. list comphrensions

result = [x**2 for x in range(1, 11)]
print(result)

#2.
result = [x for x in range(1, 21) if x % 2 == 0]
print(result)

#3.

result = [(letter, number) for letter in 'ABC' for number in range(1, 4)]
print(result)

#4.
data = [1, None, 2, None, 3]

result = [x for x in data if x is not None]
print(result)

#5.
words = ['cat', 'dog', 'apple']

result = [word[::-1] for word in words]
print(result)