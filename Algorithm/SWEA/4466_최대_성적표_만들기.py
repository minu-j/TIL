for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))   # 성적을 정렬된 리스트로 입력받기

    ans = 0

    for i in range(K):     # K만큼 반복하며
        ans += arr.pop()   # 리스트 pop, 정답에 가산

    print(f'#{tc + 1} {ans}')