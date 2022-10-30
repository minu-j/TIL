import sys
input = sys.stdin.readline

pokemon = ['']

N, M = map(int, input().split())

for n in range(N):
    pokemon.append(input().rstrip('\n'))
for m in range(M):
    now = input().rstrip('\n')
    if now.isdigit():
        print(pokemon[int(now)])
    else:
        print(pokemon.index(now))
