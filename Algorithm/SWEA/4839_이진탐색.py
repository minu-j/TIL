T = int(input())

for tc in range(T):
    P, Pa, Pb = map(int, input().split())
    l, r, c = 1, P, 0

    count_a = 0   # A가 몇번 탐색하는지 카운트
    count_b = 0   # B가 몇번 탐색하는지 카운트

    while Pa != c:   # A먼저 카운트 해보기
        count_a += 1   # 일단 찾는 횟수 한번 +1
        c = (l + r) // 2   # 가운데는 왼쪽, 오른쪽 페이지 나누기 2의 몫
        if c == Pa:   # 만약 가운데 페이지가 목표 페이지와 같다면
            break   # 반복문 종료
        else:   # 다르다면
            if Pa > c:   # 페이지가 가운데보다 크다면
                l = c   # 가운데 페이지를 왼쪽페이지로
            elif Pa < c:   # 작다면
                r = c   # 가운데 페이지를 오른쪽 페이지로

    l, r, c = 1, P, 0   # 페이지 초기화

    while Pb != c:   # A팀과 동일하게
        count_b += 1
        c = (l + r) // 2
        if c == Pb:
            break
        else:
            if Pb > c:
                l = c
            elif Pb < c:
                r = c

    if count_a == count_b:   # 두 카운트 값이 같다면 0 출력
        print(f'#{tc + 1} 0')

    elif count_a < count_b:   # B가 더 크다면 A 승
        print(f'#{tc + 1} A')

    else:   # 작다면 B 승
        print(f'#{tc + 1} B')