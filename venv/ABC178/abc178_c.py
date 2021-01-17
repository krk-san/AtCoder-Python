# header
MOD = 1000000007

# main
if __name__ == '__main__':
    N = int(input())
    ans = pow(10, N, MOD) - (2*pow(9, N, MOD)- pow(8, N, MOD))
    ans %= MOD
    print(ans)