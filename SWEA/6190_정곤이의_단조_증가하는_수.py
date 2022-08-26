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
    arr = sorted(list(map(int, input().split())), reverse=True)   # 큰 값부터 확인하도록 내림차순으로 정렬
    max_danjo = -1      # 단조가 없다면 -1 출력되도록 초기값을 -1로 지정
    
    # 두 수의 곱이 단조인지 확인
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] * arr[j] > max_danjo:         # 두 수의 값이 지금까지 가장 큰 단조보다 크다면?
                if danjo(arr[i], arr[j]):           # 그리고 단조라면?
                    max_danjo = arr[i] * arr[j]     # 가장 큰 단조를 바꿔주고
                    break                           # 해당 줄은 더이상 볼 필요가 없으므로(내림차순이므로) 다음줄로 넘어감

    print(f'#{tc + 1} {max_danjo}')
