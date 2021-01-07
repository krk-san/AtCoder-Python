# header
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


# function
def solve(Sx, Sy, Gx, Gy):
    ret = (Sx*Gy + Gx*Sy) / (Gy + Sy)
    return ret


# main
if __name__ == '__main__':
    Sx, Sy, Gx, Gy = map(float, readline().split())
    print(solve(Sx, Sy, Gx, Gy))