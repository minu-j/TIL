for tc in range(int(input())):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split('0'))) for _ in range(N)]


    ans = 0

    print(f'#{tc + 1} {ans}')
