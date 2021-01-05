# header
import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

# function
def solve(H, W, A):
    ret = A.sum() - H * W * A.min()
    return ret

# input
H, W = map(int, readline().split())
A = np.array(read().split(), dtype = 'int64').reshape(H, W)

# output
print(solve(H, W, A))