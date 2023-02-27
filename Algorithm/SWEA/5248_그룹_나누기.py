def find_set(x):
    if team[x] != x:
        team[x] = find_set(team[x])
    return team[x]


for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    wish_team = []
    for i in range(0, M * 2, 2):
        wish_team.append(sorted(arr[i:i + 2]))

    team = list(range(N + 1))

    for j, k in wish_team:
        if find_set(j) != find_set(k):
            team[find_set(k)] = find_set(j)

    for m in range(len(team)):
        find_set(m)

    team.pop(0)

    print(f'#{tc + 1} {len(set(team))}')
