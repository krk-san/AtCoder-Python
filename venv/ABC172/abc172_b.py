# function
def solve(S, T):
    ret = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ret += 1
    return ret


# main
if __name__ == '__main__':
    S = input()
    T = input()
    print(solve(S, T))
