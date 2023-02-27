N = int(input())

count = 665
while N > 0:
    count += 1
    if '666' in str(count):
        N -= 1
print(count)