N = int(input())
R, G, B = map(int, input().split())
min_rgb = [R, G, B]
for _ in range(N - 1):
    R, G, B = map(int, input().split())
    R += min(min_rgb[1], min_rgb[2])
    G += min(min_rgb[0], min_rgb[2])
    B += min(min_rgb[1], min_rgb[0])
    min_rgb = [R, G, B]
print(min(min_rgb))
