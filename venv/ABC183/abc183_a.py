# header
import sys
read = sys.stdin.buffer.read


# main
if __name__ == '__main__':
    x = int(read())
    print(max(0, x))
