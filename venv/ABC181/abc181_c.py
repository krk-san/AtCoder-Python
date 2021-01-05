# header

# function
def solve(N, XY):
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if (XY[j][1] - XY[i][1]) * (XY[k][0] - XY[i][0]) == (XY[j][0] - XY[i][0]) * (XY[k][1] - XY[i][1]):
                    print("Yes")
                    return
    print("No")
    return
# main
if __name__ == "__main__":
    # input
    N = int(input())
    XY = [list(map(int, input().split())) for i in range(N)]
    solve(N, XY)