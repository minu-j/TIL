arr = set()
for tc in range(int(input())):
    arr.add(input())
for word in sorted(list(arr), key=lambda x: (len(x), x)):
    print(word)
