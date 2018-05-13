# Uses python3
import sys

def get_change(m):
    num_ten = m // 10
    remainder = m % 10
    num_five = remainder // 5
    remainder = remainder % 5
    num_one = remainder
    x = num_ten + num_five + num_one
    return x

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
