# header
import sys
sys.setrecursionlimit(10 ** 7)


#function
def dfs(v, parent, G, cnt_G):
    cnt_G[v] += cnt_G[parent]

    for nv in G[v]:
        if nv != parent:
            dfs(nv, v, G, cnt_G)
    return


# main
if __name__ == '__main__':
    N, Q = map(int, input().split())
    G = [[] for _ in range(N+1)]
    cnt_G = [0] * (N+1)

    for i in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    for i in range(Q):
        p, x = map(int, input().split())
        cnt_G[p] += x

    dfs(1, 0, G, cnt_G)

    print(' '.join(map(str, cnt_G[1:])))