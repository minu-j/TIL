case = int(input())

n = []
m = []
ai = []
bj = []

for x in range(case):
    nm = list(input().split())

    if nm[0] >= nm[1]:
        n.append(int(nm[0]))
        m.append(int(nm[1]))    
        ai.append(list(map(int, input().split())))
        bj.append(list(map(int, input().split())))

    elif nm[1] > nm[0]:
        m.append(int(nm[0]))
        n.append(int(nm[1]))    
        bj.append(list(map(int, input().split())))
        ai.append(list(map(int, input().split())))

for x in range(case):
    max = 0
    if n[x] == m[x]:
        for y in range(n[x]):
            if max < ai[x][y] * bj[x][y]:
                max = ai[x][y] * bj[x][y]

    else:
        while len(ai[x]) >= len(bj[x]):
            for y in range(len(bj[x])):
                if max < ai[x][y] * bj[x][y]:
                    max = ai[x][y] * bj[x][y]
            bj[x].insert(0, 0)
    
    print(f'#{x + 1} {max}')        
