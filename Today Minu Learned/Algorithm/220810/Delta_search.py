T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_num = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue

                sum_num += abs(arr[ni][nj] - arr[i][j])

    print(sum_num)