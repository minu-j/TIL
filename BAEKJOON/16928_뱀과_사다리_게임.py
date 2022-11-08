from collections import deque
from pprint import pprint

board = list(range(101))
N, M = map(int, input().split())
for i in range(N + M):
    s, e = map(int, input().split())
    board[s] = e

visited = [0] * 101
q = deque([1])
count = 0
ans = 9999999999

while q:
    count += 1
    for turn in range(len(q)):
        now = q.popleft()
        for dice in range(1, 7):
            if now + dice <= 100:
                post = board[now + dice]
                if not visited[post]:
                    visited[post] = count
                    if post == 100:
                        if ans > count:
                            ans = count
                    else:
                        q.append(post)
print(ans)