# header
import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


# function
def solve(N):
    ret = 0
    for i in range(N):
        a, b = map(int, readline().split())
        ret += ((a+b) * (b-a+1)) // 2
    return ret


# main
if __name__ == '__main__':
    N = int(readline())
    solve(N)