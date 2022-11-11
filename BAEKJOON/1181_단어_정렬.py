arr = []
for tc in range(int(input())):
    arr.append(input())
arr = sorted(arr, key=lambda x: (len(x), x))
for _ in arr:
    print(_)