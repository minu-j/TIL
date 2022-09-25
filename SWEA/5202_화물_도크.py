for tc in range(int(input())):
    N = int(input())

    works = [tuple(map(int, input().split())) for i in range(N)]
    works.sort(key=lambda x: (x[1], -x[0]))   # 종료시간이 이르고, 시작시간이 늦은 순서대로 정렬

    finish = 0
    ans = 0

    for work in works:
        if work[0] >= finish:   # 직전 활동이 끝난 시간보다 시작시간이 이를 경우 +1
            finish = work[1]
            ans += 1

    print(f'#{tc + 1} {ans}')
