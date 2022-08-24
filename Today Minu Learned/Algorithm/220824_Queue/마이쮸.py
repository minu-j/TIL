# 데크로 풀기
from collections import deque

queue = deque()         # 대기줄을 저장할 큐 생성
taken = [0] * 100       # 각자 이미 가져간 마이쮸 갯수를 저장할 리스트 생성
mychu = 20              # 마이쮸는 20개
num = 1                 # 1번부터 시작

# 마이쮸를 나눠주는 반복문
while mychu:
    queue.append(num)           # 큐에 번호에 해당하는 대기인원 추가
    now = queue.popleft()       # 현재 마이쮸를 받아야 할 사람은 큐의 맨 왼쪽사람
    taken[now] += 1             # 해당 번호 사람이 받은 마이쮸 갯수를 누적
    mychu -= taken[now]         # 마이쮸를 가져가야하는 갯수만큼 차감
    if mychu <= 0:              # 남은 마이쮸가 0보다 작아지면
        print(f'마지막으로 마이쮸를 받은 사람은 {now}번')   # 누가 가져갔는지 출력 후
        break                                         # 반복문 종료
    else:
        print(f'{now}번이 마이쮸를 {taken[now]}개 가져갔고, 남은 마이쮸는 {mychu}개')
    queue.append(now)           # 가져간 후 곧바로 다시 줄서기
    num += 1                    # 1명이 더 와야하니까 번호 +1
