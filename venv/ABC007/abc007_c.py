# header
from collections import deque

INF = 1e+9

# function
def solve(R, C, sy, sx, gy, gx, c):
    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1

    q = deque()
    q.append([sy, sx])
    dist = [[INF] * C for _ in range(R)]
    dist[sy][sx] = 0
    map_next = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    while len(q) != 0:
        y = q[0][0]
        x = q[0][1]
        q.popleft()

        for nyx in map_next:
            ny = y + nyx[0]
            nx = x + nyx[1]
            if (c[ny][nx] == '.') and (dist[ny][nx] == INF):
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny, nx])

    return dist[gy][gx]


# main
if __name__ == '__main__':
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    c = [list(input()) for _ in range(R)]
    print(solve(R, C, sy, sx, gy, gx, c))