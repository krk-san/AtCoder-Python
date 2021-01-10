# header
import itertools
import math

# function
def solve(N, xy):
    lis = [x for x in range(N)]
    lis_permutations = itertools.permutations(lis)

    ret = 0
    cnt = 0
    for lis_permu in lis_permutations:
        for i in range(len(lis_permu)-1):
            x1 = xy[lis_permu[i]][0]
            x2 = xy[lis_permu[i+1]][0]
            y1 = xy[lis_permu[i]][1]
            y2 = xy[lis_permu[i+1]][1]
            ret += math.sqrt((x1-x2)**2 + (y1-y2)**2)
        cnt += 1
    ret /= cnt
    return ret


# main
if __name__ == '__main__':
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, xy))