# A와 B에게 줄 음식의 재료를 각각 선택하는 함수
def select(depth):
    if depth >= N:
        if sum(sel) == N // 2:
            select_a = []
            select_b = []
            for _ in range(len(sel)):
                if sel[_] == 1:         # 1은 A의 재료
                    select_a.append(_)
                else:                   # 0은 B의 재료
                    select_b.append(_)
            A.append(select_a)
            B.append(select_b)
        return
    sel[depth] = 1
    select(depth + 1)
    sel[depth] = 0
    select(depth + 1)


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # powerset을 이용한 부분집합으로 각 음식의 재료 구하기
    sel = [0] * N
    A = []
    B = []
    select(0)

    # 최소값을 구하기 위해 큰 값 지정하기
    ans = 999999999

    # A, B에게 줄 재료를 순회하면서 해당 조합으로 만든 요리의 맛 최소값 구하기
    for i in range(len(A)):
        taste_A = 0
        taste_B = 0
        for j in range(N // 2):
            for k in range(N // 2):
                if not j == k:
                    taste_A += matrix[A[i][j]][A[i][k]]
                    taste_B += matrix[B[i][j]][B[i][k]]
        if abs(taste_A - taste_B) < ans:
            ans = abs(taste_A - taste_B)

    print(f'#{tc + 1} {ans}')
