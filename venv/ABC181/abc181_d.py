# function
def solve(S):
    cnt = [0] * 10
    keta = len(S)

    # count each number
    for s in S:
        cnt[int(s)] += 1

    # make 8 multiples list
    list_8 = [8 * i for i in range(1,125)]

    # Check
    for i in list_8:
        if len(str(i)) == 1 and keta != 1:
            continue
        if len(str(i)) == 2 and keta != 2:
            continue

        cnt_need = [0] * 10
        tmp = i
        while tmp > 0:
            cnt_need[tmp%10] += 1
            tmp //= 10

        ok = True
        for j in range(10):
            if cnt_need[j] > cnt[j]:
                ok = False
                break
        if ok:
            return "Yes"

    return "No"


# main
if __name__ == '__main__':
    S = input()
    print(solve(S))