from collections import deque


# 해당하는 자석을 특정 방향으로 회전시키고, 연결된 다른 자석을 재귀로 회전
def move(n, d):
    rotated.append(n)
    if d == 1:
        mags[n].appendleft(mags[n].pop())   # 1이면 시계 방향으로 회전
    else:
        mags[n].append(mags[n].popleft())   # -1이면 시계 반대 방향으로 회전
    if len(is_mag_connect[n]) > 0:   # 연결된 자석이 1개 이상이라면
        for _ in is_mag_connect[n]:
            if _ not in rotated:   # 회전된 적이 없다면
                move(_, -d)   # 연결된 다른 자석을 반대 방향으로 돌리기


for tc in range(int(input())):
    K = int(input())
    mags = [deque(map(int, input().split())) for _ in range(4)]
    mags.insert(0, 0)

    for turn in range(K):
        is_mag_connect = [[] for _ in range(5)]
        N, D = map(int, input().split())

        # 각 자석이 연결되어있는지 여부 확인해서 그래프 그리기
        for i in range(1, 4):
            if mags[i][2] ^ mags[i + 1][6] == 1:
                is_mag_connect[i].append(i + 1)
                is_mag_connect[i + 1].append(i)

        # 회전시키기
        rotated = []   # 이미 회전되었는지 체크용 리스트
        move(N, D)

    # 점수계산
    score = 0
    for idx, mag in enumerate(mags[1:]):
        if mag[0] == 1:
            score += 2 ** idx

    print(f'#{tc + 1} {score}')
