num_list = set(range(1, 10000))
visited = set()


def self_num(n):
    next_n = sum(map(int, list(str(n)))) + n
    if next_n > 10000 or n == next_n or next_n in visited:
        return
    else:
        if next_n in num_list:
            num_list.remove(next_n)
        visited.add(next_n)
        self_num(next_n)


for i in list(range(1, 10001)):
    self_num(i)

for j in num_list:
    print(j)
