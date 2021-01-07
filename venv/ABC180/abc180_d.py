# function
def solve(X, Y, A, B):
    ret = 0
    while A*X <= B+X and A*X <= Y:
        X *= A
        ret += 1
    ret += (Y-X-1) // B
    return ret


# main
if __name__ == '__main__':
    X, Y, A, B = map(int, input().split())
    print(solve(X, Y, A, B))