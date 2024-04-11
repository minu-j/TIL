for tc in range(int(input())):
    N, nums = int(input()), sorted(list(map(int, input().split())))
    double_num_set = set(map(lambda x: x * 2, nums))
    ans = 0
    for l in range(N - 1):
        for r in range(l + 1, N):
            if nums[l] + nums[r] in double_num_set:
                ans += 1
    print(ans)
