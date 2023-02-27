# 재귀로 모든 경로 휘저으며 찾기
def move(y, x, depth):
    global sum_num
    global ans

    sum_num += matrix[y][x]   # 해당하는 값을 누적합에 더해줌

    if depth == (N - 1) * 2:   # 최대 길이에 도달(오른쪽 아래)했다면 종료하고 누적값이 정답보다 작다면 정답 변수에 대치
        if sum_num < ans:
            ans = sum_num
        sum_num -= matrix[y][x]    # 함수 빠져나가기 전에 더했던 값 빼기
        return

    # 아래로 이동
    if y + 1 < N:
        move(y + 1, x, depth + 1)

    # 오른쪽으로 이동
    if x + 1 < N:
        move(y, x + 1, depth + 1)

    sum_num -= matrix[y][x]    # 함수 빠져나가기 전에 더했던 값 빼기


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    sum_num = 0
    ans = 9999999999999999999999
    move(0, 0, 0)

    print(f'#{tc + 1} {ans}')
