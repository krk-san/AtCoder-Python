# header
import heapq


# function
def check(X):
    lis = []
    for hs in HS:
        val = (X - hs[0]) // hs[1]
        lis.append(val)
    lis.sort()

    for cnt, val in enumerate(lis):
        if val < cnt:
            return False
    return True


def solve(N, HS):
    l = 0
    r = 1e+18
    X = (l+r) // 2

    while(r-l>1):
        X = (l+r) // 2
        if check(X):
            r = X
        else:
            l = X
    return int(r)


# main
if __name__ == '__main__':
    N = int(input())
    HS = [list(map(int, input().split())) for i in range(N)]
    print(solve(N, HS))