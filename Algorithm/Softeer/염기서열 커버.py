import sys

def check(a, b):
    word = []
    for i in range(len(a)):
        if a[i] != '.' and b[i] != '.' and a[i] != b[i]:
            return False
        elif a[i] == b[i]:
            word.append(a[i])
        else:
            if a[i] != '.':
                word.append(a[i])
            else:
                word.append(b[i])
    return word


N, M = map(int, input().split())

super_dna = [list(input())]
for n in range(N - 1):
    dna = input()
    is_marge = False
    for i in range(len(super_dna)):
        marged = check(dna, super_dna[i])
        if marged:
            super_dna[i] = marged
            is_marge = True
            break
    if not is_marge:
        super_dna.append(dna)

print(len(super_dna))