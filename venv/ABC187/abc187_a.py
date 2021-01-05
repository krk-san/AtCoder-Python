# import

# function
def S(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

# main
if __name__ == "__main__":
    # input
    A, B = map(int, input().split())

    # output
    print(max(S(A), S(B)))