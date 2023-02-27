T = int(input()) # 테스트케이스의 갯수

for i in range(T):
    cards = map(int, list(input()))   # 카드 입력
    count = [0] * 12                  # 각 숫자의 카드를 셀 빈 리스트 생성
    baby_gin = 0                      # baby gin을 판별할 변수 생성

    for j in cards:   # 각 숫자별 카드의 갯수 카운트
        for k in range(10):
            if j == k:
                count[k] += 1

    for j in range(10):      # 0번 카드부터 9번 카드까지 반복하여
        while True:
            if count[j] >= 3:    # 갯수가 3보다 크다면 Triplet이므로
                baby_gin += 1    # baby_gin +1 후
                count[j] -= 3    # 해당 갯수 카드를 차감
            elif count[j] >= 1 and count[j + 1] >= 1 and count[j + 2] >= 1:   # 또는 해당 카드부터 2번째 이후 카드까지 1 이상이면 run이므로
                baby_gin += 1      # baby_gin +1 후
                count[j] -= 1      # 각 카드를 차감
                count[j + 1] -= 1
                count[j + 2] -= 1
            else:
                break

    if baby_gin == 2:   # 만약 triplet 또는 run이 2면 1 출력
        print(f'#{i + 1} 1')
    else:               # 아니면 0
        print(f'#{i + 1} 0')
