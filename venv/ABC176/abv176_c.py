# function
def solve(N, A):
    ret = 0
    h_max = 0

    for i in range(N):
        ret += max(0, h_max-A[i])
        h_max = max(h_max, A[i])

    return ret


# main
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))