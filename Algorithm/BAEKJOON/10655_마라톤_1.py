N = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(N)]


# 맨하탄 거리 구하는 함수
def get_manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


acc_dist = get_manhattan_dist(
    checkpoints[0], checkpoints[1])   # 체크포인트 건너뛰지 않았을 때 누적 거리
dist = [0, acc_dist]    # [현재에서 다음까지 거리, 다음에서 다다음까지 거리]
best_jump = 0    # 가장 효과적으로 건너뛴 거리

for n in range(N - 2):
    # 다음 체크포인트에서 다다음 체크포인트까지 거리 구하기
    next_dist = get_manhattan_dist(checkpoints[n + 1], checkpoints[n + 2])

    # 누적 거리에 더하기
    acc_dist += next_dist

    # 현재에서 다음 체크포인트까지 거리는 저장된 이전 거리 사용
    dist = [dist[1], next_dist]

    # 건너뛰어서 이득 본 거리
    # ((현재 -> 다다음 거리) - ((현재 -> 다음) + (다음 -> 다다음)))
    jumped_dist = sum(dist) - \
        get_manhattan_dist(checkpoints[n], checkpoints[n + 2])

    # 기가막힌 점프였다면 저장
    if jumped_dist > best_jump:
        best_jump = jumped_dist

# 정답은 누적 거리 - 가장 효과적으로 건너뛴 거리
print(acc_dist - best_jump)
