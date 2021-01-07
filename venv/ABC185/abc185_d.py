# function
def solve(N, M, A):
    ans = 0
    k = N

    for i in range(M+1):
        dA = A[i+1]-A[i]-1
        if dA == 0:
            continue
        k = min(k, A[i+1]-A[i]-1)

    for i in range(M+1):
        dA = A[i + 1] - A[i] - 1
        if dA == 0:
            continue
        ans += (((dA-1) // k) + 1 )

    return ans


# main
if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    A += [0, N+1]
    A.sort()

    print(solve(N, M ,A))

