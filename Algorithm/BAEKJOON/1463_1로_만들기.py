from collections import deque

q = deque([int(input())])
visited = set()
ans = 0

while q:
    for _ in range(len(q)):
        now = q.popleft()
        if now == 1:
            print(ans)
            exit(0)
        calc_3 = now // 3
        calc_2 = now // 2
        calc_1 = now - 1
        if now % 3 == 0 and calc_3 not in visited:
            visited.add(calc_3)
            q.append(calc_3)
        if now % 2 == 0 and calc_2 not in visited:
            visited.add(calc_2)
            q.append(calc_2)
        q.append(calc_1)
    ans += 1