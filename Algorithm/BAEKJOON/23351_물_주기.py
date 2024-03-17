# 완전탐색으로 풀면
# 화분들 중 하나에 물을 주는 경우의 수, 다음날 모든 화분들 중 하나에 물을 주는 경우의 수...
# 100^100?

# A는 N의 약수다!!!

N, K, A, B = map(int, input().split())
pots, day, pointer = [K] * N, 0, 0


# 물 못받은 화분에 물주기
def increase_moisture():
    global pointer
    for waterIdx in range(pointer, pointer + A):
        pots[waterIdx] += B
        pointer = (pointer + 1) % N


# 모든 화분의 수분 증발
def decrease_moisture():
    for i in range(N):
        pots[i] -= 1
        if not pots[i]:
            return False
    return True


while True:
    day += 1
    increase_moisture()
    if not decrease_moisture():
        # 화분 중 하나라도 수분이 0이 될 경우 중단
        break

print(day)

# 근데 결국 죽는건 가장 낮게 증가하는 맨 뒤 숫자때문 아닌가?
# 맨 뒤 숫자만 고려해서 구현해보자

N, K, A, B = map(int, input().split())
order, pot, day = N / A, K, 0

# 화분들 중 가장 오른쪽 화분의 수분이 날짜랑 같아질 때 까지 반복
while pot != day:
    # 가장 오른쪽 화분에 물을 줄 차례가 되면 물주기
    if order == 1:
        pot += B
    # 한바퀴 다 돌면 차례 초기화
    elif not order:
        order = N / A
    order -= 1
    day += 1

print(day)
