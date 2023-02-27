N = int(input())

ans = 99999999999

for i in range(5000):
    for j in range(5000):
        if i + j > 5000:
            break
        elif 3 * i + 5 * j == N and i + j < ans:
            ans = i + j
if ans == 99999999999:
    print(-1)
else:
    print(ans)
