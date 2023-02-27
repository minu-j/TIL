def sum_nums(nums):
    ans = 0
    for num in nums:
        ans += int(num)
    return ans


n = int(input())
print(sum_nums(input()))
