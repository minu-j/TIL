def calc_score(a, b, c):
    return abs(max(a, b, c) - min(a, b, c))


def find_nearest_num(n, nums):
    l, r = 0, len(nums) - 1
    min_dist = 9999999999
    nearest_num = 0

    while l <= r:
        m = (l + r) // 2

        dist = abs(n - nums[m])
        if dist < min_dist:
            min_dist = dist
            nearest_num = nums[m]

        if n < nums[m]:
            r = m - 1
        elif nums[m] < n:
            l = m + 1
        else:
            break

    return nearest_num


A, B, C = map(int, input().split())
a_nums = sorted(map(int, input().split()))
b_nums = sorted(map(int, input().split()))
c_nums = sorted(map(int, input().split()))
ans = 9999999999

for a in a_nums:
    for b in b_nums:
        c_from_a = find_nearest_num(a, c_nums)
        c_from_b = find_nearest_num(b, c_nums)
        dist = min(calc_score(a, b, c_from_a), calc_score(a, b, c_from_b))

        if not dist:
            print(dist)
            exit(0)

        if dist < ans:
            ans = dist

print(ans)
