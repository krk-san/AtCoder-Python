# function
def solve(S):
    if S[-1] == 's':
        S += 'es'
    else:
        S += 's'
    return S


# main
if __name__ == '__main__':
    S = input()
    print(solve(S))