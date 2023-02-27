def solution(marbles):
    def score(arr):
        for i in range(len(arr) * 2 - 1):
            if len(arr) == 1:
                left = right = [1]
            elif i % 2 == 0:
                now = i // 2
                left = arr[:now]
                right = arr[now + 1:]
            else:
                now = i // 2
                left = arr[:now + 1]
                right = arr[now + 1:]

            if sum(left) == sum(right):
                first = abs(len(left) - len(right))
                second = len(arr)
                third = sum(arr)
                forth = ''
                for k in arr:
                    forth += str(k)
                ans.append((first, second, third, forth, arr[::]))

    def case(depth):
        if sel:
            score(sel)
        for i in range(len(marbles)):
            if check[i] == 0:
                sel.append(marbles[i])
                check[i] = 1
                case(depth + 1)
                sel.pop()
                check[i] = 0

    ans = []
    sel = []
    check = [0] * len(marbles)
    case(0)
    ans.sort(key=lambda x: (x[0], -x[1], -x[2], x[3]))
    return ans[0][4]


print(solution([1, 2, 3, 4, 4]))    # [1, 4, 4, 2, 3]
print(solution([5, 5, 1, 4]))       # [5, 4, 5]
print(solution([3, 9, 7, 5]))       # [3, 9, 5, 7]
print(solution([7, 3, 1]))          # [7]


