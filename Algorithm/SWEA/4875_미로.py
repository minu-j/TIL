# 미로찾는 함수
def maze(si, sj):
    global ans

    # 해당 좌표를 방문한 것으로 리스트 추가
    visit.append((si, sj))
    if ans:
        return

    # 상하좌우 네 방향을 탐색하며 이동
    for _ in range(4):

        # 만약 가려고 하는 칸이 도착점이면 정답은 1
        if matrix[si + di[_]][sj + dj[_]] == 3:
            ans = 1

        # 가려고 하는 칸이 방문되지 않았거나, 0이라면 해당 칸 방문
        elif (si + di[_], sj + dj[_]) not in visit and matrix[si + di[_]][sj + dj[_]] == 0:
            maze(si + di[_], sj + dj[_])


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]

    # 미로 범위 밖으로 벗어나지 않게 사방에 1을 둘러주는 작업
    for i in matrix:
        i.insert(0, 1)
        i.append(1)
    matrix.insert(0, [1] * len(matrix[0]))
    matrix.append([1] * len(matrix[0]))

    # 시작점이 어딘지 좌표를 확인
    for i in range(N + 2):
        for j in range(N + 2):
            if matrix[i][j] == 2:
                Si, Sj = i, j

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    visit = []
    ans = 0
    maze(Si, Sj)

    print(f'#{tc + 1} {ans}')
