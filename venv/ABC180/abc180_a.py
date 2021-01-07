# header

# function
def solve(N, A, B):
    ret = N - A + B
    return ret


# main
if __name__ == '__main__':
    N, A, B = map(int, input().split())
    print(solve(N, A, B))