# 중위순회 활용
# 중위순회하며 방문하는 인덱스의 값이 정렬된 완전 이진 트리의 노드값과 같음을 활용
def inorder(n):
    if n > N:   # 노드값이 N보다 커질 경우 재귀 종료
        return
    inorder(n * 2)
    idx.append(n)   # 중위순회하며 방문한 인덱스값을 리스트에 저장
    inorder(n * 2 + 1)


for tc in range(int(input())):
    N = int(input())
    idx = [0]
    inorder(1)
    # 루트 노드의 값은, 인덱스 리스트의 1번 값에 해당하는 인덱스와 같을 것임.
    # N/2번 노드의 값은, 인덱스 리스트의 N/2번 값에 해당하는 인덱스와 같을 것임.
    print(f'#{tc + 1} {idx.index(1)} {idx.index(N // 2)}')
