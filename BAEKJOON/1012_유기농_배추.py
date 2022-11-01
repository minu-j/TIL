import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(int(input())):
    M, N, K = map(int, input().split())
    cabbage = set()
    for _ in range(K):
        cabbage.add(tuple(map(int, input().split())))

    ans = 0
    visited = set()

    for p in cabbage:
        if p not in visited:
            q = deque()
            q.append(p)

            while q:
                now = q.popleft()
                # 1. q를 popleft 한 후 visited 체크
                visited.add(now) 

                for d in range(4):
                    np = (di[d] + now[0], dj[d] + now[1])
                    if np in cabbage and np not in visited:
                        # 2. q에 append 하기 전 visited 체크
                        visited.add(np)
                        q.append(np)
            ans += 1

    print(ans)
