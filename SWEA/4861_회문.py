T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N - M + 1):

            # 가로 회문 검사
            word_h = arr[i][j:j + M]
            if word_h == word_h[::-1] and len(word_h) == M:   # 회문이고, 길이가 M과 같으면
                ans = ''.join(word_h)   # 리스트를 join해서 정답 변수에 저장

            # 세로 회문 검사
            word_v = []
            for k in range(M):
                word_v.append(arr[j + k][i])
            if word_v == word_v[::-1] and len(word_h) == M:
                ans = ''.join(word_v)

    print(f'#{tc + 1} {ans}')
