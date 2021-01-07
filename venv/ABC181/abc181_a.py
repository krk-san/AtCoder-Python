# header
import sys
read = sys.stdin.buffer.read


# function
def solve(N):
    if N%2 == 0:
        return "White"
    else:
        return "Black"


# main
if __name__ == '__main__':
    N = int(read())
    print(solve(N))