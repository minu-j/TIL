for i in range(10):
    N = int(input())    # 테스트케이스의 길이 입력
    case = list(map(int, input().split()))

    buildings = [0] * (N + 4)   # 테스트케이스보다 4칸 긴 리스트를 만들고

    for j in range(N):  # 테스트케이스 양옆 2칸을 0으로 하는 리스트 생성
        buildings[j + 2] = case[j]

    ans = 0     # 정답 출력을 위한 ans변수 할당
    
    for j in range(N):  # 테스트케이스 길이만큼 반복
        max_num = 0

        for k in range(5):  # 각 빌딩마다 양옆 두 칸의 빌딩과 높이를 비교하는 반복문
            if k == 2:     # 자기 자신과의 비교하게 될 경우
                continue   # 해당 비교는 무시
            elif case[j] <= buildings[j + k]:   # j번째 빌딩이 양옆 두 칸의 빌딩보다 작을 경우
                max_num = 256                     # max_num  최대값으로
            else:
                if max_num < buildings[j + k]:  # 비교를 위해 양옆 두 칸의 빌딩의 크기 중 제일 큰 빌딩을 찾아서
                    max_num = buildings[j + k]  # max 변수에 할당
        
        if max < case[j]:           # j번째 빌딩이 max_num 보다 작다면
            ans += (case[j] - max_num  # ans 변수에 층수의 차이만큼을 가산

    print(f'#{i + 1} {ans}')