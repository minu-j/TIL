n = int(input())
score = list(map(int, input().split()))
new_score = []

for i in range(len(score)):
    new_score.append(score[i] / max(score) * 100)

new_avg = sum(new_score) / len(score)

print(new_avg)