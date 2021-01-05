# header
import sys

read = sys.stdin.buffer.read

# input
N, W = map(int, read().split())

# output
ans = N // W
print(ans)