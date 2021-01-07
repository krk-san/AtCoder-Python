# header
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline


# function
def solve(N, A):
    ret = A[0]
    cnt_max = -1

    for k in range (2, max(A)+1):
        cnt = 0
        for a in A:
            if a%k == 0:
                cnt += 1
        if cnt > cnt_max:
            cnt_max = cnt
            ret = k

    return ret


# main
if __name__ == '__main__':
    N = int(readline())
    A = list(map(int, readline().split()))
    print(solve(N, A))