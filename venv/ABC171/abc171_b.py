# function
def solve(N, K, p):
    p.sort()
    ret = 0
    for i in range(K):
        ret += p[i]
    return ret


# main
if __name__ == '__main__':
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(N, K, p))