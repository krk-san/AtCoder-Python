def solve(N, M, T, A, B):
    H = N
    for i in range(M):
        H -= (A[i] - B[i])
        if H <= 0:
            return False
        H += (B[i+1] - A[i])
        H = min(N, H)
    if H > (T - B[M]):
        return True
    else:
        return False

N, M, T = map(int, input().split())

A = []
B = [0]

for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

B.append(T)

if solve(N, M, T, A, B):
    print("Yes")
else:
    print("No")
