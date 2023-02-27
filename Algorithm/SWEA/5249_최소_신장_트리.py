def make_set(x):
    p[x] = x
    return


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(x)] = find_set(y)
    return


for tc in range(int(input())):
    V, E = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(E)]
    matrix.sort(key=lambda x: x[2])
    p = [0] * (V + 1)
    for _ in range(V + 1):
        make_set(_)

    ans = 0
    count = 0

    for x, y, w in matrix:
        if find_set(x) != find_set(y):
            union(x, y)
            ans += w
            count += 1

        if count == V:
            break

    print(f'#{tc + 1} {ans}')
