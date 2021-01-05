# header
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

# function
def solve(N):
    keta = len(str(N))
    ret = keta
    for bit in range(1<<keta):
        tmp = 0
        cnt = 0
        for i in range(keta):
            mask = 1<<i
            if bit & mask:
                tmp += int(str(N)[i])
            else:
                cnt += 1
        if tmp%3 == 0:
            ret = min(ret, cnt)
    if ret == keta:
        ret = -1
    return ret

# input
N = int(readline())

# output
print(solve(N))