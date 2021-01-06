# header

# function
def solve(N, W, STP):
    # imos
    P_sum = [0] * 200100

    for stp in STP:
        s, t, p = stp
        P_sum[s] += p
        P_sum[t] -= p

    for i in range(200010):
        if P_sum[i] > W:
            return "No"
        P_sum[i+1] += P_sum[i]

    return "Yes"

# main
if __name__ == '__main__':
    N, W = map(int, input().split())
    STP = [map(int, input().split()) for _ in range(N)]
    print(solve(N, W, STP))