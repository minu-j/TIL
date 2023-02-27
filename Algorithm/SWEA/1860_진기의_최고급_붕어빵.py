for tc in range(int(input())):
    N, M, K = map(int, input().split())
    C = sorted(list(map(int, input().split())))
    ans = 'Possible'

    # 손님 N 명, M 초마다 K 개 붕어빵

    # 각 시간(초)마다 몇명의 손님이 오는지 체크하기
    timeline = [0] * (max(C) + 1)   # 타임라인의 길이는 제일 늦게 오는 손님 +1
    for i in C:                     # 손님 리스트를 돌면서 해당 시간 인덱스에 +1
        timeline[i] += 1

    fish = 0
    count = 0

    for i in range(len(timeline)):  # 타임라인을 1초씩 살펴보기
        if i > 0 and i % M == 0:    # 0보다 크고, M으로 나눈 나머지가 0이면 붕어빵을 만들 수 있으므로
            fish += K               # 붕어빵 +K

        fish -= timeline[i]         # 해당 시간의 손님만큼 붕어빵을 가져감

        if fish < 0:                # 붕어빵이 다 떨어져버리면
            ans = 'Impossible'      # 불가능 선언 후 반복문 종료
            break

    print(f'#{tc + 1} {ans}')
