# 완전탐색
# 9P3은 504이므로 10^5번 돌아도 멀쩡함
# N이 최대 100이라 완탐으로 풀 수 있을듯.

from itertools import permutations, combinations

num_set = set(map(lambda x: ''.join(x),
                  permutations(map(str, range(1, 10)), 3)))

for turn in range(int(input())):
    qusetion, strike, ball = input().split()
    strike, ball = int(strike), int(ball)
    turn_possible_num_set = set()

    strike_idx_list = list(combinations(range(3), strike))
    ball_idx_list = []
    for i in range(len(strike_idx_list)):
        ball_idx_list.append(
            list(combinations(set(range(3)) - set(strike_idx_list[i]), ball)))

    for s, b in zip(strike_idx_list, ball_idx_list):
        possible_num_set = set()
        for num in num_set:
            isPossible = True
            for s_idx in s:
                if qusetion[s_idx] != num[s_idx]:
                    isPossible = False
            if not isPossible:
                continue

            if ball:
                for b_idx_list in b:
                    for b_idx in b_idx_list:
                        if (qusetion[b_idx] == num[b_idx]) and (num in possible_num_set):
                            possible_num_set.remove(num)
                        if not ((qusetion[b_idx] == num[b_idx]) or (qusetion[b_idx] not in num)):
                            possible_num_set.add(num)
            else:
                possible_num_set.add(num)

        turn_possible_num_set = turn_possible_num_set.union(possible_num_set)

    num_set &= turn_possible_num_set

print(len(num_set))
