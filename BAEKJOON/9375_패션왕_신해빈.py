for tc in range(int(input())):
    n = int(input())
    clothes = {}
    for _ in range(n):
        i, j = input().split()
        if j in clothes:
            clothes[j] += 1
        else:
            clothes[j] = 2
    ans = 1
    for _ in clothes.values():
        ans *= _
    print(ans - 1)
