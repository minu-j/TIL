# 입력받은 10진수 N을 2진수로 변환하여 리스트에 2진수 값을 저장하는 함수
def bin2(n, depth):
    if depth == 14:
        return
    if 2 ** -depth == n:
        bin_list.append('1')
        return
    elif 2 ** -depth > n:
        bin_list.append('0')
        bin2(n, depth + 1)
    else:
        bin_list.append('1')
        bin2(n - (2 ** -depth), depth + 1)


for tc in range(int(input())):
    N = float(input())
    bin_list = []
    bin2(N, 1)
    if len(bin_list) > 12:
        print(f'#{tc + 1} overflow')
    else:
        print(f'#{tc + 1} {"".join(bin_list)}')
