from collections import deque
from pprint import pprint

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

def move():
    q0 = deque([prisoner[0]])
    q1 = deque([prisoner[1]])
    visited = {}
    visited[prisoner[0]] = 0
    visited[prisoner[1]] = 0
    while q0 or q1:
        if q0:
            for _ in range(len(q0)):
                i, j = q0.popleft() 
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if (ni, nj) in aisles and (ni, nj) not in visited:
                        visited[(ni, nj)] = visited[(i, j)] + aisles[(ni, nj)]
                        print('aisles 0', ni, nj, visited[(ni, nj)])
                        if aisles[(ni, nj)]:
                            q0.append((ni, nj))
                        else:
                            q0.appendleft((ni, nj))
                    if (ni, nj) in exits:
                        print('0', ni, nj, visited[(i, j)] + exits[(ni, nj)])
        if q1:
            for _ in range(len(q1)):
                i, j = q1.popleft() 
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if (ni, nj) in aisles and (ni, nj) not in visited:
                        visited[(ni, nj)] = visited[(i, j)] + aisles[(ni, nj)]
                        print('aisles 1', ni, nj, visited[(ni, nj)])
                        if aisles[(ni, nj)]:
                            q1.append((ni, nj))
                        else:
                            q1.appendleft((ni, nj))
                    if (ni, nj) in exits:
                        print('1', ni, nj, visited[(i, j)] + exits[(ni, nj)])


# for tc in range(int(input())):
N, M = map(int, input().split())
aisles = {}
exits = {}
prisoner = []
for n in range(N):
    row = input()
    for m in range(M):
        if row[m] == '$':
            prisoner.append((n, m))
        if n == 0 or n == N - 1 or m == 0 or m == M - 1:
            if row[m] == '.' or row[m] == '$':
                exits[(n, m)] = 0
            elif row[m] == '#':
                exits[(n, m)] = 1
        else:
            if row[m] == '.' or row[m] == '$':
                aisles[(n, m)] = 0
            elif row[m] == '#':
                aisles[(n, m)] = 1
move()