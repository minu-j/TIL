# 연이어진 box의 세로*가로 크기를 구하고, 방문한 box의 위치를 기록하는 함수
def search(x, y):
    x_count = 1
    y_count = 1
    while matrix[x + x_count][y] != 0:
        x_count += 1
    while matrix[x][y + y_count] != 0:
        y_count += 1

    for xi in range(x_count):
        for yj in range(y_count):
            visited.append((x + xi, y + yj))

    box_list.append((x_count, y_count))


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 테두리 치기
    for _ in range(N):
        matrix[_].insert(0, 0)
        matrix[_].append(0)
    matrix.insert(0, [0] * (N + 2))
    matrix.append([0] * (N + 2))

    visited = []
    box_list = []

    # 전체 box 배열을 순회하며, 0이 아니거나, 방문되지 않았다면 함수를 실행하는 반복문
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if matrix[i][j] != 0 and (i, j) not in visited:
                search(i, j)

    # 구해진 box 리스트를 조건에 맞게 정렬
    box_list = sorted(box_list, key=lambda x: (x[0] * x[1], x[0]))

    # 정렬된 리스트를 조건에 맞게 출력
    print(f'#{tc + 1} {len(box_list)}', end=' ')
    for i in range(len(box_list)):
        for j in box_list[i]:
            print(j, end=' ')
    print()
