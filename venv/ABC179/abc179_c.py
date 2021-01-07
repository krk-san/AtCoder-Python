# header
import math


# function
def solve(N):
    ret = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a*b >= N:
                break
            ret += 1
    return ret


# main
if __name__ == '__main__':
    N = int(input())
    print(solve(N))