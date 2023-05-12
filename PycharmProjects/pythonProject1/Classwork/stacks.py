from collections import deque

q1 = deque([])
q1.append(1)
q1.append(2)
q1.append(3)
q1.append(4)
q1.popleft()
print(q1)
print(q1.index(2))

