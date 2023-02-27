for tc in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split())) + [0]

    # 봉우리의 시작점을 체크해서 카운트
    ans = 0
    up = False   # 올라가고 있는 중인지?

    for i in range(N + 1):
        if arr[i + 1] >= arr[i] and up:   # 오르막길중이면 봉우리가 아님.
            continue
        elif arr[i + 1] > arr[i] and not up:   # 다음 지형이 더 높은데, 직전이 내리막이었다면 봉우리의 시작이므로 +1
            ans += 1
            up = True
        else:   # 나머지의 경우는 봉우리를 지난 경우이므로 오르막이 아님.
            up = False

    print(f'#{tc + 1} {ans}')
