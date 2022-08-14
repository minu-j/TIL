for tc in range(10):
    N = int(input())
    table = [list(input()) for _ in range(8)]
    for i in range(8):
        for j in range(N - 1):
            table[i].append('*')
    for i in range(N - 1):
        table.append(['*'] * len(table[0]))
    ans = 0
    for i in range(8):
        for j in range(8):
            count_h = 0
            count_v = 0
            for k in range(N // 2):
                if table[i][j + k] == table[i][j + N - 1 - k]:
                    count_h += 1
                if table[j + k][i] == table[j + N - 1 - k][i]:
                    count_v += 1
            if count_h == N // 2:
                ans += 1
            if count_v == N // 2:
                ans += 1
    print(f'#{tc + 1} {ans}')