for T in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]

    max_len = 0

    for i in range(100):   # 가로세로 2차원으로 모든 글자를 시작 포인트로 검사
        for j in range(100):
            word_v = []   # 세로 단어를 저장할 빈 리스트 생성

            for k in range(100 - j):   # 해당 좌표의 글자를 시작으로 모든 길이만큼 검사하는 반복문
                # 가로 회문 검사
                word_h = arr[i][j:j + k + 1]
                if word_h == word_h[::-1]:
                    if max_len < len(word_h):   # 길이가 제일 길면 변수에 저장
                        max_len = len(word_h)

                # 세로 회문 검사

                word_v.append(arr[j + k][i])
                if word_v == word_v[::-1]:
                    if max_len < len(word_v):
                        max_len = len(word_v)

    print(f'#{tc} {max_len}')