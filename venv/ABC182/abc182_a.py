# header
import sys

read = sys.stdin.buffer.read

# input
A, B = map(int, read().split())

# output
ans = 2 * A +100 - B
print(ans)