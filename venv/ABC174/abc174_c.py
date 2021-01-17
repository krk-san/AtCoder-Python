# function
def solve(K):
    num = 0
    tmp = 1

    for i in range(K+1):
        num += tmp * 7
        num %= K
        if num == 0:
            return (i+1)
        tmp *= 10
        tmp %= K

    return -1


# main
if __name__ == '__main__':
    K = int(input())
    print(solve(K))