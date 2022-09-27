for tc in range(int(input())):
    N, K = map(int, input().split())
    nums = list(input())

    passwords = set()

    for i in range(N // 4):
        for j in range(4):
            passwords.add(int('0x' + ''.join(nums[N // 4 * j:N // 4 * (j + 1)]), 16))
        nums.insert(0, nums.pop())

    print(f'#{tc + 1} {sorted(list(passwords), reverse=True)[K - 1]}')
