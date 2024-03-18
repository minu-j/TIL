# 완전탐색
# 9P3은 504이므로 10^5번 돌아도 멀쩡함
# N이 최대 100이라 완탐으로 풀 수 있을듯.

from itertools import permutations, combinations

num_set = set(map(lambda x: ''.join(x),
                  permutations(map(str, range(1, 10)), 3)))

for turn in range(int(input())):
    qusetion, strike, ball = input().split()
    strike, ball = int(strike), int(ball)
    possible_num_set = set()

    for num in num_set:
        strike_cnt, ball_cnt = 0, 0

        for i in range(3):
            if num[i] == qusetion[i]:   # strike 카운트
                strike_cnt += 1
            elif num[i] in qusetion:    # ball 카운트
                ball_cnt += 1
        if strike_cnt == strike and ball_cnt == ball:
            possible_num_set.add(num)

    num_set = possible_num_set

print(len(num_set))
