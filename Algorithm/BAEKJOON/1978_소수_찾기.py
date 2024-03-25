N = int(input())


def is_prime_number(x):
    if x < 2:
        return False
    for n in range(2, x):
        if not x % n:
            return False
    return True


ans = 0
for num in list(map(int, input().split())):
    if is_prime_number(num):
        ans += 1

print(ans)
