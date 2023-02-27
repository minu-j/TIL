import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    fr = [0] + list(map(int, input().split()))
    sr = [0] + list(map(int, input().split()))
    for c in range(2, n + 1):
        fr[c] = fr[c] + max(sr[c - 1], sr[c - 2])
        sr[c] = sr[c] + max(fr[c - 1], fr[c - 2])
    print(max(fr[n], sr[n]))