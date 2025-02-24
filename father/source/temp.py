from collections import deque

data = [1, 2, 3]

queue0 = ["1111", "3333", "5555"]
queue = deque(["1111", "3333", "5555"])

print(data)
print(queue)

queue.append('7777')
print(queue)


print(queue0)
print(queue)