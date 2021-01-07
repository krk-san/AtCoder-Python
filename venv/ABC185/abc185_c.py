# header
from math import factorial


# function
def comb(n, c):
    return factorial(n) // (factorial(n-c) * factorial(c))


# main
if __name__ == '__main__':
    L = int(input())
    print(comb(L-1, 11))