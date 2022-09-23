import pprint

move_direction = {1: (-1, 0),
                  2: (1, 0),
                  3: (0, -1),
                  4: (0, 1)}

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    micro_list = []

    for k in range(K):
        micro_list.append(list(map(int, input().split())))

    for turn in range(M):
        visited = [(0, 0)] * len(micro_list)

        for idx, micro in enumerate(micro_list):
            print(idx, micro, visited)
            micro[0] += move_direction[micro[3]][0]
            micro[1] += move_direction[micro[3]][1]





        pprint.pprint(micro_list)

    # print(f'#{tc + 1} {ans}')