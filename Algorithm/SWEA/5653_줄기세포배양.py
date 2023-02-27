for tc in range(int(input())):
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 초기상태 체크
    grid = {}
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                # ( 비활성상태 카운트, 활성상태 카운트, 첫번째 활성화 마킹 )
                grid[(i, j)] = [matrix[i][j], matrix[i][j], 1]

    for T in range(K):

        wait_for_copy = {}   # 번식 대기줄

        for cell in grid:   # 그리드 셀 순회

            # 비활성 카운트 -1
            if grid[cell][0]:
                grid[cell][0] -= 1
                continue

            # 활성애들 중에서 아직 목숨이 남아있는애들
            elif not grid[cell][0] and grid[cell][1]:

                # 첫번째 활성화일 경우, 첫번째 활성화 마킹 없앤 후 번식하기
                if grid[cell][2] == 1:
                    grid[cell][2] -= 1

                    # 번식하기
                    for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
                        # 번식하려는 좌표에 세포가 없을 경우에만 번식
                        if (cell[0] + di, cell[1] + dj) not in grid:
                            # 번식하려는 좌표에 이미 번식하려고 하는 세포가 있다면?
                            if (cell[0] + di, cell[1] + dj) in wait_for_copy:
                                # 값이 더 클 경우만 번식하기
                                if grid[cell][1] > wait_for_copy[(cell[0] + di, cell[1] + dj)][0]:
                                    wait_for_copy[(cell[0] + di, cell[1] + dj)] = [grid[cell][1], grid[cell][1], 1]
                            # 없다면 번식하기
                            else:
                                wait_for_copy[(cell[0] + di, cell[1] + dj)] = [grid[cell][1], grid[cell][1], 1]

                # 생명력 1 깎기
                grid[cell][1] -= 1

        # 번식 대기중인 셀 그리드에 추가하기
        for copy_cell in wait_for_copy:
            grid[copy_cell] = wait_for_copy[copy_cell]
        wait_for_copy.clear()

    # 시간 끝나면 살아있는 세포 찾기
    ans = 0
    for cell in grid:
        if grid[cell][1]:
            ans += 1

    print(f'#{tc + 1} {ans}')
