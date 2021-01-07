# function
def solve(N, A):
    A.sort()
    ret = 0
    A_sum = [0] * (N + 1)
    for i in range(N):
        A_sum[i+1] = A_sum[i] + A[i]

    for i in range(N-1):
        ret += (A_sum[N] - A_sum[i+1]) - (N - i - 1) * A[i]
    return ret

# main
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))