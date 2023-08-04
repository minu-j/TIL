import sys

from collections import deque

H, K, R = map(int, input().split())
tree = [[]] + [[deque(), deque()] for _ in range(2 ** H - 1)]
for h in range(2 ** H):
    tree.append(deque(list(map(int, input().split()))))

for day in range(1, R + 1):
    for n in range(1, 2 ** (H + 1)):
        odd_day = (day + 1) % 2 # 홀수날 0 짝수날 1
        seat = n % 2 # 왼쪽사람 0 오른쪽사람 1
        if n == 1:
            # 부서장
            if tree[n][odd_day]:
                tree[0].append(tree[n][odd_day].popleft())
        elif n < 2 ** H:
            # 직원
            if tree[n][odd_day]:
                tree[(n - seat) // 2][seat].append(tree[n][odd_day].popleft())
        else:
            # 말단직원
            if tree[n]:
                tree[(n - seat) // 2][seat].append(tree[n].popleft())
print(sum(tree[0]))
