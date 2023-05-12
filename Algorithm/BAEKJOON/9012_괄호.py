for tc in range(int(input())):
    cnt = 0
    for i in input():
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")