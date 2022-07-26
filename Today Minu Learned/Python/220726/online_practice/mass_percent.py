percent = []
salt_water = []
i = 1

while True:
    inf = input(f'{i}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split()
    if 'Done' in inf:
        break
    else:
        percent.append(int(inf[0].rstrip('%')))
        salt_water.append(int(inf[1].rstrip('g')))
    i += 1

salt = []

for _ in range(len(salt_water)):
    salt.append(0.01 * percent[_] * salt_water[_])
    print(salt)

salt_percent = int((sum(salt) / sum(salt_water)) * 100)

print(f'{salt_percent:.1f}% {sum(salt_water)}g')