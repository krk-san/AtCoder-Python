# header
import math

# function
def manhattan(N, x):
    ret = 0
    for i in x:
        ret += abs(i)
    return ret


def euclid(N, x):
    ret = 0
    for i in x:
        ret += i ** 2
    ret = math.sqrt(ret)
    return ret


def chebyshev(N, x):
    ret = 0
    for i in x:
        ret = max(ret, abs(i))
    return ret


# main
if __name__ == '__main__':
    N = int(input())
    x = list(map(int, input().split()))

    print(manhattan(N, x))
    print(euclid(N, x))
    print(chebyshev(N, x))