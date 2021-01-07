# header
import numpy as np


# function
def solve(N, AB):
    A_sum = AB.sum(0)[0]
    AB_plus = [2*ab[0] + ab[1] for ab in AB]
    AB_plus.sort(reverse=True)

    tot = 0
    for i in range(N):
        tot += AB_plus[i]
        if tot > A_sum:
            return i + 1


# main
if __name__ == '__main__':
    N = int(input())
    AB = np.array([list(map(int, input().split())) for _ in range(N)])

    print(solve(N, AB))