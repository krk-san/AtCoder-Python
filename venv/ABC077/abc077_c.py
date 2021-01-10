# header
import bisect


# function
def solve(N, A, B, C):
    ret = 0
    A.sort()
    B.sort()
    C.sort()

    for b in B:
        ret += bisect.bisect_right(A, b-1) * (N-bisect.bisect_left(C, b+1))

    return ret

# main
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(solve(N, A, B, C))