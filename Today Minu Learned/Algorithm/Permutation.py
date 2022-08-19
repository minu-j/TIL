arr = ['A', 'B', 'C']
sel = [0, 0, 0]
check = [0, 0, 0]

def perm(depth):
    if depth == 3:
        print(sel)
        return
    for i in range(3):
        if not check[i]:
            check[i] = 1
            print('1', check, sel)
            sel[depth] = arr[i]
            print('2', check, sel)
            perm(depth + 1)
            print('3', check, sel)
            check[i] = 0
            print('4', check, sel)

print(perm(0))