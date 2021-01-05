# header
import sys
import numpy as np
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

# Solve
def solve(N, K, T):
    l = [x+2 for x in range (N-1)]
    ans = 0
    for v in itertools.permutations(l):
        v = [1] + list(v) + [1]
        t = 0
        for i in range(N):
            t += T[v[i]-1][v[i+1]-1]
        if t == K:
            ans += 1
    return ans

# Input
N, K = map(int, readline().split())
T = np.array(read().split(), np.int64).reshape(N, N)

# Output
print(solve(N, K, T))