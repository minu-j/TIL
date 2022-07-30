n = int(input())
i = 0
while i < n:
    score = 0
    case = input()
    scores = [0] * len(case)
    for _ in range(len(case)):
        if case[_] == 'O':
            scores[_] = scores[_] + 1 + score
            score += 1
        else:
            score = 0
    print(sum(scores))
    i += 1