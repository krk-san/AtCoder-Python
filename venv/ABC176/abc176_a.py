# main
if __name__ == '__main__':
    N, X, T = map(int, input().split())
    ans = ((N-1)//X+1) * T
    print(ans)