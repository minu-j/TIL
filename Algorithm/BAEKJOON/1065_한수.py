N = int(input())
ans = 0
for i in range(1, N + 1):
    str_i = str(i)
    same = True
    g = 9999999999
    for j in range(len(str_i) - 1):
        if g == 9999999999:
            g = int(str_i[j + 1]) - int(str_i[j])
        else:
            if g == int(str_i[j + 1]) - int(str_i[j]):
                same = True
            else:
                same = False
                break
    if same:
        ans += 1
print(ans)