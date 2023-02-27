def comb(n, depth):
    if depth == n:
        comb_list.append(sel[::])
        return

    for f in range(4):
        sel[depth] = f
        comb(n, depth + 1)


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 벽치기
    matrix.insert(0, [8] * N)
    matrix.append([8] * N)
    for _ in matrix:
        _.insert(0, 8)
        _.append(8)

    core_line = [[set(), set(), set(), set()]for _ in range(13)]
    # print(core_line)
    core = 0

    # print(matrix)

    # 델타

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                core += 1

                for k in range(4):
                    x = i
                    y = j
                    while True:

                        if matrix[x + di[k]][y + dj[k]] == 8:
                            core_line[core][k] = (True, core_line[core][k])
                            break

                        elif matrix[x + di[k]][y + dj[k]] == 1:
                            core_line[core][k] = [False]
                            break

                        elif matrix[x + di[k]][y + dj[k]] == 0:
                            # print((x + di[k], y + dj[k]))
                            core_line[core][k].add((x + di[k], y + dj[k]))

                        x += di[k]
                        y += dj[k]

    # print(core_line, core)

    sel = [0] * core
    comb_list = []

    comb(core, 0)
    # print(comb_list)

    ans = 99999

    for i in range(len(comb_list)):
        count = 0
        line_visit = []
        for j in range(len(comb_list[i])):
            if core_line[j + 1][comb_list[i][j]][0] is True:
                for k in line_visit:
                    if k in core_line[j + 1][comb_list[i][j]][1]:
                        count = 999999999
                        break
                line_visit.extend(core_line[j + 1][comb_list[i][j]][1])
                count += len(core_line[j + 1][comb_list[i][j]][1])
            else:
                count = 99999999
                break
            # print(line_visit)
            if count >= ans:
                break
        if count < ans:
            ans = count

    print(f'#{tc + 1} {ans}')
