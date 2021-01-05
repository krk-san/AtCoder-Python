from math import factorial

def comb(n, c):
    return factorial(n) // (factorial(n-c) * factorial(c))

L = int(input())
print(comb(L-1, 11))