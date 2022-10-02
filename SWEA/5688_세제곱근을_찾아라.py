for tc in range(int(input())):
    N = int(input())
    M = round(N ** (1 / 3))
    if M ** 3 == N:
        print(f'#{tc + 1} {M}')
    else:
        print(f'#{tc + 1} -1')
