# function
def solve(H, W, K, c):
    ret = 0

    for h_bit in range(1<<H):
        for w_bit in range(1<<W):
            cnt = 0
            for i in range(H):
                mask_i = 1<<i
                if not (h_bit & mask_i):
                    continue
                for j in range(W):
                    mask_j = 1<<j
                    if not (w_bit & mask_j):
                        continue
                    if c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ret += 1

    return ret



# main
if __name__ == '__main__':
    H, W, K = map(int, input().split())
    c = [input() for i in range(H)]
    print(solve(H, W, K, c))