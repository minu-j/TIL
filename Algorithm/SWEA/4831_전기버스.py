T = int(input()) # 테스트케이스의 갯수

for i in range(T):
    K, N, M  = map(int, input().split())         # K, N, M 입력
    chargers = list(map(int, input().split()))   # 충전기 위치 입력
    bus_stops = [0] * (N + K)                    # 정류장을 1차원 배열로 표시하기 위한 리스트 생성
    bus_stops[N] += 1                            # 마지막 정류장에 충전기가 있는것으로 표기하여 K개 이하의 정류장이 남았을 때 충전하지 않도록 함

    for j in chargers:       # 충전기의 위치를 1차원 배열로 표시
        for k in range(N):
            if j == k:
                bus_stops[k] += 1

    charge_count = 0   # 충전 횟수를 카운트하기 위한 변수
    battery = K        # 배터리를 K만큼 충전
    possible = True    # 실행 가능한지 여부 판단하기 위한 변수

    for j in range(1, N):       # 1부터 N까지의 각 정류장에서 충전을 해야하는지 여부를 판단하기 위한 반복문
        battery -= 1            # 정류장을 한 칸 이동하면 배터리 -1
        if battery < 0:         # 배터리가 0보다 작아지면
            possible = False    # 완주 불가능
        elif bus_stops[j] == 1:     # 정류장에 충전기가 있을 경우,
            if battery == 0:        # 배터리가 0이면
                battery = K         # K만큼 충전
                charge_count += 1   # 배터리 충전 횟수 +1
            elif battery >= 1:      # 배터리가 1 이상 남았을 경우
                left_stops = 0      # 남은 충전기 갯수를 확인하기 위한 변수
                for k in range(battery):            # 남은 배터리로 갈 수 있는 정류장 중에서
                    if bus_stops[j + k + 1] == 1:   # 충전기가 있는 정류장이 있다면?
                        left_stops += 1             # 남은 충전기 갯수 +1
                if left_stops >= 1:     # 만약 남은 정류장에 충전기가 있다면
                    pass                # 충전하지 않고 지나감
                else:                   # 남은 정류장에 충전기가 없다면
                    battery = K         # K만큼 충전
                    charge_count += 1   # 배터리 충전 횟수 +1

    if possible is False:      # 완주가 불가능하다면
        print(f'#{i + 1} 0')   # 0을 출력

    else:
        print(f'#{i + 1} {charge_count}')