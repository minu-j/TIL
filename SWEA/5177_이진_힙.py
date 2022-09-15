for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    tree = [0]

    for i in arr:
        tree.append(i)
        if