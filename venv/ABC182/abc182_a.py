# header
import sys
read = sys.stdin.buffer.read


# function
def solve(A, B):
    ret = 2 * A +100 - B
    return ret


# main
if __name__ == '__main__':
    A, B = map(int, read().split())
    print(solve(A, B))