for tc in range(int(input())):
    str1, str2 = list(input()), input()
    print(f'#{tc + 1} {max(list(str2.count(i) for i in str1))}')