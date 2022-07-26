num = list(map(int, input().split())) # 1 1 3 3 0 1 1

now = 1
pre = 0

for i in num:
    if num[now] == num[pre]: # 이전 숫자와 지금 숫자가 같을 경우
        del num[now] # 이전 리스트 값을 제거

    now += 1
    pre += 1

print(num)