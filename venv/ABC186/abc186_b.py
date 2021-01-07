# header
import sys
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline


# function
def solve(H, W, A):
    ret = A.sum() - H * W * A.min()
    return ret


# main
if __name__ == '__main__':
    H, W = map(int, readline().split())
    A = np.array(read().split(), dtype = 'int64').reshape(H, W)

    print(solve(H, W, A))