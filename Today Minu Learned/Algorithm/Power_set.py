arr = ['A', 'B', 'C']
check = [0, 0, 0]


def powerset(idx):
    if idx == 3:
        print(*check)
        return

    check[idx] = 0
    powerset(idx + 1)

    check[idx] = 1
    powerset(idx + 1)

powerset(0)


