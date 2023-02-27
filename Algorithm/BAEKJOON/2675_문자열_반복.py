for tc in range(int(input())):
    n, words = map(str, input().split())
    ans = []
    for word in words:
        ans.append(word * int(n))
    print(''.join(ans))