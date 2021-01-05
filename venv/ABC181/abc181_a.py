# header
import sys

read = sys.stdin.buffer.read

# function
def solve(N):
    if N%2 == 0:
        return "White"
    else:
        return "Black"

# input
N = int(read())

# output
print(solve(N))