dance = {'ChongChong'}
ans = 0
for tc in range(int(input())):
    A, B = input().split()
    if A in dance:
        dance.add(B)
    elif B in dance:
        dance.add(A)
print(len(dance))