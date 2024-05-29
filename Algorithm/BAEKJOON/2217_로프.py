N = int(input())
print(max([(N - i) * n for i, n in enumerate(sorted(int(input()) for _ in range(N)))]))