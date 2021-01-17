# function
def solve(N, D, XY):
    ret = 0

    for xy in XY:
        if  xy[0]**2 + xy[1]**2 <= D**2:
            ret += 1

    return ret


# main
if __name__ == '__main__':
    N, D = map(int, input().split())
    XY = [list(map(int, input().split())) for i in range(N)]
    print(solve(N, D, XY))