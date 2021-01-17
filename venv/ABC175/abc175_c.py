# function
def solve(X, K, D):
    if X >= K*D:
        return abs(X-K*D)

    step = X // D
    d = X - D*step
    if (K-step)%2 == 0:
        return d
    else:
        return abs(d-D)


# main
if __name__ == '__main__':
    X, K, D = map(int, input().split())
    print(solve(abs(X), K, D))