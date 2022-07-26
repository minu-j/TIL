# 함수에 리턴값이 없는 경우

nums = [1, 2, 3, 4, 5]

def a():
    global nums
    nums = [1, 2, 3, 4]
    c = 4
    print(nums)
    print(id(c))

    def b():
        # nonlocal c
        # c = [1]
        print(id(c))
        c = [0]
    b()
    print(c)

a()

print(nums)