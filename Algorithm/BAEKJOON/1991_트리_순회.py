def find(depth):
    global pre, center, post

    pre += depth
    left, right = tree[depth]
    if left != ".":
        find(left)
    center += depth
    if right != ".":
        find(right)
    post += depth


N = int(input())
tree = dict()
pre = ''
center = ''
post = ''
for _ in range(N):
    P, L, R = input().split()
    tree[P] = (L, R)
find("A")
print(pre)
print(center)
print(post)