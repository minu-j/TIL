# 소인수분해
def soinsu(n):
    for i in range(2, n + 1):
        if n % i == 0:
            nums.append(i)
            n = n // i
            soinsu(n)
            break
    return


for tc in range(int(input())):
    N = int(input())
    ans = 0

    nums = []
    soinsu(N)

    count = [0] * (max(nums) + 1)

    for j in nums:
        count[j] += 1
    for idx, k in enumerate(count):
        if k and k % 3 != 0:
            ans = -1
            break
        elif k and k % 3 == 0:
            count[idx] = k // 3
            ans += idx * count[idx]

    print(f'#{tc + 1} {ans}')
    
