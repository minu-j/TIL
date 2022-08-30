# T1, T2를 입력하면 그룹별 인원 최대, 최소값의 차를 출력하는 함수
def test(t1, t2):
    S = score
    A = 0
    B = 0
    C = 0
    for idx_s in range(len(S)):
        if t2 <= idx_s:
            A += S[idx_s]
        elif t1 <= idx_s < t2:
            B += S[idx_s]
        elif idx_s < t1:
            C += S[idx_s]

    if K_min <= A <= K_max and K_min <= B <= K_max and K_min <= C <= K_max:

        return max(A, B, C) - min(A, B, C)
    else:
        return False


for tc in range(int(input())):
    N, K_min, K_max = map(int, input().split())
    imp = list(map(int, input().split()))

    score = [0] * 101

    # 1~100점까지 몇명이 있는지 카운트해서 score 리스트에 저장
    for idx, i in enumerate(imp):
        score[i] += 1

    ans = 999999999999999   # 정답은 최소값이 출력되어야 하므로 일단 큰 수

    # 완전탐색해서 T1, T2값을 함수에 넣고 돌리기
    for T1 in range(1, 101):
        for T2 in range(T1, 101):
            T = test(T1, T2)
            if T is False:   # 함수 리턴값이 False면 넘기기
                continue
            else:
                if T < ans:   # 정답보다 작은 값이 리턴되면 정답을 리턴값에 저장
                    ans = T

    if ans == 999999999999999:   # 정답이 한번도 저장이 안됐으면(리턴값이 모두 False면)
        ans = -1                 # -1을 출력



    print(f'#{tc + 1} {ans}')
