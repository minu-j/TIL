N, K = map(int, input().split())
temps = [0] + list(map(int, input().split()))
ans = -99999999999

for i in range(1, N + 1):
    temps[i] = temps[i - 1] + temps[i]

for idx in range(N - K + 1):
    sum_temps = temps[idx + K] - temps[idx]
    if ans < sum_temps:
        ans = sum_temps

print(ans)
