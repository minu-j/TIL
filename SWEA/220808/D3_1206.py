for i in range(10):
    N = int(input()) # 테스트케이스의 길이 입력
    case = list(map(int, input().split())) # 개별 테스트케이스 입력

    buildings = [0] * (N + 4) # 양옆 2칸 빈공간을 위한 N + 4개의 빈 리스트 생성

    for _ in range(N): # 테스트케이스 양옆에 2칸을 0으로 하는 리스트
        buildings[_ + 2] = case[_]

    ans = 0
    
    for _ in range(N):
        max = 0
        for height in range(5):
            if height == 2:
                continue
            elif case[_] <= buildings[_ + height]:
                max = 256
            else:
                if max < buildings[_ + height]:
                    max = buildings[_ + height]
        
        if max < case[_]:
            ans += (case[_] - max)

    print(f'#{i + 1} {ans}')

    i += 1