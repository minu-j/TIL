N = int(input())
ans = 1
while True:
    now = ans
    for i in str(ans):
        now += int(i)
    if now > 1000000:
        print(0)
        exit(0)
    elif now == N:
        print(ans)
        exit(0)
    else:
        ans += 1