from collections import deque

Q = deque(list(range(1, int(input()) + 1)))

while len(Q) > 1:
    Q.popleft()
    Q.append((Q.popleft()))

print(Q[0])
