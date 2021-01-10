# header
import itertools


# function
def solve(N, P, Q):
    lis = [x for x in range(1, N+1)]
    lis_permutations = list(itertools.permutations(lis))
    a = lis_permutations.index(P)
    b = lis_permutations.index(Q)
    return abs(a - b)


# main
if __name__ == '__main__':
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))
    print(solve(N, P, Q))