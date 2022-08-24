# 데크로 풀기
from collections import deque

for tc in range(10):
    T = int(input())
    queue = deque(map(int, input().split()))    # 데크 이용하여 변수에 값 저장
    now = 1                                     # 반복문 탈출을 위한 변수 지정

    # 5번의 사이클을 반복할 반복문
    while now:
        for i in range(1, 6):           # 5번 반복하여
            now = queue.popleft()       # 왼쪽 값을 추출 후
            now -= i                    # 1~5만큼 감소
            if now <= 0:                # 만약 감소했을 때 0보다 작거나 같다면?
                now = 0                 # 0으로 만든 뒤
                queue.append(now)       # 큐 오른쪽에 추가 후 반복문 종료
                break
            queue.append(now)           # 0이 아니라면 그냥 큐 오른쪽에 추가

    # 결과 출력
    print(f'#{T}', end=' ')
    for i in range(8):
        print(queue.popleft(), end=' ')
    print()
