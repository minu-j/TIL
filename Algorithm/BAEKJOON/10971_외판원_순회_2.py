N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def start(now=0, t=0, depth=1):
    global ans, mask

    if depth == N and matrix[now][0]:
        ans = min(ans, t + matrix[now][0])
        return

    for destination in range(N):
        if not mask & (1 << destination) and matrix[now][destination] and t + matrix[now][destination] < ans:
            mask |= (1 << destination)
            start(destination, t + matrix[now][destination], depth + 1)
            mask ^= (1 << destination)
    return

mask, ans = 1, 9999999999999
start()

print(ans)
