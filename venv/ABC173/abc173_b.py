# header
from collections import defaultdict


# function
def solve(N, S):
    result = ['AC', 'WA', 'TLE', 'RE']
    num_dict = defaultdict(int)

    for s in S:
        for res in result:
            if s == res:
                num_dict[s] += 1

    for res in result:
        print(f"{res} x {num_dict[res]}")


# main
if __name__ == '__main__':
    N = int(input())
    S = [input() for i in range(N)]
    solve(N, S)