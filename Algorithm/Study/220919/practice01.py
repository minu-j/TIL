for tc in range(int(input())):
    arr = input()
    for i in range(0, len(arr), 7):
        print(int('0b' + arr[i:i + 7], 2), end=' ')
    print()

