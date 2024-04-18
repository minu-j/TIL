win = {'H': 1, 'P': 2, 'S': 0}
N = int(input())
win_acc = [[0] * N for _ in range(3)]
win_acc_r = [[0] * N for _ in range(3)]

for i in range(N):
    gesture = input()
    win_acc[win[gesture]][i] = 1
    win_acc_r[win[gesture]][i] = 1

for i in range(1, N):
    for j in range(3):
        win_acc[j][i] = win_acc[j][i - 1] + win_acc[j][i]

for i in range(N - 2, -1, -1):
    for j in range(3):
        win_acc_r[j][i] = win_acc_r[j][i + 1] + win_acc_r[j][i]

ans = 0
for i in range(N - 1):
    for j in range(3):
        for k in range(3):
            acc = win_acc[j][i] + win_acc_r[k][i + 1]
            if ans < acc:
                ans = acc
print(ans)
