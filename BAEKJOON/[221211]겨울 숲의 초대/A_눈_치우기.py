N = int(input())
town = sorted(list(map(int, input().split())))

ans = 0
for m in range(1440):
    town.sort()
    ans += 1

    A = town.pop()
    A -= 1

    if len(town) > 0:
        B = town.pop()
        B -= 1
        if B > 0:
            town.append(B)

    if A > 0:
        town.append(A)

    if len(town) == 0:
        break


if len(town) > 0:
    print(-1)
else:
    print(ans)