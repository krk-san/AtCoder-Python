# header
MOD = 1000000007

# function
def solve(N, A):
    ret = 0
    A_sum = [0] * (N+1)

    for i, a in enumerate(A):
        A_sum[i+1] = (A_sum[i] + a)%MOD

    for i in range(N-1):
        ret += (A[i] * (A_sum[N] - A_sum[i+1]))%MOD
        ret %= MOD

    return ret


# main
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))