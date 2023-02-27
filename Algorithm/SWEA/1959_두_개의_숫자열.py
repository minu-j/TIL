case = int(input())

ai = []
bj = []

for x in range(case):
    n, m = map(int, input().split())

    if n >= m:
        ai.append(list(map(int, input().split())))
        bj.append(list(map(int, input().split())))

    elif m > n:
        bj.append(list(map(int, input().split())))
        ai.append(list(map(int, input().split())))

for _ in range(case):
    max = -9999999
    
    while len(bj[_]) <= len(ai[_]):
        mul = []
        for i in range(len(bj[_])):
            mul.append(bj[_][i] * ai[_][i])
        
        if sum(mul) > max:
            max = sum(mul)

        bj[_].insert(0, 0)
    
    print(f'#{_ + 1} {max}')   