N, M = map(int, input().split())
list_1, list_2 = list(map(int, input().split())), list(
    map(int, input().split()))

p1 = 0
p2 = 0
ans = []

while p1 < N or p2 < M:
    if p1 == N:
        ans.append(list_2[p2])
        p2 += 1

    elif p2 == M:
        ans.append(list_1[p1])
        p1 += 1

    elif list_1[p1] < list_2[p2]:
        ans.append(list_1[p1])
        p1 += 1

    elif list_1[p1] > list_2[p2]:
        ans.append(list_2[p2])
        p2 += 1
    else:
        ans.append(list_1[p1])
        ans.append(list_2[p2])
        p1 += 1
        p2 += 1

print(' '.join(map(str, ans)))
