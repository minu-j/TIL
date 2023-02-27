for tc in range(int(input())):
    N = int(input())
    ans = []
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    # 각 화폐가 몇장 필요한지 계산하는 반복문
    for idx, i in enumerate(money):
        ans.append(N // i)          # 가격을 화폐로 나눈 몫(지폐 장 수)를 정답 리스트에 추가
        N = N - (i * ans[idx])      # 다음 계산을 위해 가격을 차감

    # 양식에 맞게 출력
    print(f'#{tc + 1}')
    for i in ans:
        print(i, end=' ')
    print()