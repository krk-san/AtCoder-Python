# function
def solve(N, M, ks, p):
    ret = 0
    for bit in range(1<<N):
        ok = True
        for i in range(M):
            cnt = 0
            for s in ks[i][1:]:
                mask = 1<<(s-1)
                if bit & mask:
                    cnt += 1
            if cnt%2 != p[i]:
                ok = False
                break
        if ok:
            ret += 1
    return ret


# main
if __name__ == '__main__':
    N, M = map(int, input().split())
    ks = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    print(solve(N, M, ks, p))