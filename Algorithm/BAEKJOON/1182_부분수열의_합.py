def get_subsequence(depth=0, subsequence=[]):
    global ans
    if depth == N:
        if subsequence and sum(subsequence) == S:
            ans += 1
        return
    
    subsequence.append(nums[depth])
    get_subsequence(depth + 1, subsequence)
    subsequence.pop()
    get_subsequence(depth + 1, subsequence)
    

N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
get_subsequence()
print(ans)