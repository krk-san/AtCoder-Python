# header
from functools import lru_cache

# function
@lru_cache(maxsize=None)
def f(a, b, c):
    MAX = 100
    if a == MAX or b == MAX or c == MAX:
        return 0
    ret = ((f(a+1, b, c) + 1) * a + (f(a, b+1, c) + 1) * b + (f(a, b, c+1) + 1) * c ) / (a + b + c)
    return ret

# main
if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(f(A, B, C))