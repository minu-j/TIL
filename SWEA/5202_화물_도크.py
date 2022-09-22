for tc in range(int(input())):
    N = int(input())

    works = []

    for i in range(N):
        works.append(tuple(map(int, input().split())))

    works.sort()

    select = [0] * N
    ans = 0
    comb(0)



    print(f'#{tc + 1} {ans}')
