def get_max_benefit(depth=0, benefit=0, left=0):
    global ans
    if depth == N:
        if ans < benefit:
            ans = benefit
        return
    if left:
        get_max_benefit(depth + 1, benefit, left - 1)
    else:
        if N - depth > days[depth][0] - 1:
            get_max_benefit(depth + 1, benefit + days[depth][1], days[depth][0] - 1)
        get_max_benefit(depth + 1, benefit, left)


N = int(input())
days = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
get_max_benefit()
print(ans)