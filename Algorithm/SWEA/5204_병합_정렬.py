def marge_sort(num_list):
    if len(num_list) == 1:
        return num_list

    left = num_list[:(len(num_list)) // 2]
    right = num_list[(len(num_list)) // 2:]

    left_list = marge_sort(left)
    right_list = marge_sort(right)

    return marge(left_list, right_list)


def marge(left, right):
    global ans

    if left[-1] > right[-1]:
        ans += 1

    sorted_list = [0] * (len(left) + len(right))
    l, r, idx = 0, 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            sorted_list[idx] = left[l]
            l += 1
            idx += 1
        else:
            sorted_list[idx] = right[r]
            r += 1
            idx += 1

    while l < len(left):
        sorted_list[idx] = left[l]
        l += 1
        idx += 1
    while r < len(right):
        sorted_list[idx] = right[r]
        r += 1
        idx += 1

    return sorted_list


for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    sorted_arr = marge_sort(arr)

    print(f'#{tc + 1} {sorted_arr[N // 2]} {ans}')
