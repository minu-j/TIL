from collections import deque

pc = [[] for _ in range(int(input()) + 1)]
L = int(input())
infect = {1}
for i in range(L):
    a, b = map(int, input().split())
    pc[a].append(b)
    pc[b].append(a)

virus = deque([1])
while virus:
    now = virus.popleft()
    for net in pc[now]:
        if net not in infect:
            infect.add(net)
            virus.append(net)

print(len(infect) - 1)