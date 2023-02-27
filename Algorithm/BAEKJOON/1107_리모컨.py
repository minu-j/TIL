now = 100
target = int(input())
n = int(input())
button_set = set(range(0, 10))
if n > 0:
    button_set = button_set - set(map(int, input().split()))

ans = abs(target - now)

count = 0
ch_up = ch_down = target

same = True

while True:
    if count + len(str(target)) >= ans:
        break

    up = down = True

    for j in str(ch_up):
        if int(j) not in button_set:
            up = False
            break

    for k in str(ch_down):
        if int(k) not in button_set:
            down = False
            break

    # print(up, ch_up, down, ch_down, count)

    if up:
        if ans > count + len(str(ch_up)):
            ans = count + len(str(ch_up))

    if down:
        if ans > count + len(str(ch_down)):
            ans = count + len(str(ch_down))
        break

    ch_up += 1
    if ch_down - 1 >= 0:
        ch_down -= 1

    count += 1

print(ans)
