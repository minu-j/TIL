# 22. 11. 3. / 113112KB / 112ms / 134B
N = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += arr[-i + -1] * (i + 1)
print(ans)

# 23. 5. 30. / 118968KB / 128ms / 140B
N, P = int(input()), sorted(map(int, input().split()))
print(sum(list(map(lambda x: sum(x), list(map(lambda x: P[:x], range(N, -1, -1)))))))