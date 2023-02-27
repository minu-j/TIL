words = [list(input()), list(input()), list(input()), list(input()), list(input())]

for i in range(15):
    for j in range(5):
        if len(words[j]) <= i:
            continue
        else:
            print(words[j][i], end='')