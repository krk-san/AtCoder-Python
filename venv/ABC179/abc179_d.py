# header
MOD = 998244353


# function
def solve(N, K, LR):
    dp = [0] * N
    sdp = [0] * (N+1)
    dp[0] = 1

    for i in range(N):
        for lr in LR:
            l = i - lr[1]
            r = i - lr[0] + 1
            dp[i] += sdp[max(0, r)] - sdp[max(0, l)]
            dp[i] %= MOD
        sdp[i+1] = sdp[i] + dp[i]
        sdp[i+1] %= MOD

    return dp[N-1]


# main
if __name__ == '__main__':
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    print(solve(N, K, LR))