for tc in range(int(input())):
    N, Q = map(int, input().split())
    box = [0] * N   # N 길이만큼 0이 채워진 박스 리스트 생성

    for i in range(1, Q + 1):       # Q회만큼 반복시행
        L, R = map(int, input().split())
        for j in range(L - 1, R):   # L부터, R까지의 박스 숫자를
            box[j] = i              # i로 변경

    print(f'#{tc + 1} {" ".join(map(str, box))}')   # box리스트를 join해서 출력
