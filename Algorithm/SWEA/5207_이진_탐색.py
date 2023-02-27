def bin_search(l, r, m, t):
    global side
    global ans

    if t == list_A[m]:   # 찾으면 정답 +1 후 종료
        ans += 1
        return

    if t < list_A[m]:   # 찾는 값이 왼쪽에 있을 때,
        if side != 'left':   # 이전에 봤던 곳이 왼쪽이 아닌 경우에만
            side = 'left'
            bin_search(l, m - 1, (l + m - 1) // 2, t)   # 왼쪽 탐색
        else:
            return
    else:
        if side != 'right':
            side = 'right'
            bin_search(m + 1, r, (m + 1 + r) // 2, t)
        else:
            return


for tc in range(int(input())):
    N, M = map(int, input().split())
    list_A = sorted(list(map(int, input().split())))
    list_B = sorted(list(map(int, input().split())))

    ans = 0
    # B에 있는 값 순서대로 검증
    for target in list_B:
        side = ''
        if target in list_A:   # 찾는 값이 A 안에 있는 경우에만 실행
            bin_search(0, N - 1, (N - 1) // 2, target)

    print(f'#{tc + 1} {ans}')
