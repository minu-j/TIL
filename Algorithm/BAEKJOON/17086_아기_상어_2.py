from collections import deque

N, M = map(int, input().split())
shark_set = set()
safe_distance = dict()


def find_shark():
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] == 1:
                shark_set.add((i, j))


def find_safe_dist():
    di, dj = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    for (shark_i, shark_j) in shark_set:
        wait_list = deque([(shark_i, shark_j)])
        visited = {(shark_i, shark_j)}
        distance = 0
        while len(wait_list):
            for idx in range(len(wait_list)):
                (now_i, now_j) = wait_list.popleft()
                if (now_i, now_j) in safe_distance:
                    if safe_distance[(now_i, now_j)] > distance:
                        safe_distance[(now_i, now_j)] = distance
                else:
                    safe_distance[(now_i, now_j)] = distance
                for direction in range(8):
                    ni, nj = now_i + di[direction], now_j + dj[direction]
                    if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in shark_set and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        wait_list.append((ni, nj))
            distance += 1


find_shark()
find_safe_dist()
print(max(safe_distance.values()))
