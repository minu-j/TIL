import pprint

move_direction = {1: (-1, 0),
                  2: (1, 0),
                  3: (0, -1),
                  4: (0, 1)}


# 매 시간마다 미생물의 위치를 움직이는 함수
def move(m1):
    d = misang_dict[m1]['direction']
    misang_dict[m1]['position'][0] += move_direction[d][0]
    misang_dict[m1]['position'][1] += move_direction[d][1]


# 미생물이 가장자리에 도착했을 때 //2만큼을 죽이고, 방향을 반대로 바꾸는 함수
def kill(m2):
    misang_dict[m2]['head'] //= 2
    if misang_dict[m2]['direction'] == 1 or misang_dict[m2]['direction'] == 3:
        misang_dict[m2]['direction'] += 1
    elif misang_dict[m2]['direction'] == 2 or misang_dict[m2]['direction'] == 4:
        misang_dict[m2]['direction'] -= 1


for tc in range(int(input())):
    N, M, K = map(int, input().split())

    misang_dict = []
    for misang_k in range(K):
        misang = list(map(int, input().split()))

        misang_dict.append({'position': [misang[0], misang[1]],
                            'head': misang[2],
                            'direction': misang[3],
                            'is_alive': True})
    # pprint.pprint(misang_dict)

    for T in range(M):

        # 움직이기
        for i in range(len(misang_dict)):
            move(i)

        # 죽이고 방향 바꾸기
        for j in range(len(misang_dict)):
            if misang_dict[j]['position'][0] == 0 or misang_dict[j]['position'][0] == N - 1 or misang_dict[j]['position'][1] == 0 or misang_dict[j]['position'][1] == N - 1:
                kill(j)

        # 겹친애들 합치기
        for k in range(len(misang_dict)):
            for l in range(k, len(misang_dict)):
                if k != l and misang_dict[k]['position'] == misang_dict[l]['position']:
                    k_head = misang_dict[k]['head']
                    l_head = misang_dict[l]['head']
                    if k_head > l_head:
                        misang_dict[k]['head'] += misang_dict[l]['head']
                        misang_dict[l]['head'] = 0
                        misang_dict[l]['is_alive'] = False
                    else:
                        misang_dict[l]['head'] += misang_dict[k]['head']
                        misang_dict[k]['head'] = 0
                        misang_dict[k]['is_alive'] = False

        # 죽은애들은 없애기
        for o in range(len(misang_dict)):
            for p in range(len(misang_dict)):
                if not misang_dict[p]['is_alive']:
                    misang_dict.pop(p)
                    break




    # 남아있는 미생물 갯수 세기
    ans = 0
    for m in range(len(misang_dict)):
        ans += misang_dict[m]['head']

    print(f'#{tc + 1} {ans}')
