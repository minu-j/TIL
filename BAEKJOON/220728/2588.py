a, b = int(input()), int(input())
print(f'{(a * ((b % 100) % 10))}\n{a * ((b % 100) // 10)}\n{a * (b // 100)}\n{a * b}')