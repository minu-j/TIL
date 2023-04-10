N, M = map(int, input().split())
tree_list = sorted(list(map(int, input().split())), reverse=True)
tree_list.append(0)
cut_tree = 0
ans = 999999999999999999999999999

for idx in range(len(tree_list) - 1):
    if tree_list[idx] == tree_list[idx + 1]:
        continue
    else:
        cut_tree_sum = (tree_list[idx] - tree_list[idx + 1]) * (idx + 1)
        if cut_tree_sum + cut_tree > M:
            for h in range(tree_list[idx], tree_list[idx + 1], -1):
                if (tree_list[idx] - h) * (idx + 1) + cut_tree >= M:
                    print(h)
                    exit(0)
        elif cut_tree_sum + cut_tree == M:
            print(tree_list[idx + 1])
            exit(1)
        else:
            cut_tree += cut_tree_sum
