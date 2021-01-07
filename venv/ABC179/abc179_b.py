# function
def solve(N, D):
    cnt = 0
    for d in D:
        if d[0] == d[1]:
            cnt += 1
            if cnt >= 3:
                return "Yes"
        else:
            cnt = 0
    return "No"


# main
if __name__ == '__main__':
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, D))