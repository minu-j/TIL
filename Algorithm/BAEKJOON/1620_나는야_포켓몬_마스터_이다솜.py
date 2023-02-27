import sys
sys.stdin = open('input.txt', 'r')

pokemon = []

while True:
    a = input()
    pokemon.append(a)
    if a == 'chobits':
        break

print(pokemon)