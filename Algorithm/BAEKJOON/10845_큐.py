from collections import deque
import sys

Q = deque([])
for N in range(int(sys.stdin.readline())):
    now = list(sys.stdin.readline().rstrip().split())
    if now[0] == 'push':
        Q.append(now[1])
    if now[0] == 'pop':
        if len(Q) > 0:
            n = Q.popleft()
            print(n)
        else:
            print(-1)
    if now[0] == 'size':
        print(len(Q))
    if now[0] == 'empty':
        if len(Q) > 0:
            print(0)
        else:
            print(1)
    if now[0] == 'front':
        if len(Q) > 0:
            n = Q.popleft()
            print(n)
            Q.appendleft(n)
        else:
            print(-1)
    if now[0] == 'back':
        if len(Q) > 0:
            n = Q.pop()
            print(n)
            Q.append(n)
        else:
            print(-1)
