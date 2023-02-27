N, M = map(int, input().split())
name = set()
ans = []
for i in range(N):
    name.add(input())
for j in range(M):
    m = input()
    if m in name:
        ans.append(m)
print(len(ans))
for k in sorted(ans):
    print(k)