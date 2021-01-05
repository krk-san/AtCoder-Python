# import

# function
def solve(N, S):
    S_set1 = set(s for s in S)
    for s in S:
        if (s in S_set1) and ( '!' + s in S_set1):
            return s
    return "satisfiable"

# main
if __name__ == "__main__":
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(solve(N, S))


