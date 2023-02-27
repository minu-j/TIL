arr = ['A', 'B', 'C']
check = [0, 0, 0, 0, 0]

def powerset(idx):
    if idx == 5:
        if sum(check) == 3:
            A = []
            for idx_, _ in enumerate(check):
                if _:
                    A.append(idx_ + 1)
            arrow.append(A)

        return

    check[idx] = 0
    powerset(idx + 1)

    check[idx] = 1
    powerset(idx + 1)

powerset(0)

print(arrow)

arrow = []