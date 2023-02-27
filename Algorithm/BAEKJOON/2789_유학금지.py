X = 'CAMBRIDGE'
word = list(input())
for i in range(len(word)):
    for j in X:
        if word[i] == j:
            word[i] = ''
for i in word:
    print(i, end='')