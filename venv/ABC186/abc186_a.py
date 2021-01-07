# header
import sys
read = sys.stdin.buffer.read


# function
def solve(N, W):
    ret = N // W
    return ret


# main
if __name__ == '__main__':
    N, W = map(int, read().split())
    print(solve(N, W))