# import
import math

# function
def divisor(x):
    ret = set()
    for i in range(1, int(math.sqrt(x))+1):
        if x % i == 0:
            ret.add(x // i)
            ret.add(i)
    ret = sorted(ret)
    return ret


def solve(N):
    div_N = divisor(N)
    for i in div_N:
        print(i)


# main
if __name__ == '__main__':
    N = int(input())
    solve(N)