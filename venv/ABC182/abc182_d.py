# function
def solve(N, A):
    ret = 0
    pos = 0

    A_sum = [0] * (N+1)
    A_sum_max = [0] * (N+1)

    for i in range(N):
        A_sum[i+1] = A_sum[i] + A[i]
        A_sum_max[i+1] = max(A_sum[i+1], A_sum_max[i])

    for i in range(N+1):
        ret = max(pos+A_sum[i], pos+A_sum_max[i], ret)
        pos += A_sum[i]
    return ret


# main
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))