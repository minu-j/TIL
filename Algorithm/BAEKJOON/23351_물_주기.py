# 완전탐색으로 풀면
# 화분들 중 하나에 물을 주는 경우의 수, 다음날 모든 화분들 중 하나에 물을 주는 경우의 수...
# 100^100?

# A는 N의 약수다!!!

# N, K, A, B = map(int, input().split())
# pots, day, pointer = [K] * N, 0, 0


# def increase_moisture():
#     global pointer
#     for waterIdx in range(pointer, pointer + A):
#         pots[waterIdx] += B
#         pointer = (pointer + 1) % N


# def decrease_moisture():
#     for i in range(N):
#         pots[i] -= 1
#         if not pots[i]:
#             return False
#     return True


# while True:
#     day += 1
#     increase_moisture()
#     if not decrease_moisture():
#         break

# print(day)

# 근데 결국 죽는건 가장 낮게 증가하는 맨 뒤 숫자때문 아닌가?
# 맨 뒤 숫자만 고려해서 구현해보자

N, K, A, B = map(int, input().split())
left, pot, day = N / A, K, 0

while pot != day:
    if left == 1:
        pot += B
    elif not left:
        left = N / A
    left -= 1
    day += 1

print(day)
