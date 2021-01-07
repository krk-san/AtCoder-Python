# header
import sys
read = sys.stdin.buffer.read


# function
def hexademical(x):
    ret = 0
    i = 0
    while x > 0:
        ret += (x % 8) * (10 ** i)
        i += 1
        x //= 8
    return ret


def check(x):
    while x > 0:
        if x % 10 == 7:
            return False
        x //= 10
    return True


def solve(N):
    ret = 0
    for i in range(1, N+1):
        if check(i) and check(hexademical(i)):
            ret += 1
    return ret


# main
if __name__ == '__main__':
    N = int(read())

    print(solve(N))