def search(n, x, y):
    sel[x][y] = 1
    for i in range(n):
        for j in range(n):
            if x - i == y - j:
                sel[i][j] = 1
            elif x + y == i + j:
                sel[i][j] = 1
            elif x == i or y == j:
                sel[i][j] = 1


sel = [[0] * 8 for _ in range(8)]

search(8, 4, 4)

print(sel)