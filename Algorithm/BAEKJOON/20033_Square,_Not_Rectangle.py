def find_square(h):
    max_len, now_len = 0, 0
    for i in range(N):
        if heights[i] >= h:
            now_len += 1
            if max_len <= now_len:
                max_len = now_len
        else:
            now_len = 0

        if h <= max_len:
            return True
    return False


MAX_HEIGHT = 300000
N = int(input())
heights = list(map(int, input().split()))
l, r = 1, min(MAX_HEIGHT, N)
ans, m = 1, (l + r) // 2

while l <= r:
    if find_square(m):
        if ans < m:
            ans = m
        l = m + 1
    else:
        r = m - 1
    m = (l + r) // 2
print(ans)
