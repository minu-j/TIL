from collections import deque

arr = deque(list(input().split('-')))

ans = 0

for i in range(len(arr)):
    now = sum(list(map(int, arr.popleft().split('+'))))
    if i == 0:
        ans = now
    else:
        ans -= now

print(ans)