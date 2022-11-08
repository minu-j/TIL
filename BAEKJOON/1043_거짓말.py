from collections import deque

N, M = map(int, input().split())
person = [set() for _ in range(N + 1)]
T = list(map(int, input().split()))[1:]
party = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

if not T:
    print(M)
    exit(0)

for i in party:
    q = deque(i)
    for j in range(len(q)):
        now = q.popleft()
        for k in q:
            person[now].add(k)
        q.append(now)

q = deque(T)

while q:
    now = q.popleft()
    for i in person[now]:
        if i not in T:
            T.append(i)
            q.append(i)
T = set(T)

ans = 0

for j in party:
    lie = j.isdisjoint(T)

    if lie:
        ans += 1

print(ans)