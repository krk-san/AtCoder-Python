# main
if __name__ == '__main__':
    N = int(input())
    ans = ((N-1)//1000+1)*1000 - N
    print(ans)