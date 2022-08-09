T = int(input()) # 테스트케이스의 갯수

for i in range(T):
    N = int(input())
    box_list = list(map(int, input().split()))

    max_fall = 0

    for j in range(N):   # 박스의 가로 길이만큼 반복
        max_count = 0

        for k in box_list[j + 1:]:   # 해당 박스의 오른쪽 칸만큼만 반복
            if box_list[j] > k:      # 박스 오른쪽에 있는 박스보다 해당 박스가 크다면
                max_count += 1       # 1칸 떨어지는 것을 카운트

        if max_count > max_fall:     # 만약 카운트한 값이 최대 낙차보다 크다면
            max_fall = max_count     # 변수에 할당

    print(f'#{i + 1} {max_fall}')  # 최대 낙차 값 출력