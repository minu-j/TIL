def f(depth, start):

    if depth == 3:
        for i in range(3):
            print(sel[i], end=' ')
        print()
        return

    else:
        for i in range(start, 4):
            sel[depth] = cards[i]
            f(depth + 1, i + 1)


cards = ['A', 'B', 'C', 'D']
sel = [0] * 3

f(0, 0)