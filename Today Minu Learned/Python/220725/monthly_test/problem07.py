# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    bin_num = []

    while n > 1:
        if n == 1:
        elif n == 0
        else:
        bin_num.append(n % 2)
        n = n // 2
        print(bin_num)

     
    n = bin_num[::-1]
    return n

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010