# 1. 완전탐색
# 모든 기둥의 양쪽에 기둥이 없을 때 까지 끝까지 찾기
# 그럴건 없을 것 같고, 왼쪽 오른쪽 기둥들의 최대높이를 각각 구하고 둘중 하나라도 제일 높은게 나랑 같으면 그 높이
# 모든 기둥 순회시 10^3 * 10^3 * 10^3이므로 완탐으로 가능할듯?

N = int(input())
container = [0] * 1001
for n in range(N):
    L, H = map(int, input().split())
    if container[L] < H:
        container[L] = H

maxHeight = max(container)

for c in range(1, len(container) - 1):
    container[c] = max(container[c], min(
        max(container[:c]), max(container[c + 1:])))

print(sum(container))


# 2. 좌, 우 끝에서부터 탐색하며 높이 좁혀나며 풀 수 있지 않을까?

N = int(input())
posts = sorted([tuple(map(int, input().split(' ')))
               for _ in range(N)], key=lambda x: x[0])

ans = 0

highestLeft = (0, 0)
for i in range(N):
    if posts[i][1] > highestLeft[1]:
        ans += highestLeft[1] * (posts[i][0] - highestLeft[0])
        highestLeft = posts[i]

highestRight = (1001, 0)
for i in range(N - 1, -1, -1):
    if posts[i][1] > highestRight[1]:
        ans += highestRight[1] * (highestRight[0] - posts[i][0])
        highestRight = posts[i]


print(ans + (highestLeft[1] * ((highestRight[0] + 1) - highestLeft[0])))
