# using standard queue implementation library

from collections import deque
print("DEQUE standard library, can append and pop left methods")
myQ = deque()
myQ.append("blue")
myQ.append("red")
myQ.append("black")
myQ.append("green")
print(f"MyQueue: {myQ}")

el = myQ.pop()
print(f"POP method: {el}")
print(f"MyQueue: {myQ}")

print("append left`green`")
myQ.appendleft("green")
print(f"MyQueue: {myQ}")

el = myQ.popleft()
print(f"POPLEFT method: {el}")
print(f"MyQueue: {myQ}")