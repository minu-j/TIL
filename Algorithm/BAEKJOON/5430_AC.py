from collections import deque

for tc in range(int(input())):
    F = input()
    n = int(input())
    arr = input()
    pop_num = 0
    f_count = F.count('D')

    if arr == '[]' and f_count or f_count > n:
        print('error')
        continue

    elif f_count == n:
        print('[]')
        continue

    else:
        arr = deque(list(map(str, arr.strip('[]').split(','))))
        d = 0
        r_count = 0
        for f in F:
            if f == 'R':
                r_count += 1
                if d == 0:
                    d = 1
                else:
                    d = 0
            else:
                if len(arr) == 0:
                    arr = 'error'
                    print('error')
                    break

                if d == 0:
                    arr.popleft()
                else:
                    arr.pop()
        if arr != 'error':
            if r_count % 2 == 1:
                print('[' + ','.join(list(arr)[::-1]) + ']')
            else:
                print('[' + ','.join(arr) + ']')