N = int(input())
nums = [int(input()) for _ in range(N)]
target = nums.pop(0)
ans = 0
nums.sort()

if N == 1:
    print(0)
    exit(0)

while nums[-1] >= target:
    nums[-1] -= 1
    target += 1
    ans += 1
    nums.sort()

print(ans)