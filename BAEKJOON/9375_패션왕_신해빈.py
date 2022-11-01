for tc in range(int(input())):
    n = int(input())
    clothes = {}
    for _ in range(n):
        i, j = input().split()
        if j in clothes:
            clothes[j] += 1
        else:
            clothes[j] = 1
    for l in range(1, len(clothes) + 1):
        for c in range(l):
