# function
def solve(N, L):
    ret = 0

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i]==L[j] or L[j]==L[k] or L[k]==L[i]:
                    continue
                if L[i]+L[j] > L[k] and L[j]+L[k] > L[i] and L[k]+L[i] > L[j]:
                    ret += 1

    return ret


# main
if __name__ == '__main__':
    N = int(input())
    L = list(map(int, input().split()))
    print(solve(N, L))