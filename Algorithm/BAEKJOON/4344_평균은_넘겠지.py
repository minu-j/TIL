c = int(input())
for i in range(c):
    case = list(map(int, input().split()))
    average = (sum(case) - case[0]) / case[0]
    up = []
    for _ in range(case[0]):
        if case[_ + 1] > average: up.append(case[_ + 1])
    print(f'{len(up) / len(case[1:]) * 100:.3f}%')