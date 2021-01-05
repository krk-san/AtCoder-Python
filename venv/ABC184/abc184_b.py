N, X = list(map(int, input().split()))
S = input()

ans = X

for s in S:
    if s =='o':
        ans += 1
    else:
        ans -= 1
    ans = max(0, ans)

print(ans)