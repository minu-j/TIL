N = int(input())
col_1 = [0, 0]
col_2 = [0, 0]
col_3 = [0, 0]
for i in range(N):
    f, s, t = map(int, input().split())
    f_max = max(f + col_1[0], f + col_2[0])
    f_min = min(f + col_1[1], f + col_2[1])
    s_max = max(s + col_1[0], s + col_2[0], s + col_3[0])
    s_min = min(s + col_1[1], s + col_2[1], s + col_3[1])
    t_max = max(t + col_2[0], t + col_3[0])
    t_min = min(t + col_2[1], t + col_3[1])
    col_1 = [f_max, f_min]
    col_2 = [s_max, s_min]
    col_3 = [t_max, t_min]

print(max(col_1[0], col_2[0], col_3[0]), min(col_1[1], col_2[1], col_3[1]))
