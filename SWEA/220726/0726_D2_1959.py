case = int(input())

n = []
m = []
ai = []
bj = []

for x in range(case):
    nm = list(input().split())
    n.append(int(nm[0]))
    m.append(int(nm[1]))

    if n >= m:
        ai.append(list(map(int, input().split())))
        bj.append(list(map(int, input().split())))
    elif m > n:
        n, m = m, n
        bj.append(list(map(int, input().split())))
        ai.append(list(map(int, input().split())))


print(n, m, ai, bj)

for x in range(case):
    max = 0
    if n[x] == m[x]:
        for y in range(n[x]):
            print(ai[x][y] * bj[x][y])
            if max < ai[x][y] * bj[x][y]:
                max = ai[x][y] * bj[x][y]

    else:
        i = 0
        for y in range(m[x]):
            for z in range(n[x] - m[x] + 1):
                print(ai[x][z], bj[x][y])
                if max < ai[x][z + i] * bj[x][y]:
                    max = ai[x][z + i] * bj[x][y]
            i += 1

    print(f'#{x + 1} {max}')        
