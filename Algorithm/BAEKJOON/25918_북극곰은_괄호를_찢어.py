N, S, stack, ans = int(input()), input(), [], 0
for s in S:
    if stack:
        now = stack.pop()
        if now == s:
            stack.extend([now, s])
    else:
        stack.append(s)
    ans = max(len(stack), ans)
if stack:
    print(-1)
else:
    print(ans)