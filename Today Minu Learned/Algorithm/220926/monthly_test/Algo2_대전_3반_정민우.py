# T1을 전위순회하여 값을 리스트에 저장
def pre(n):
    if n > N:
        return
    T1_pre.append(n)
    pre(n * 2)
    pre(n * 2 + 1)


# 중위순회
def mid(n):
    if n > N:
        return
    mid(n * 2)
    T1_mid.append(n)
    mid(n * 2 + 1)


# 후위순회
def post(n):
    if n > N:
        return
    post(n * 2)
    post(n * 2 + 1)
    T1_post.append(n)


# 중위순회하여 정답 출력
def ans(n):
    if n > N:
        return
    ans(n * 2)
    print(T2[n], end=' ')
    ans(n * 2 + 1)


for tc in range(int(input())):
    N = int(input())
    T1 = list(range(N + 1))
    T2 = [0] * (N + 1)

    T1_pre = [0]
    T1_mid = [0]
    T1_post = [0]

    pre(1)
    mid(1)
    post(1)

    # 순회한 순서중에서 가장 높은 값을 T2 노드에 저장
    for i in range(1, N + 1):
        T2[i] = max(T1_pre[i], T1_mid[i], T1_post[i])

    print(f'#{tc + 1}', end=' ')
    ans(1)
    print()
