# function
def solve(N, XY):
    ret = 0
    for i in range(0, N-1):
        for j in range(i+1, N):
            a = (XY[i][1]-XY[j][1]) / (XY[i][0]-XY[j][0])
            if a >= -1 and a <= 1:
                ret += 1
    return ret

# main
if __name__ == "__main__":
    N = int(input())
    XY = [list(map(int, input().split())) for i in range(N)]

    print(solve(N, XY))