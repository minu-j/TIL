N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def start(now=0, t=0, depth=1):
    global ans
    if depth == N and matrix[now][0]:
        ans = min(ans, t + matrix[now][0])
    for destination in range(N):
        if destination not in visited and matrix[now][destination]:
            visited.add(destination)
            start(destination, t + matrix[now][destination], depth + 1)
            visited.remove(destination)
    return

visited, ans = {0}, 9999999999999
start()

print(ans)