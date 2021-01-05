# header
import sys

readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# input
N = int(readline())

ans = 0
for i in range(N):
    a, b = map(int, readline().split())
    ans += ((a + b )  * (b - a + 1)) // 2

# output
print(ans)