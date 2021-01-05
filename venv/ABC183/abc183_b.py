# header
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# input
Sx, Sy, Gx, Gy = map(float, readline().split())

#output
ans = (Sx * Gy + Gx * Sy) / (Gy + Sy)
print(ans)