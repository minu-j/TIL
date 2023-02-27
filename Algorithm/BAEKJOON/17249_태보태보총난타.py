left, right = input().split('(^0^)')
left_count = right_count = 0
for i in left:
    if i == '@':
        left_count += 1

for i in right:
    if i == '@':
        right_count += 1

print(left_count, right_count)