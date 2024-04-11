N = int(input())
A, B = map(int, input().split())
ans = 0
coords = set([tuple(map(int, input().split())) for _ in range(N)])
for coord in coords:
    if ((coord[0] + A, coord[1] + B) in coords) and ((coord[0] + A, coord[1]) in coords) and ((coord[0], coord[1] + B) in coords):
        ans += 1
print(ans)
