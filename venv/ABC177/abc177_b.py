# function
def solve(S, T):
    ret = len(T)

    for i in range(len(S)-len(T)+1):
        cnt = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                cnt += 1
        ret = min(ret, cnt)

    return ret


# main
if __name__ == '__main__':
    S = input()
    T = input()
    print(solve(S, T))
