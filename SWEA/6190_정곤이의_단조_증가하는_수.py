# 단조인지 아닌지 판단하는 함수
def danjo(n, m):
    nm = list(map(int, (list(str(n * m)))))   # 두 수의 곱을 리스트로 입력받고,
    count = 0
    for _ in range(len(nm) - 1):   # 전체 숫자 자릿수의 길이 -1만큼 반복하여
        if nm[_] > nm[_ + 1]:      # 해당 숫자가 다음 수보다 크다면 False
            return False
        else:
            count += 1             # 조건에 맞다면 카운트 +1
    if count == len(nm) - 1:       # 카운트가 자릿수 길이 -1과 같다면 True
        return True


for tc in range(int(input())):
    N = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)   #
    max_danjo = -1

    for i in range(N):
        for j in range(i + 1, N):
            if danjo(arr[i], arr[j]):
                if (arr[i] * arr[j]) > max_danjo:
                    max_danjo = arr[i] * arr[j]
                    break

    print(f'#{tc + 1} {max_danjo}')
