from collections import deque


def solution(edges, roots):
    tree = [[] for _ in range(len(edges) + 2)]
    answer = [0] * len(edges)
    for s, e in edges:
        tree[s].append(e)
        tree[e].append(s)
    # print(tree)

    for root in roots:
        visited = {root}
        q = deque([root])
        check = [False] * len(edges)

        while q:
            # print('')
            # print(q)
            now = q.popleft()
            # print('now', now)

            for index, edge in enumerate(edges):

                if now in edge and not check[index]:
                    if edge[0] == now:
                        check[index] = True
                    elif edge[1] == now:
                        # print(index, edge)
                        edges[index] = edges[index][::-1]
                        answer[index] += 1
                        check[index] = True

            # print(check)
            # print(edges)

            for r in tree[now]:
                if r not in visited:
                    visited.add(r)
                    q.append(r)

    return answer


print(solution([[1, 3], [1, 2], [2, 4], [2, 5]],  [2, 3]))  # [1,2,0,0]
print(solution([[1, 2], [1, 3], [2, 4]], [3, 4, 1, 2]))     # [3,2,2]
