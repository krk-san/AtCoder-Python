# header
import bisect


# function
def solve(N, M, K, A, B):
    # cumsum
    tot_A = [0] * (N+1)
    tot_B = [0] * (M+1)
    for i in range(N):
        tot_A[i+1] = tot_A[i] + A[i]
    for i in range(M):
        tot_B[i+1] = tot_B[i] + B[i]

    # calc
    ret = 0
    for i in range(N+1):
        t = tot_A[i]
        idx = bisect.bisect_right(tot_B, K-t)
        if idx == 0:
            continue
        else:
            ret = max(ret, i+idx-1)
    return ret


# main
if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve(N, M, K, A, B))