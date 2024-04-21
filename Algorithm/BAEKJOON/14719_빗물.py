H, W = map(int, input().split())
heights = list(map(int, input().split()))
rain = [0] * W

max_height = 0
for i in range(W):
    if max_height <= heights[i]:
        max_height = heights[i]

    rain[i] = (max_height - heights[i])

max_height = 0
for i in range(W - 1, -1, -1):
    if not rain[i]:
        break

    if max_height <= heights[i]:
        max_height = heights[i]

    rain[i] = (max_height - heights[i])

print(sum(rain))
