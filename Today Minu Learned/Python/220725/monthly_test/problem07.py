# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    bin = []
    while True:
        while n > 1:
            bin.append(n % 2)
            n = n // 2
            dec_to_bin(n)
        bin.append(n)
        break

    bin = bin[::-1]

    ans = ''
    for i in bin:
        ans += str(i)
    return int(ans)

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010